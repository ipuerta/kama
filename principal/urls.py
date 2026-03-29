from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('login/', auth_views.LoginView.as_view(template_name='principal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='principal/password_change.html',
        success_url='/password_change/done/'
    ), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='principal/password_change_done.html'
    ), name='password_change_done'),

    path('grupos/', views.grupos, name='grupos'),
    path('alta_grupo/', views.alta_grupo, name='alta_grupo'),
    path('grupos/<int:id>', views.info_grupo, name='info_grupo'),
    
    path('artistas/', views.artistas, name='artistas'),
    path('alta_artista/', views.alta_artista, name='alta_artista'),
    path('artistas/<int:id>', views.info_artista, name='info_artista'),
    
    path('paises/<int:id>', views.info_pais, name='info_pais'),
    path('alta_pais/', views.alta_pais, name='alta_pais'),
    path('alta_comp/', views.alta_compañia, name='alta_comp'),
    path('comps/', views.compañias, name='comps'),
    path('info_comp/<int:id>', views.info_compañia, name='info_comp'),
    path('alta_video/', views.alta_video, name='alta_video'),
    path('info_video/<int:id>', views.info_video, name='info_video'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)