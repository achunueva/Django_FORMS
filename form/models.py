from django.db import models
from django.db import models

# Create your models here.
class Model_text(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def str(self):
        return self.title