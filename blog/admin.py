from django.contrib import admin
from .models import Post #앞에서 만든 Post모델을 가져온다.

admin.site.register(Post) #만든 모델을 관리자 페이지에서 볼려면!
