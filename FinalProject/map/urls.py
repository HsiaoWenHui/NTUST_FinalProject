from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.photo_list, name='photo_list'),
    url(r'^record/$', views.record, name='record'),
    url(r'^diary/$',views.diary, name='diary'),
    url(r'^Diary_Page/$',views.Diary_Page, name='Diary_Page'),
]
