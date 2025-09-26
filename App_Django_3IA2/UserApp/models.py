from django.db import models
from django.contrib.auth.models import AbstractUser
from ConferenceApp.models import Conference

class User(AbstractUser):

    user_id = models.CharField(max_length=8,primary_key=True,unique=True,editable=False)
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255)
    ROLE = [
           ("participant",'participant'),
           ("commitee"," membre du comité organisateur scientifique")
    ]
    role = models.CharField(max_length=255,choices=ROLE,default="participant")
    nationality = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updtate = models.DateTimeField(auto_now=True)



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