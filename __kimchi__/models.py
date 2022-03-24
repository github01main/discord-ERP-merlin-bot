from django.db import models # use models attribute in django db.
from django.contrib.auth.models import User # use django authorized user attributes.

# Create your models here.

""" 1) Document
문서의 카테고리를 형성하는 model 입니다.
"""
class Document (models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200) # 게시물 이름 속성 접근.
    description = models.TextField(null=True, blank=True) # 게시물 설명 속성 접근.
    # participants =
    updated = models.DateTimeField(auto_now=True) # 업데이트 시간 속성 접근.
    created = models.DateTimeField(auto_now_add=True) # 생성 시간 속성 접근.

    """
    Document 모델의 값들 중에서 데이터화 하여 .html 공간에 쏴줄 하나의 형태는 name 입니다.
    """
    def __str__(self):
        return self.name

""" 2) Post_item
게시판을 형성하는 model 입니다.
"""
class Post_item (models.Model):
    # host = 
    # topic = 
    post_name = models.CharField(max_length=200) # 게시물 이름 속성 접근.
    description = models.TextField(null=True, blank=True) # 게시물 설명 속성 접근.
    # participants =
    updated = models.DateTimeField(auto_now=True) # 업데이트 시간 속성 접근.
    created = models.DateTimeField(auto_now_add=True) # 생성 시간 속성 접근.

    """
    Post_item 모델의 값들 중에서 데이터화 하여 .html 공간에 쏴줄 하나의 형태는 post_name 입니다.
    """
    def __str__(self):
        return self.post_name

""" 3) Message
전송할 메시지 form을 형성하는 model 입니다.
"""
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 생성된 유저 속성 접근.
    post_item = models.ForeignKey(Post_item, on_delete=models.CASCADE) # 생성된 게시물 속성 접근.
    message_field = models.TextField() # 게시물 메시지 공간 속성 접근.
    updated = models.DateTimeField(auto_now=True) # 업데이트 시간 속성 접근.
    created = models.DateTimeField(auto_now_add=True) # 생성 시간 속성 접근.

    """
    Message 모델의 값들 중에서 데이터화 하여 .html 공간에 쏴줄 하나의 형태는 message_field 입니다.
    """
    def __str__(self):
        return self.message_field[0:50]
    
    
