from django.db import models

# Create your models here.
class job(models.Model) :                                        #table
    title=models.CharField(max_length=100)                       #column
    #location
    JOB_TYPE={
        ('FULL TIME', 'FULL TIME'),
        ('PART TIME','PART TIME')
    }
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    #category
    experience=models.IntegerField(default=1)
    def __str__(self):
        return self.title
