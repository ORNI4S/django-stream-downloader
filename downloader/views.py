import requests
from django.http import HttpResponse, Http404
from django.views import View
from django.shortcuts import render
import requests
from django.http import StreamingHttpResponse
from . import forms

import magic
import mimetypes

import subprocess




# python
# from django.http import StreamingHttpResponse

# def stream_video(request):
#     def file_iterator():
#         CHUNK_SIZE = 1024
#         while True:
#             chunk = process.stdout.read(CHUNK_SIZE)
#             if not chunk:
#                 break
#             yield chunk
#     response = StreamingHttpResponse(file_iterator(), content_type="video/mp4")
#     response['Content-Disposition'] = 'attachment; filename="video.mp4"'
#     return response



class stream_url(View):

    def get(self , request):
        form = forms.linkform() 
        return render(request , 'link.html' , {'form' : form})
    
    def post(self , request): 
        form = forms.linkform(request.POST)
        if form.is_valid():
            url = form.cleaned_data['link']
            process = subprocess.Popen(["yt-dlp", "-o", "-", url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            def file_iterator():
                CHUNK_SIZE = 8192
                while True:
                    chunk = process.stdout.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    yield chunk
            response = StreamingHttpResponse(file_iterator(), content_type="video/mp4")
            response['Content-Disposition'] = 'attachment; filename="video.mp4"'
            return response



# class stream_url(View):

#     def get(self , request):
#         form = forms.linkform() 
#         return render(request , 'link.html' , {'form' : form})
    
#     def post(self , request): 
#         form = forms.linkform(request.POST)
#         if form.is_valid():

#             url = form.cleaned_data['link']
            
#             response = requests.get(url, stream=True)
#             filename = url.split('/')[-1]
#             content_type = response.headers.get('Content-Type')
#             if not content_type:
#                 guessed_type, encoding = mimetypes.guess_type(filename)
#                 content_type = guessed_type or 'application/octet-stream'
#             file_size = int(response.headers['Content-Length'])
#             response = StreamingHttpResponse(
#                 response.iter_content(chunk_size=1024),
#                 content_type=content_type,
#             )
#             response['Content-Disposition'] = f'attachment; filename="{filename}.mp4"'
#             response['Content-Length'] = file_size
#             return response

# class stream_url(View):

#     def get(self , request) :
#         form = forms.linkform() 
#         return render(request , 'link.html' , {'form' : form})
    
#     def post(self , request) : 
#         form = forms.linkform(request.POST)
#         if form.is_valid() : 

#             url = form.cleaned_data['link']
            
        

#             response = requests.get(url, stream=True)
#             filename = url.split('/')[-1]
#             content_type = response.headers['Content-Type']
#             file_size = int(response.headers['Content-Length'])
#             response = StreamingHttpResponse(
#                 response.iter_content(chunk_size=1024),
#                 content_type=content_type,
#             )
#             response['Content-Disposition'] = f'attachment; filename="{filename}"'
#             response['Content-Length'] = file_size
#             return response