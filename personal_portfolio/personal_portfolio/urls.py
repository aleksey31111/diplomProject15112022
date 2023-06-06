"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from skills import views as skills_views
from crafts import views as crafts_views
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', skills_views.index, name='skills_index'),
    path('blog/', include('blog.urls')),
    path('crafts/', crafts_views.index, name='crafts_index'),
    path('crafts/create/', crafts_views.create, name='create_craft'),
    # Auth
    path('signup/', todo_views.signupuser, name='signupuser'),
    path('logout/', todo_views.logoutuser, name='logoutuser'),
    path('login/', todo_views.loginuser, name='loginuser'),
    # Todos

    # path('home/', todo_views.home, name='home'),
    # path('create', todo_views.createtodo, name='createtodo'),
    # path('current/', todo_views.currenttodos, name='currenttodos'),
    # Авторизация, Аутентификация, Задачи Приложения todo
    path('todo/', include('todo.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
