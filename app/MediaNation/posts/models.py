from django.db import models

# Create your models here.
class Posts(models.Model):
    '''Модель для таблиц'''

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title