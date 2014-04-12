from django.conf.urls import patterns, url

from Library import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^library/books/', views.SystemBookView.as_view(), name='detail_system'),
    url(r'^library/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^book/(?P<book_id>\d+)/checkout/$', views.checkout, name='checkout')
)
