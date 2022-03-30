from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


from .models import Article, Message, Topic, User
from .forms import ArticleForm, UserForm


def homeView(request):
    if request.GET.get('search') != None:
        search = request.GET.get('search') 
    else:
        search = ''

    articles = Article.objects.filter(
        Q(topic__name__icontains=search) | 
        Q(title__icontains=search) |
        Q(resume__icontains=search) |
        Q(body__icontains=search))

    articles_count = articles.count()
    topics = Topic.objects.all()

    context = {'articles': articles, 'topics': topics,'articles_count': articles_count, }
    return render(request, 'base/home.html', context)


def loginView(request):
    page_name = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Login')
        except:
                messages.error(request, 'Error')     

    context = {'page': page_name,}
    return render(request, 'base/login-register.html', context)


@login_required(login_url='/login/')
def logoutView(request):
    logout(request)

    return redirect('home')


def registerView(request):
    page_name = 'register'
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'page': page_name,'form': form,}
    return render(request, 'base/login-register.html', context)
    

def articleView(request, pk):
    article = Article.objects.get(id=pk)
    article_messages = article.message_set.all()
    messages_count = article_messages.count()

    if request.method == 'POST':
        msg = Message.objects.create(
            user=request.user,
            article=article,
            body=request.POST.get('body')
        )
        return redirect('article', pk=article.id)

    context = {'article': article,'comments': article_messages,'comments_count': messages_count,}
    return render(request, 'base/article-view.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    user_articles = user.article_set.all()

    context = {'user': user, 'user_articles': user_articles,}
    return render(request, 'base/profile-view.html', context)


@login_required(login_url='/login/')
def updateProfile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated.')
            return redirect('home')
    else:
        form = UserForm(instance=request.user)
    
    context = {'form': form,}
    return render(request, 'base/edit-user.html', context)



@login_required(login_url='/login/')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        messages(request, "You're not allowed here!")
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')

    context = {'object': message,}
    return render(request, 'base/delete-form.html', context)


@login_required(login_url='/login/')
def createArticle(request):
    form = ArticleForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created_at = Topic.objects.get_or_create(name=topic_name)

        Article.objects.create(
            author=request.user,
            topic=topic,
            title=request.POST.get('title'),
            resume=request.POST.get('resume'),
            body=request.POST.get('body'),

        )
        return redirect('home')

    context = {'form': form, 'topics':topics,}
    return render(request, 'base/article-form.html', context)


@login_required(login_url='/login/')
def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)

    if request.user == article.author and request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created_at = Topic.objects.get_or_create(name=topic_name)
        article.title = request.POST.get('title')
        article.topic = topic
        article.resume = request.POST.get('resume')
        article.body = request.POST.get('body')
        return redirect('home')


    context = {'form': form, }
    return render(request, 'base/article-form.html', context)


@login_required(login_url='/login/')
def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    
    if request.method == 'POST':
        article.delete()

        return redirect('home')

    context = {'object': article,}
    return render(request, 'base/delete-form.html', context)

