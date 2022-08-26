from django.contrib import admin
from .models import Form


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ("work_date", "user","crew_status", "site_ID", "CX_status", "completeness", "daily", "next_day", "our_notes", "market")
    search_fields  = ("user","crew_status", "site_ID", "CX_status", "completeness", "daily_progress", "next_day_plan", "notes", "market")
    
    def our_notes(self, obj):
        loadedNotes = obj.notes
        if len(loadedNotes) > 10:
            return loadedNotes[0:7]+" ..."
        else:
            return loadedNotes
    
    def daily(self, obj):
        daily_prog = obj.daily_progress
        if len(daily_prog) > 10:
            return daily_prog[0:7]+" ..."
        else:
            return daily_prog

    def next_day(self, obj):
        next = obj.next_day_plan
        if len(next) > 10:
            return next[0:7]+" ..."
        else:
            return next

# Register your models here.
