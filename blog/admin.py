# admin.py

from django.contrib import admin
from .models import Post

# 관리자 페이지에서 Post 모델을 보려면 이 부분을 등록해야 함.
admin.site.register(Post)
