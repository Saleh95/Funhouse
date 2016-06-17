from django.db import models
from django.contrib.auth.models import Permission, User
from music.models import Song

class Profile(models.Model):
    user= models.OneToOneField(User)
    picture= models.ImageField(blank=True,default='default')
    background=models.ImageField(blank=True)
    favorite= models.ManyToManyField(Song,blank=True,default='')
    followers=models.ManyToManyField('self',blank=True,related_name='crush',symmetrical=False)
    following= models.ManyToManyField('self',blank=True,related_name='buddy',symmetrical=False)

    def __str__(self):
        return self.user.first_name+self.user.last_name+str(self.user.id)

User.profile=property(lambda u:Profile.objects.get_or_create(user=u)[0])

class Playlist(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    songs= models.ManyToManyField(Song,blank=True,default='')

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
