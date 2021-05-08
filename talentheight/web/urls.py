from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    #Viewer Url
    path('', views.index, name='index' ),
    path('explore', views.explore, name='explore' ),
    path('trending', views.trending, name='trending' ),
    path('popular', views.popular, name='popular' ),
    path('history', views.history, name='history' ),
    path('subscriptions', views.subscriptions, name='subscriptions' ),    
    path('open-video/<pid>', views.openvideo, name='openvideo'),
    path('mychannel', views.mychannel, name='mychannel'),
    path('myvideos', views.myvideos, name='myvideos'),
    path('aboutuser', views.aboutuser, name='aboutuser'),
    path('editprofile', views.editprofile, name='editprofile'),  
    path('userplaylist/', views.userplaylist, name='userplaylist'),
    path('wallet/', views.wallet, name='wallet'),


    path('register-into-talentheight', views.signup, name='signup'),
    path('login-into-talentheight', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_chang.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


    #Creator Url
    path('dashboard/', views.dashboard, name='dashboard'),
    path('uploadvideo/', views.uploadvideo, name='uploadvideo'),
    path('channels/', views.channels, name='channels'),
    path('playlist/', views.playlist, name='playlist'),
    path('profile/edit/', views.profileedit, name='profile-edit'),
    path('profile/edit/bank-details', views.bankaccount, name='bankaccount'),
    
    
    path('myVideos/', views.myvideos, name='myvideos'),
    path('account/setting/', views.myvideos, name='account-settings'),
    path('starratings/', views.starrating, name='star'),
    
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)