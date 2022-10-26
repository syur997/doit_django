from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')
    
    # 필요한 코드 넣기
    # render(request, '템플릿 파일', {'키':변수값}) -> 3개 필수로 넣어야함
    return render(
        request,
        'blog/index.html',
        {'posts': posts})
    # 파이썬 파일을 hmtl로 보내야하니까 렌더링해라
