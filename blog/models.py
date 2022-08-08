from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
from django.core.validators import FileExtensionValidator

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog/images') # media url paxi blog/images create garxa ra tes vitra store hunxa photos
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at',) #ordering the latestpost to the first by - reversing 

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)


# model for the user
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profilemodel")
    image = models.ImageField(default='default.png', upload_to="blog/images/profile", validators=[FileExtensionValidator(['png','jpg'])])
    #biography thapera models pani banaune

    def __str__(self):
        return self.user.username