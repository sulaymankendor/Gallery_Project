from django.db import models

# Create your models here.

class Gallery(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Galleries', max_length=1000)
    date = models.DateField(auto_now_add=True)  
    time = models.TimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.description}: date={self.date}, time={self.time}'