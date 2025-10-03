from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
name_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        
        message='le titre de la conférence doit contenir uniquement des lettres et espaces (pas de chiffres).'
)

class Conference(models.Model):
    conference_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,validators=[name_validator])
    THEME = [
        ("IA","Computer science & IA"),
        ("SE","Science & eng"),
        ("SC","Social science"),
         ]
    theme = models.CharField(max_length=255, choices=THEME)
    location = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add= True)
    update = models.DateTimeField(auto_now=True)
    def clean(self):
        if self.start_date_date > self.end_date:
            raise ValidationError("la date de debut doit être preexterieur à la date de fin.")


class Submission(models.Model):
    submission_id = models.CharField(max_length=255,primary_key=True,unique=True)
    title  = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.TextField()
    paper = models.FileField(
        upload_to = "papers/"
    )
    STATUS =[
        ("submitted","accepted"),
        ("under review", "under review"),
        ("accepted", "accepted"),
        ("rejected", "rejected")
    ]
    status = models.CharField(max_length=50,choices=STATUS)
    payed = models.BooleanField(default=False)
    submission_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add= True)
    update = models.DateTimeField(auto_now=True)

    user = models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="submissions")
    conference = models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")


