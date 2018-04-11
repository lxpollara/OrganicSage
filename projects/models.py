from django.db import models

from django.utils import timezone
# Create your models here.


class ProjectLoc(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=100, choices=[('Consulting', 'Consulting'), ('Inspection', 'Inspection'), ('Other','Other')])
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    description = models.TextField(null=True)
    blog_post = models.CharField(max_length=200, null=True)
    image_src = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name