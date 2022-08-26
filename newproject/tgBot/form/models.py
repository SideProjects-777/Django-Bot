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
    currDay = models.DateField(auto_now=True)
    crewStatus = models.CharField(max_length=9,
                  choices=CREW,
                  default="WORK")
    siteID = models.TextField(max_length=10)
    CXstatus = models.CharField(max_length=9,
                  choices=CX,
                  default="CXS")
    completeness =models.TextField(max_length=100)
    dailyProgress = models.TextField(max_length=250)
    nextDayPlan = models.TextField(max_length=250)
    notes = models.TextField(max_length=250)
    market = models.TextField(max_length=250)
    user = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.currDay.strftime("%d-%m-%Y") +'  /   ' + self.user 

    def snippet(self):
        return self.nextDayPlan[:10]+'...'

