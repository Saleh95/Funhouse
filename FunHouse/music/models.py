from django.db import models
from django.contrib.auth.models import Permission, User
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist= models.CharField(max_length=140)
    title = models.CharField(max_length=500)
    album_logo = models.FileField(blank=True)
    genre = models.CharField(max_length=100)
    slug= models.SlugField(unique=True)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + ' - ' + self.artist

    class Meta:
        ordering=["-upload_date"]



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    video_id = models.CharField(max_length=50)
    audio_file = models.FileField(default='')

    def __str__(self):
        return self.song_title

def pre_save_Album_receiver(sender,instance,*args,**kwargs):
    slug= slugify(instance.title)
    exists= Album.objects.filter(slug=slug).exists()
    if(exists):
        slug= "%s-%s" % (instance.id,slugify(instance.title))

    instance.slug=slug

pre_save.connect(pre_save_Album_receiver,sender=Album)