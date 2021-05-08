from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import *
from .forms import SignUpForm

# Viewer Views
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def explore(request):
    posts = Post.objects.all()
    cat = ChannelCategory.objects.all()
    return render(request, 'explore.html', {'posts': posts, 'cat': cat})

def trending(request):
    posts = Post.objects.all()
    return render(request, 'trending.html', {'posts': posts})

def popular(request):
    posts = Post.objects.all()
    return render(request, 'popular.html', {'posts': posts})

def history(request):
    posts = Post.objects.all()
    return render(request, 'history.html', {'posts': posts})

def subscriptions(request):
    return render(request, 'subscriptions.html')

def mychannel(request):
    return render(request, 'mychannel.html')

def aboutuser(request):
    return render(request, 'aboutuser.html')

def editprofile(request):
    if request.method == 'POST':
        pi = UserProfile.objects.get(id= request.user.userprofile.id)
        pi.user = request.user
        request.user.first_name = request.POST.get('fname')
        request.user.last_name = request.POST.get('lname')
        request.user.username = request.POST.get('username')
        request.user.email = request.POST.get('email')
        request.user.save()
        pi.phone = request.POST.get('phone')
        pi.city = request.POST.get('city')
        pi.country = request.POST.get('country')
        pi.state = request.POST.get('state')
        pi.address = request.POST.get('address')
        pi.dob = request.POST.get('dob')
        pi.gender = request.POST.get('gender')
        pi.save()
        messages.success(request, "Information added sucessfully")
        return render(request, 'editprofile.html')
    else:
        return render(request, 'editprofile.html')

def userplaylist(request):
    return render(request, 'userplaylist.html')

def wallet(request):
    return render(request, 'wallet.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form' : form})

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            #Get the post parameter
            username = request.POST.get('username')
            password = request.POST.get('password')
            print("Login Start")
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if user is not None: 
                auth_login(request, user)
                messages.success(request, "Sucessfully Login into Talent Height")
                print("Logged in")
                return redirect('index')
            else:
                messages.error(request, "Invalid Credentials!  Please try again")
                return redirect('signin')
    
    return render(request, 'signin.html')

def logout(request):
    auth_logout(request)
    messages.info(request, "Successfully Logged Out")   
    return redirect('index')

def openvideo(request, pid):
    post = Post.objects.get(id=pid)
    return render(request, 'video-details.html', {'post': post})



#Creator Views
def dashboard(request):
    posts = Post.objects.all
    chan = Channel.objects.filter(user=request.user)
    return render(request, 'creator_dashboard/index.html', {'posts': posts, 'chan': chan})

def bankaccount(request):
    if request.method == 'POST':
        bank = Bank()
        bank.user = request.user
        bank.accountnumber = request.POST.get('accountnumber')
        bank.accountname = request.POST.get('accountname')
        bank.name = request.POST.get('name')
        bank.ifsc = request.POST.get('ifsc')
        bank.save()
        messages.success(request,"Bank Detailed added Successfully")
        return render(request, 'creator dashboard/profile-edit.html')
    else:
        return render(request, 'creator dashboard/profile-edit.html')

def channels(request):
    Category = ChannelCategory.objects.all()
    chan = Channel.objects.filter(user=request.user)
    if request.method == 'POST':   
        ccat = ChannelCategory.objects.get(name=request.POST.get('category'))
        channel = Channel()
        channel.user = request.user
        channel.name = request.POST.get('name')
        channel.category = ccat
        channel.description = request.POST.get('description')
        channel.save()
        messages.success(request,"Channel Created Successfully")
        return render(request, 'creator_dashboard/channel.html', {'Category': Category, 'chan': chan})
    else:
        return render(request, 'creator_dashboard/channel.html', {'Category': Category, 'chan': chan})

def playlist(request):
    posts = Post.objects.all()
    play = Playlist.objects.filter(user=request.user)
    if request.method == 'POST':   
        playpost = Post.objects.get(name=request.POST.get('post'))
        playlist = Playlist()
        playlist.user = request.user
        playlist.name = request.POST.get('name')
        playlist.save()
        messages.success(request,"Playlist Created Successfully")
        return render(request, 'creator dashboard/playlist.html', {'posts': posts, 'play': play})
    else:
        return render(request, 'creator dashboard/playlist.html', {'posts': posts, 'play': play})

def uploadvideo(request):
    Category = ChannelCategory.objects.all()
    channels = Channel.objects.all()
    if request.method == 'POST':   
        channel = Channel.objects.get(id=request.POST.get('channel'))
        upload = Post()
        upload.title = request.POST.get('title')
        upload.description = request.POST.get('description')
        upload.save()
        messages.success(request,"Video Uploaded Successfully")
        return render(request, 'creator_dashboard/uploadvideo.html', {'Category': Category, 'channels': channels})
    else:
        return render(request, 'creator_dashboard/uploadvideo.html', {'Category': Category, 'channels': channels})












def starrating(request):
    posts = Post.objects.all
    return render(request, 'creator dashboard/rating.html', {'posts': posts,})

def subscribers(request):
    posts = Post.objects.all
    return render(request, 'creator dashboard/user.html', {'posts': posts,})



def myvideos(request):
    posts = Post.objects.all
    return render(request, 'myvideos.html', {'posts': posts,})

def accountsetting(request):
    posts = Post.objects.all
    return render(request, 'creator dashboard/account-setting.html', {'posts': posts,})

def profile(request):
    posts = Post.objects.all
    return render(request, 'creator dashboard/profile.html', {'posts': posts,})

def profileedit(request):
    posts = Post.objects.all
    return render(request, 'creator dashboard/profile-edit.html', {'posts': posts,})




def movie_category(request):
    return render(request, 'movie-category.html')

def M_details(request):
    return render(request, 'movie-details.html')

def show_category(request):
    return render(request, 'show-category.html')

def S_details(request):
    return render(request, 'show-details.html')

def signle(request):
    return render(request, 'show-signle.html')

def single(request):
    return render(request, 'show-single.html')

def watch(request):
    return render(request, 'watch-video.html')

def showlist(request):
    return render(request, "index.html") 

def contact(request):
    if request.method=="POST":
        try:
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            content =request.POST['content']
            contact=Contact()
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.content = content
            contact.save()
            messages.success(request,'Successfully Submited')
            return render(request, "contact.html") 
        except Exception as e:
            messages.error(request,'Error: '+str(e))
            print('Error: '+str(e))
            return render(request, "contact.html") 
    else:
        return render(request, "contact.html") 

#deepshikha
def channelcategory(request):
    if request.method=="POST":
        try:
            name=request.POST['name']
            active=request.POST['active']
            channelcategory=ChannelCategory()
            channelcategory.name = name
            channelcategory.active = active 
            channelcategory.save()
            messages.success(request,'Successfully Submited')
            return render(request, "channelcategory.html") 
        except Exception as e:
            messages.error(request,'Error: '+str(e))
            print('Error: '+str(e))
            return render(request, "channelcategory.html") 
    else:
        return render(request, "channelcategory.html")

def status(request):
    if request.method=="POST":
        try:
            user=request.POST['user']
            image=request.POST['image']
            created=request.POST['created']
            status=Status()
            status.user = user
            status.image = image
            status.created = created
            status.save()
            messages.success(request,'Successfully Submited')
            return render(request, "status.html") 
        except Exception as e:
            messages.error(request,'Error: '+str(e))
            print('Error: '+str(e))
            return render(request, "status.html") 
    else:
        return render(request, "status.html") 

def post(request):
    if request.method=="POST":
        try:
            channel=request.POST['channel']
            cat=request.POST['category']
            title=request.POST['title']
            video=request.POST['video']
            thumbnail = request.POST['thumbnail']
            posted=request.POST['posted']
            discription=request.POST['discription']
            likes=request.POST['likes']
            dislikes=request.POST['dislikes']
            posted=request.POST['posted']
            post=Post()
            post.channel = channel
            post.title = title
            post.video = video
            post.posted = posted
            post.discription = discription
            post.likes = likes
            post.dislikes = dislikes
            post.posted = posted
            post.save()
            messages.success(request,'Successfully Submited')
            return render(request, "post.html") 
        except Exception as e:
            messages.error(request,'Error: '+str(e))
            print('Error: '+str(e))
            return render(request, "post.html") 
    else:
        return render(request, "post.html") 

def award(request):
    if request.method=="POST":
        try:
            name=request.POST['name']
            min_subscriber_count=request.POST['min_subscriber_count']
            min_watch_time=request.POST['min_watch_time']
            image=request.POST['image']
            likes=request.POST['likes']
            message=request.POST['message']
            posted=request.POST['posted']
            award=Award()
            award.name = name
            award.min_subscriber_count = min_subscriber_count
            award.min_watch_time = min_watch_time
            award.posted = posted
            award.image= image
            award.likes = likes
            award.message = message
            award.save()
            messages.success(request,'Successfully Submited')
            return render(request, "award.html") 
        except Exception as e:
            messages.error(request,'Error: '+str(e))
            print('Error: '+str(e))
            return render(request, "award.html") 
    else:
        return render(request, "award.html") 

def monetization(request):
    if request.method=="POST":
        try:
            subscribers=request.POST['subscribers']
            views=request.POST['views']
            videos=request.POST['videos']
            likes=request.POST['likes']
            strikes=request.POST['strikes']
            watchtime=request.POST['watchtime']
            monetization=Monetization()
            monetization.subscribers = subscribers
            monetization.views = views
            monetization.videos = videos
            monetization.likes = likes
            monetization.strikes = strikes
            monetization.watchtime = watchtime
            monitization.save()
            messages.success(request,'Successfully Submited')
            return render(request, "monitization.html") 
        except Exception as e:
            messages.error(request,'Error: '+str(e))
            print('Error: '+str(e))
            return render(request, "monitization.html") 
    else:
        return render(request, "monitization.html") 