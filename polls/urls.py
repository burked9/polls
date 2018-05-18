from django.conf.urls import include, url
from django.contrib import admin
from polls import views

##app_name = "polls"

urlpatterns = [
        # ex: /polls/
        url(r'^$', views.index, name='index'),
        # ex: /polls/5/
        url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
        # ex: /polls/5/results
        url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
        # ex: /polls/5/vote
        url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
       ## url(r'^polls/', include('polls.urls')),
       ## url(r'^admin/', admin.site.urls),
]

'''
url(r'^about/', views.about, name='about'),
url(r'^category/(?P<category_name_slug>[\w-]+)/$', views.category, name='category'),
'''