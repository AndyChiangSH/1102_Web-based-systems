from django.db import models

# Create your models here.
class HW7(models.Model):
    column1 = models.CharField(default="江尚軒")
    column1 = models.PositiveIntegerField(default=4108056005)
    pub_time = models.DateTimeField(auto_now=True)