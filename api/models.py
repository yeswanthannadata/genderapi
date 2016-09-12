from django.db import models

# Create your models here.

class Details(models.Model):
    first_name    = models.CharField(max_length=255)
    last_name     = models.CharField(max_length=255)
    gender        = models.CharField(max_length=255)

    class Meta:
        db_table = u'details'
    def __unicode__(self):
        return self.first_name

