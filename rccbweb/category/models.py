from django.db import models
from django.contrib import admin
import uuid
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def getsorted_complaint(self):
        return self.complaints.order_by('-votes')


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def getsorted_complaint(self):
        return self.complaints.order_by('-votes')


class Complaint(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    complaint_txt = models.TextField(max_length=1000)
    reg_date = models.DateField('date posted')
    votes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="complaints")
    geotag = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="complaints")

    class Meta:
        ordering = ['-votes']

    def __str__(self):
        return self.complaint_txt


admin.site.register(Complaint)
admin.site.register(Location)
admin.site.register(Category)
