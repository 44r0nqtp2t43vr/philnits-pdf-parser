from django.contrib.postgres.fields import ArrayField
from django.db import models

class Question(models.Model):
    question = models.TextField()
    image = models.ImageField(upload_to = 'uploads/', null = False)
    answer = models.CharField(max_length = 1, null = False, blank = False)
    choices = ArrayField(
        models.TextField(),
        size = 4,
        blank = True,
        null = False
    )

    class Meta:
        app_label = 'my_app'
