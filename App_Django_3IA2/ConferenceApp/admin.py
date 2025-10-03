from django.contrib import admin

from ConferenceApp.models import Conference,Submission
admin.site.register(Conference)
admin.site.register(Submission)
admin.site.site_title = "Gestion des conférences"
admin.site.site_header = "Administration des conférences"
admin.site.index_title = "Bienvenue dans l'interface d'administration"