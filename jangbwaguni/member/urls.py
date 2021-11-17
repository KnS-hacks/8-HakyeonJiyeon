from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

# app_name = 'member'
urlpatterns = [
    path('', views.d_mypage, name='d_mypage'),
    path('list/', views.d_mypage_orderlist, name='d_mypage_orderlist'),
    
    path('index/', views.IndexView.as_view(), name='index'),
    path('login', views.login, name="login"),
]
# from django.urls.resolvers import URLPattern



# urlpatterns = [
#     path('signup', views.signup, name='signup'),
#     # path('login', views.Login, name = 'login'),
# ]
