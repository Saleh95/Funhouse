from django.views import generic
from django.shortcuts import HttpResponse
from .models import Album

class IndexView(generic.ListView):
    template_name = 'Fun/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DeleteView):
    model = Album
    template_name = 'Fun/detail.html'

def song_download(request, pk):
    song = Album.song_set.objects.get(id=pk)
    fsock = open('/media/'+song.audio_file, 'r')
    response = HttpResponse(fsock, mimetype='audio/mpeg')
    response['Content-Disposition'] = "attachment; filename=%s - %s.mp3" % \
                                     (song.artist, song.song_title)
    return response