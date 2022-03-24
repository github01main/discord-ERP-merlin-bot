from django.shortcuts import render
from .models import Document
from .models import Post_item

""" Queset 작동 원리 

queryset = ModelName.objects.all()

1) Queryset = 응답할 변수를 가지는 잡아두는 공간.
2) ModelName = 모델이름.
3) obejcts = 모델 오브젝트들의 속성.
4) all() 메소드 다른 예시 .get(), .filter(), .exclude()

"""
documents = [
    {'id':1, 'name':'Merlin Bot Start Tutorial'},
    {'id':2, 'name':'1. Setup to Discord'},
    {'id':3, 'name':'2. Commands'},
]
    
"""
Documents에 적힌 모든 object 리스트들을 출력하고 context에 적용합니다.
context 는 home에 키쌍 값들을 중 name 값들을 참조하여 home.html 도메인에 데이터를 보내줍니다.
"""
    # home Domain.
def home(request):
    documents = Document.objects.all()
    context = {'documents': documents}
    return render(request, 'extends/home.html', context)
"""
Documents에 적힌 모든 object 리스트들중 도메인의 primary key키는 document의 id로 가져와 context에 적용합니다.
context 는 document_page 특정 값의 name 값을 참조하여 document_page.html 도메인에 데이터를 보내줍니다.
"""
    # document_page Domain.
def document_page(request, pk):
    document = Document.objects.get(id=pk)
    context = {'document': document}
    return render(request, 'extends/document_page.html', context)

"""
Post_item에 적힌 모든 object 리스트들중 도메인의 primary key키는 Post_item에 id로 가져와 context에 적용합니다.
context 는 Post_item 특정 값의 name 값을 참조하여 post_item.html 도메인에 데이터를 보내줍니다.
"""
    # post Domain.
def post(request, pk):
    post_item = Post_item.objects.get(id=pk)
    context = {'post_item': post_item}
    return render(request, 'extends/post.html', context)
    
    # Contact Domain.
def contact(request):
    context3 = {'documents': documents}
    return render(request, 'extends/contact.html', context3)
