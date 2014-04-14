from django.conf.urls import patterns, url

from Library import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'Library/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'Library/index.html'}, name='logout'),
    url(r'^book/all/', views.SystemBookView.as_view(), name='detail_system'),
    url(r'^library/(?P<pk>\d+)/$', views.LibraryBookView.as_view(), name='detail_library'),
    url(r'^book/(?P<pk>\d+)/$', views.BookView.as_view(), name='detail_book'),
    url(r'^book/(?P<book_id>\d+)/checkout/$', views.checkout_or_return, name='checkout_or_return')
)
