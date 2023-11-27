from django.db import models

# Create your models here.
class Note(models.Model):
    # Title of the note
    title = models.CharField(max_length=255)

    # The PDF file
    file = models.FileField(upload_to='notes/')

    # Upload date
    upload_date = models.DateTimeField(auto_now_add=True)

    # Optional description
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]