from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User # use django authorized user attributes.
from django.contrib.auth import authenticate, login
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
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category/3/')

    # what do you want to send context to DOM space ?
    context = {'form': form}
    return render(request, 'extends/createPost.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 4) 게시물 업데이트.
    
    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    
    if request.method == 'POST':
        form =PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/category/3/')
        
    # what do you want to send context to DOM space ?
    context = {'form': form}
    return render(request, 'extends/createPost.html', context)

"""------------------------------------------------------------------------------------------------------------------------------------"""

"""
    # 5) 게시물 삭제.

    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/category/3/')

    # what do you want to send context to DOM space ?
    return render(request, 'extends/deletePost.html', {'obj':post})

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

    [1] 최근 수정일 : 2022-03-28 정심일.
    [2] 최종 수정일 : 2022-03-29 조시욱.
"""
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/category/3/')
        
        else:
            messages.error(request, 'Username OR password does not exit')
        
    # what do you want to send context to DOM space ?
    context = {}
    return render(request, 'extends/login.html', context)
    

"""------------------------------------------------------------------------------------------------------------------------------------"""

    # 컨택트 도메인.
def contact(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'extends/contact.html', context)
