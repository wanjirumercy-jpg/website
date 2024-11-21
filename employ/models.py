from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"



class Slider(models.Model):
    slider_desc = models.TextField()
    slider_head = models.CharField(max_length=100)
    slider_btn = models.CharField(max_length=50)
    slider_image = models.ImageField(upload_to = 'slides/')

    def __str__(self):
        return self.slider_head


class Featured(models.Model):
    feature_desc = models.TextField()
    feature_title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.feature_title



class Service(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title






