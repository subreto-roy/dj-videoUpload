from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos_uploaded')
    else:
        form = VideoForm()
    return render(request, 'video/base.html', {'form': form})

