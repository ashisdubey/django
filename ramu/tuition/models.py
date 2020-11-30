from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=128)
    feedback = models.CharField(max_length=3000)
    posted_on = models.DateField

    def __str__(self):
        return f"{self.name} ({self.feedback})"

class Enquiry(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=128)
    enquiry = models.CharField(max_length=3000)
    posted_on = models.DateField
    reply = models.CharField(max_length=3000)
    replied_on = models.DateField
    reply_id = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.enquiry} - {self.reply}"
