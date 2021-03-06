from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^gridlayout/', include('appgridlayout.urls', namespace='appgridlayout')),
    
    url(r'^buttons/', include('buttons.urls', namespace='buttons')),

    url(r'^menu/', include('menu.urls', namespace='menu')),
]
