from django.conf.urls import url
from a1 import views
urlpatterns=[
    url(r'^$',views.index,name='Home'),
    url(r'^shopkeeper_signup/',views.shpkprSU,name='Signup'),
    url(r'^shopkeeper_login/',views.shpkprLG,name='Login'),
]