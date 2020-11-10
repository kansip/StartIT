from django.shortcuts import render, get_object_or_404
from app.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == "POST":
        form = feedback(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            fb = Feedback.objects.create(name=name, phone=phone,
                                         email=email,
                                         message=message)
            fb.save()
            messages.success(request, 'Profile updated successfully')
    return render(request, 'index.html')


def news(request):
    blog_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 15)  # сколько постов на 1 странице
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    return render(request, "news.html", {'posts': blog_list})


def new(request, post_id):
    return render(request, "new.html", {'post': get_object_or_404(Post, id=post_id)})
