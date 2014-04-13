from django.conf.urls import patterns, url

from Library import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^book/all/', views.SystemBookView.as_view(), name='detail_system'),
    url(r'^library/(?P<pk>\d+)/$', views.LibraryBookView.as_view(), name='detail_library'),
    url(r'^book/(?P<pk>\d+)/$', views.BookView.as_view(), name='detail_book'),
    url(r'^book/(?P<book_id>\d+)/checkout/$', views.checkout, name='checkout')
)
