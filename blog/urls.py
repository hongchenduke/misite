# urls.py
from . import views
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [

    # DRF函数视图--url
    # re_path(r'^articles/$', views.article_list),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),

    # DRF APIView视图和通用视图(generic)--url
    # re_path(r'^articles/$', views.ArticleList.as_view()),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


#DRF使用视图集--url配置需要使用routers
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', viewset=views.ArticleViewSet)
urlpatterns = []
urlpatterns += router.urls
