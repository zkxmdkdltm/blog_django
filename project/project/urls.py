from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import blog.views # 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name = "home"), # 추가
    path('blog/<int:id>',blog.views.detail,name="detail"),#추가
    path('new',blog.views.new,name = 'new'),
    path('create',blog.views.create, name = 'create'),
    path('blog/edit/<int:id>',blog.views.edit,name="edit"),
    path('blog/update/<int:id>',blog.views.update,name="update"),
    path('blog/delete/<int:id>',blog.views.delete, name = "delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)