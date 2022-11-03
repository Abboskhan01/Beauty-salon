from django.contrib import admin
from django.apps import apps

admin.register.site(apps.all_models['api'].values())
