from django.db import models
from django.utils import timezone


# Create your models here.
class Qualifications(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    certifying_authority = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500)
    certificate_link = models.CharField(max_length=200, null=True)
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


class Services(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def description_items(self):
        return self.description.split(':')

    def __str__(self):
        return '#collapse'+self.name