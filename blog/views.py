from django.shortcuts import render
from .models import Post, Article
from accounts.forms import SignUpForm, LoginForm
from home.forms import ContactUsForm
# Create your views here.


def article_list(request):
    signup_form = SignUpForm()
    login_form = LoginForm()
    contact_form = ContactUsForm()
    
    article_list = Article.objects.filter(status=1).order_by('-pub_date')

    context = {
        'article_list': article_list,
        'signup_form': signup_form,
        'login_form': login_form,
        'contact_form': contact_form,
    }
    return render(request, 'article_list.html', context)


def article_view(request, slug):
    
    signup_form = SignUpForm()
    login_form = LoginForm()
    contact_form = ContactUsForm()

    article = Article.objects.filter(slug=slug)
    article_object = Article.objects.get(id=article[0].pk)
    article_object.views = article_object.views + 1
    article_object.save()

    posts = article[0].posts.filter(status=1).order_by('pub_date')
    
    context = {
        'article': article,
        'posts': posts,

        'signup_form': signup_form,
        'login_form': login_form,
        'contact_form': contact_form,
    }
    return render(request, 'article_view.html', context)


def article_category(request, category):
    signup_form = SignUpForm()
    login_form = LoginForm()
    contact_form = ContactUsForm()

    article_list = Article.objects.filter(
        categories__name__icontains=category.replace('-', ' ')
        ).order_by(
            '-pub_date'
        )

    toast_message = f"Search results for '{category}'"

    context = {
        'article_list': article_list,
        'toast_message': toast_message,

        'signup_form': signup_form,
        'login_form': login_form,
        'contact_form': contact_form,
    }
    return render(request, 'article_list.html', context)