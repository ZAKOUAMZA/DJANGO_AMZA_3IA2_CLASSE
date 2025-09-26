from django.db import models
#from ConferenceApp.models import Conference

class SessionApp(models.Model):
    session_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    session_day = models.DateField(auto_now=True)
    start_time =  models.TimeField()
    end_time =    models.TimeField()
    room = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    conference = models.ForeignKey('ConferenceApp.Conference', on_delete=models.CASCADE,related_name="sessions")
    #conference = models.ForeignKey(Conference, on_delete=models.CASCADE,related_name="sessions")