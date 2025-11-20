from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return self.user.username
    
class Lead(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

   
    def save(self, *args, **kwargs):
        user = kwargs.pop("user", None)  

        if self.pk:  
            old = Lead.objects.get(pk=self.pk)
            if old.status != self.status:
                LeadHistory.objects.create(
                    lead=self,
                    old_status=old.status,
                    new_status=self.status,
                    updated_by=user
                )
                subject = f"Lead Status Updated: {self.name}"
                message = (
                    f"The status for lead '{self.name}' has changed.\n\n"
                    f"Old Status: {old.status}\n"
                    f"New Status: {self.status}\n"
                    f"Updated By: {user}\n"
                )

                recipients = []
                recipients.append(settings.DEFAULT_FROM_EMAIL)

                if self.assigned_to and self.assigned_to.email:
                    recipients.append(self.assigned_to.email)

                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    



class LeadHistory(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
