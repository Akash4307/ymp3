from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import youtube_dl
# Create your views here.


def url(request):
    print('yo')
    return render(request, 'index.html')


def process_url_from_client(request):
    url = request.POST.get('url')
    print('yo')

    print(url)



    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])




    return HttpResponse('')