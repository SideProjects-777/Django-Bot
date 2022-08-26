from django.contrib import admin
from .models import Form


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ("work_date", "user","crew_status", "site_ID", "CX_status", "completeness", "daily_progress", "next_day_plan", "notes", "market")
    search_fields  = ("user","crew_status", "site_ID", "CX_status", "completeness", "daily_progress", "next_day_plan", "notes", "market")
    pass

# Register your models here.
