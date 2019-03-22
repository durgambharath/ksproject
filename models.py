from django.db import models

# Create your models here.
class quater1_watersupply(models.Model):
     Working_place=models.CharField(max_length=50)
     Water_supply_place=models.CharField(max_length=50)
     Electrical_meter_no=models.IntegerField()


     def _str (self):
         return self.Working_place

     def is_valid(self):
         pass

