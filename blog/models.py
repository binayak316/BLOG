
from unittest.util import _MAX_LENGTH
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
    image = models.ImageField(upload_to='blog/images', null=True, blank=True) # media url paxi blog/images create garxa ra tes vitra store hunxa photos
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at',) #ordering the latestpost to the first by - reversing 

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

    def comment_count(self):#comment count garna use gareko method
        return self.comments_set.all().count()
    
    def comments(self): #yo comments uta for comment in post.comments  ma bolaxa
        return self.comments_set.all()

 
# model for the user
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profilemodel")
    image = models.ImageField( upload_to="blog/images/profile", validators=[FileExtensionValidator(['png','jpg'])])
    bio = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text