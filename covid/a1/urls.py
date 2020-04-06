from django.conf.urls import url
from a1 import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^shopkeeper_sineup',views.shpkprSU,name='shpkprSU'),
]