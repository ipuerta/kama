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
    path('alta_pais', views.alta_pais, name='alta_pais'),
#    path('premios/', views.premios, name='premios'),
#    path('wiki/', views.wiki, name='wiki'),
#    path('videos/', views.videos, name='videos'),
#    path('videos/nuevo-girl-group/', views.alta_girl_group, name='alta_girl_group'),
#    path('videos/nuevo-banda/', views.alta_banda, name='alta_banda'),
#    path('videos/nuevo-artista/', views.alta_artista, name='alta_artista'),
#    path('ajax/crear-pais/', views.ajax_crear_pais, name='ajax_crear_pais'),
#    path('ajax/cargar-ciudades/', views.ajax_cargar_ciudades, name='ajax_cargar_ciudades'),
#    path('ajax/crear-ciudad/', views.ajax_crear_ciudad, name='ajax_crear_ciudad'),
#    path('ajax/crear-compañia/', views.ajax_crear_compañia, name='ajax_crear_compañia'),
#    path('grupo/<int:id_grupo>/', views.detalle_grupo, name='detalle_grupo'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)