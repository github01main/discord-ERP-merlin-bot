from django.shortcuts import render, redirect                # move to where you want to landing url.
from django.http import HttpResponse                         # HttpResponse for this.
from django.contrib import messages                          # use message for response to user behaviour.

from django.db.models import Q                               # multiple section of mode object parameters.
from django.contrib.auth.models import User                  # use django authorized user attributes.
from django.contrib.auth import authenticate, login, logout  # user login logout authenticate.
from django.contrib.auth.decorators import login_required    # check interative dom object is it logined ?
from django.contrib.auth.forms import UserCreationForm       # Create user.

from .models import Category
from .models import Post
from .models import Topic
from .forms import PostForm

"""------------------------------------------------------------------------------------------------------------------------------------"""

""" [ Queset 작동 원리 ] 

queryset = ModelName.objects.all()

1) Queryset = 응답할 변수를 가지는 잡아두는 공간.
2) ModelName = 모델이름.
3) obejcts = 모델 오브젝트들의 속성.
4) all() 메소드 다른 예시 .get(), .filter(), .exclude()

"""
    
"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 1) 랜딩페이지.
    
    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""
def home(request):
    categories = Category.objects.all()
    
    # what do you want to send context to DOM space ?
    context = {'categories': categories}
    return render(request, 'extends/home.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 2) 카테고리.
    
    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""
def category(request, pk):
    q = request.GET.get('q') if request.GET.get('q') != None else '' # get the on the html of the q mark. of the links.
    posts = Post.objects.filter(Q(topic__name__icontains=q)   |      # filtering with models of Post in speicific data.
                                Q(name__icontains=q)          |
                                Q(description__icontains=q)   |
                                Q(host__username__icontains=q)
                                )
    post_count = posts.count()                                       # amount of post.             
    topics = Topic.objects.all()                                     # iterate all topics.
    
    categories = Category.objects.all()                              # iterate all categories.
    category = Category.objects.get(id=pk)                           # iterate all specific category when user want to access to target.
    description = category.description.splitlines()                  # description for the explain what 
    
    # what do you want to send context to DOM space ?
    context = {'category': category, 
               'post_count': post_count,
               'topics':topics,
               'description' : description,
               'categories': categories,
               'posts': posts}
    
    return render(request, 'extends/category.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 3) 게시물 생성.
    
    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""
#  게시물 생성 버튼을 클릭했으나 로그인이 되어있지않다면 login 페이지로 넘어가게된다.
@login_required(login_url='/category/5/login')
def createPost(request):
    form = PostForm()
    categories = Category.objects.all() #iterate al;l categories.
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category/3/')

    # what do you want to send context to DOM space ?
    context = {'form': form, 'categories':categories}
    return render(request, 'extends/createPost.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 4) 게시물 업데이트.
    
    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""

# Edit 버튼을 클릭했으나 로그인이 되어있지않다면 login 페이지로 넘어가게된다.
@login_required(login_url='/category/5/login')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    categories = Category.objects.all() #iterate al;l categories.
    
    # 자신이 생성한 게시물이 아니면 접근을 거부한다.
    if request.user != post.host:
        return HttpResponse(" Your are not allowed here !! ")
                            
    if request.method == 'POST':
        form =PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/category/3/')
        
    # what do you want to send context to DOM space ?
    context = {'form': form, 'categories':categories}
    return render(request, 'extends/createPost.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 5) 게시물 삭제.

    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""
# 삭제 버튼을 클릭했으나 로그인이 되어있지않다면 login 페이지로 넘어가게된다.
@login_required(login_url='/category/5/login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    categories = Category.objects.all() #iterate al;l categories.
    
    # 자신이 생성한 게시물이 아니면 접근을 거부한다.
    if request.user != post.host:
        return HttpResponse(" Your are not allowed here !! ")
        
    if request.method == 'POST':
        post.delete()
        return redirect('/category/3/')
    context = {'obj':post,'categories':categories}
    # what do you want to send context to DOM space ?
    return render(request, 'extends/deletePost.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 6) 게시물 primary key 공유 베이스.

    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""
def post(request, pk):
    post = Post.objects.get(id=pk)

    # what do you want to send context to DOM space ?
    context = {'post': post}
    return render(request, 'extends/community.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 7) 로그인페이지

    [1] 최근 수정일 : 2022-03-29 조시욱.
    [2] 최종 수정일 : 2022-03-30 조시욱.
"""
def loginPage(request):
    
    page = 'login'
    categories = Category.objects.all() #iterate al;l categories.
    # 로그인 이미 되어있는데 login url로 수동으로 입력하더라도 재 로그인 페이지가 아닌 커뮤니티 페이지로 넘어가게 된다.
    if request.user.is_authenticated:
        return redirect('/category/3/')
    
    # username 과 password입력값을 'get' 요청하여 dom에 전송한다. try catch는 유저의 데이터 값에 대한 예외처리이다.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username=username, password=password)
        
        # 입력된 유저의 데이터가 데이터 베이스에 존재한다면 커뮤니티 페이지로 넘어가게된다.
        if user is not None:
            login(request, user)
            return redirect('/category/3/')
        
        # 유저 이름 또는 패스워드가 일치 하지않는다면 messages.error를 발생시킨다.
        else:
            messages.error(request, 'Username OR password does not exit')
        
    # what do you want to send context to DOM space ?
    context = {'page': page, 'categories': categories}
    return render(request, 'extends/login.html', context)
    

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 8) 로그아웃

    [1] 최근 수정일 : 2022-03-29 조시욱.
    [2] 최종 수정일 : 2022-03-30 조시욱.
"""

    # 쿠키에 저장된 유저의 데이터 값을 삭제하고 login 페이지로 넘어가게 된다.
def logoutUser(request):
    logout(request)
    return redirect('/category/5/login')

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 9) 회원가입

    [1] 최근 수정일 : 2022-03-29 조시욱.
    [2] 최종 수정일 : 2022-03-30 조시욱.
"""

    # 쿠키에 저장된 유저의 데이터 값을 삭제하고 login 페이지로 넘어가게 된다.
def registerPage(request):
    form = UserCreationForm()
    categories = Category.objects.all() #iterate al;l categories.
    context = {'form':form, 'categories':categories}
    return render(request, 'extends/login.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 9) 컨택트

    [1] 최근 수정일 : 2022-03-29 조시욱.
    [2] 최종 수정일 : 2022-03-30 조시욱.
"""

    # 컨택트 도메인.
def contact(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'extends/contact.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""
