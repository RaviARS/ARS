from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, PostArticleForm
from .models import PostArticle


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # USERNAME_FIELD = user.username
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def post(request):
    return render(request, 'post.html')


@login_required
def category(request):
    return render(request, 'category.html')


@login_required
def article_post(request):
    """ S23 Conference Registration Form. """

    def handle_uploaded_file(f):
        with open('articlefeeds/static/img/upload/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    if request.method == "POST":
        form = PostArticleForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['images'])
            form.save()
            return redirect("article-list")
    else:
        form = PostArticleForm()
    return render(request, 'article_post.html', {'form': form})


@login_required
def article_list(request):
    """ S23.1 post_article Registered List. """
    # print((USERNAME_FIELD), "$"*33)
    # for i, j in User.username:
    #     print(i, j)
    articles = PostArticle.objects.all().order_by('-id')
    return render(request, 'article_list.html', {'articles': articles})


@login_required
def article_edit(request, id):
    """ S23.2 post_article Form Edit. """

    article = PostArticle.objects.get(id=id)
    return render(request, 'article_edit.html', {'article': article})


@login_required
def article_update(request, id):
    """ S23.3 post_article Form Update. """

    article = PostArticle.objects.get(id=id)
    form = PostArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect("/article-list")
    return render(request, 'article_edit.html', {'article': article})


@login_required
def article_destroy(request, id):
    """ S23.4 post_article Form Delete. """

    user_article = PostArticle.objects.get(id=id)
    user_article.delete()
    return redirect("/article-list")


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
