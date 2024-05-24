from django.db import models

# Create your models here.
class ChapterItem(models.Model):
    pos = models.IntegerField(default=0)
    subject = models.CharField(max_length=20)
    chpName = models.CharField(max_length=1000)
    status = models.CharField(max_length=20)
    note = models.CharField(max_length=50000, blank=True)