from django.db import models

SUBJECT_CHOICES = (
    ('MATHS','Maths'),
    ('BEE','BEE'),
    ('MECHANICS','Mechanics'),
    ('PHYSICS','Physics'),
    ('CHEMISTRY','Chemistry'),
)
TYPE_CHOICE=(
    ('IAT1','IAT-1 Paper'),
    ('IAT2','IAT-2 Paper'),
    ('UNI','University Past Paper'),
    ('PRELIM','Prelims Papers'),
    ('TUTORIAL','Tutorial'),
    ('TT','Time Table')
)
# Create your models here.
class MCQ(models.Model):
    que=models.TextField()
    opt1=models.TextField()
    opt2=models.TextField()
    opt3=models.TextField()
    opt4=models.TextField()
    ans=models.IntegerField()

class PDF(models.Model):
    name = models.CharField(max_length=50)
    types = models.CharField(max_length=9, choices=TYPE_CHOICE)
    uploadque = models.FileField(upload_to="")
    uploadans = models.FileField(upload_to="",blank=True)
    year = models.IntegerField(blank=True)
    subject = models.CharField(max_length=9, choices=SUBJECT_CHOICES)

class Announcement(models.Model):
    text=models.TextField()
    upload=models.FileField(upload_to="",blank=True)