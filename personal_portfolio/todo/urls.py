from django.urls import path
from . import views
from todo import views as todo_views
from skills import views as skills_views
from crafts import views as crafts_views


app_name = 'todo'

urlpatterns = [
    path('skills/', skills_views.index, name='skills_index'),
    path('crafts/', crafts_views.index, name='crafts_index'),
    # Auth
    # path("signup/", views.signupuser, name='signupuser'),
    # Auth
    path('signup/', todo_views.signupuser, name='signupuser'),
    path('logout/', todo_views.logoutuser, name='logoutuser'),
    path('login/', todo_views.loginuser, name='loginuser'),
# Todos
    path('home/', todo_views.home, name='home'),
    path('create', todo_views.createtodo, name='createtodo'),
    path('current/', todo_views.currenttodos, name='currenttodos'),
    path('todo/<int:todo_pk>', todo_views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', todo_views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', todo_views.deletetodo, name='deletetodo'),
    path('completed/', todo_views.completedtodo, name='completedtodo'),
    # Todos
    # path('current/', views.currenttodos, name='currenttodos'),
]