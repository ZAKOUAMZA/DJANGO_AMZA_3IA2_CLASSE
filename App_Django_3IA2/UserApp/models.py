from django.db import models
from django.contrib.auth.models import AbstractUser
from ConferenceApp.models import Conference
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import uuid
def generate_user_id():
    return "USER" + uuid.uuid4().hex[:4].upper()
   
def verify_email(email):
     domaines = ["esprit.tn","seasame.com","tek.tn","central.tn"]
     email_domaine =email.split('@')[1]
     if email_domaine not in domaines:
          raise ValidationError("l'email est invalide et doit appartenir à un des domaines suivants: esprit.tn, seasame.com, tek.tn, central.tn")
            
name_validator = RegexValidator(
    regex=r'^[a-zA-Z\s-]+$',
    message='Le nom doit contenir uniquement des lettres alphabétiques.'
)



class User(AbstractUser):

    user_id = models.CharField(max_length=8,primary_key=True,unique=True,editable=False)
    first_name = models.CharField(max_length=255,validators=[name_validator])
    last_name =  models.CharField(max_length=255,validators=[name_validator])
    affiliation = models.CharField(max_length=255)
    ROLE = [
           ("participant",'participant'),
           ("commitee"," membre du comité organisateur scientifique")
    ]
    role = models.CharField(max_length=255,choices=ROLE,default="participant")
    nationality = models.CharField(max_length=255)
    email = models.EmailField(unique=True,validators=[verify_email])
    created_at = models.DateTimeField(auto_now_add=True)
    updtate = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
            if not self.user_id:
                new_id = generate_user_id()
                while User.objects.filter(user_id=new_id).exists():
                    new_id = generate_user_id()
                self.user_id = new_id
            super().save(*args, **kwargs)


class OrganizingCommittee(models.Model):

    committee_role = models.CharField(max_length=50,choices=[
        ("chair","chair"),
        ("co-chair","co-chair"),
        ("member","member")
    ])
    date_joined = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="committees")
    conference = models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="committees")