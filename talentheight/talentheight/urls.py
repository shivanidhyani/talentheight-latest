from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s3direct/', include('s3direct.urls')),
    path('', include('web.urls'), name='index'),
    #added by jiya
    path('oauth/', include('social_django.urls', namespace='social')), 

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)