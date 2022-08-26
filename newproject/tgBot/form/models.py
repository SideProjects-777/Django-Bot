from pickle import TRUE
from django.db import models

# Create your models here.

CREW = (
    ("WORK", "At work"),
    ("OFF", "Day off"),
    ("VACATION", "Vacation"),
)

CX = (
    ("CXS", "CXS"),
    ("PROGRESS", "In progress"),
    ("HOLD", "On hold "),
    ("CXC", "CXC"),
)

class Form(models.Model):
    work_date = models.DateField(auto_now=True)
    crew_status = models.CharField(max_length=9,
                  choices=CREW,
                  default="WORK")
    site_ID = models.TextField(max_length=10)
    CX_status = models.CharField(max_length=9,
                  choices=CX,
                  default="CXS")
    completeness =models.TextField(max_length=100)
    daily_progress = models.TextField(max_length=250)
    next_day_plan = models.TextField(max_length=250)
    notes = models.TextField(max_length=250)
    market = models.TextField(max_length=250)
    user = models.TextField(max_length=250, null=True)

    def snippet(self):
        return self.nextDayPlan[:10]+'...'

