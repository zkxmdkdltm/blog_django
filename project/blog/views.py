from django.shortcuts import render
from .models import Blog #같은 앱에 있는 models.py에 Blog class를 임포트한다.
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    blogs = Blog.objects.all() #Blog 테이블에서 모든 데이터를 가져옴
    return render(request,'home.html',{'blogs':blogs}) # rendering 해줌

def detail(request,id):
    blog = get_object_or_404(Blog,pk = id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()  # 빈 Blog 객체 생성
    new_blog.title =  request.POST['title']
	   # POST요청으로 받은 'title'의 데이터를 위에서 만든 객체의 title 컬럼에 할당
    new_blog.contents = request.POST['contents']
	   	   # POST요청으로 받은 'contents'의 데이터를 위에서 만든 객체의 contents 컬럼에 할당
    new_blog.image = request.FILES['image']
    new_blog.save() #실제 데이터베이스에 저장을 시키게 한다.
    
    return redirect('detail',new_blog.id) #새로 만들어준 상세페이지로 redirect한다

def edit(request,id):
    edit_blog = get_object_or_404(Blog,pk = id) # 파라미터 id를 받아서 디비에 해당 객체를 가져온다.
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog = get_object_or_404(Blog,pk=id) # 파라미터로 받은 id의 Blog 객체 가져옴
    update_blog.title = request.POST['title'] 
    update_blog.contents = request.POST['contents']
    try:
      update_blog.image = request.FILES['image']
    except:
      update_blog.image = None
    update_blog.save()
    return redirect('detail',update_blog.id)

def delete(request,id):
    delete_blog  = get_object_or_404(Blog,pk = id) #파라미터로 받은 id에 해당하는 Blog객체 가져옴
    delete_blog.delete() #삭제
    return redirect('home')