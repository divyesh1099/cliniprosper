from django.db import models
from django.utils import timezone

# Create your models here.
class Lecture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    meet_link = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    @property
    def is_upcoming(self):
        return timezone.now() < self.date

    @property
    def has_passed(self):
        return timezone.now() > self.date