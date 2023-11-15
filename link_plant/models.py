from django.db import models

# Create your models here.

#Profiles -> Links

class Profile(models.Model):
    BG_CHOICES =(
        ('blue', 'Blue'), 
        ('green', 'Green'), 
        ('yellow', 'Yellow'), 
    )

    #name, slug, bg-colour
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_colour = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        return self.name

class Link(models.Model):
    #text, url, profile

    text=models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')