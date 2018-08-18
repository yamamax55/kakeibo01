from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponseRedirect
#from .models import Post
from .models import Kakikomi
from django.shortcuts import render, redirect
from . import forms, models
#from .models import Kakikomi
from .forms import KakikomiForm

def index(request):
    # return HttpResponse("Hello World! このページは投稿のインデックスです。")
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request):
    #post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html')

def registory(request):
    #post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/toroku.html')

def kakikomi(request):
    #return HttpResponse(f)
    #return HttpResponse(f.as_table())
    if request.method == 'POST':
        f = KakikomiForm(request.POST)
        form  = KakikomiForm(request.POST or None)
        if form.is_valid():
            models.Kakikomi.objects.create(**form.cleaned_data)

    else:
        f = KakikomiForm(request.POST or None)
        return render(request, 'posts/kakikomiform.html', {'form1': f} )
