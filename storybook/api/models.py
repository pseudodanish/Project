from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Page(models.Model):
    # story = models.ForeignKey(Story, related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()

class ThreeDObject(models.Model):
    # page = models.ForeignKey(Page, related_name='objects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    model_file = models.FileField(upload_to='models/')
    position = models.JSONField()

class Texture(models.Model):
    # object = models.ForeignKey(ThreeDObject, related_name='textures', on_delete=models.CASCADE)
    texture_file = models.ImageField(upload_to='textures/')
