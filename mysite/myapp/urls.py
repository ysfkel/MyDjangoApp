from django.conf.urls import patterns,include, url	
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

# urlpatterns=[
# 	
# 	url(r'^$',views.index,name='index'),
# 	
# 	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
# 	
# 	url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
# 	
# 	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
# 	url(r'^api/$',views.QuestionList.as_view()),
#     url(r'^api/(?P<pk>[0-9]+)/$',views.QuestionDetail.as_view())
# ]

urlpatterns=patterns('',
	
	url(r'^$',views.index,name='index'),
	
	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	
	url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
	
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
	url(r'^api/$',views.QuestionList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$',views.QuestionDetail.as_view()),
	
	url(r'^api/item/$',views.ItemList.as_view()),
    #url(r'^api/item/(?P<pk>\d+)/$', ItemDetail.as_view(), name='itemDetail'),
	
)
# 
# urlpatterns = patterns('',
#     url(r'^$', Index.as_view(), name='index'),
#     url(r'^api/item/$', ItemList.as_view(), name='item-list'),
#     url(r'^api/item/(?P<pk>\d+)/$', ItemDetail.as_view(), name='item-detail'),
# )


urlpatterns=format_suffix_patterns(urlpatterns)
