from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from .views import Author_List

urlpatterns = [
    path('chat/', include('chat.urls')),
    #path('', include('chat.urls')),
    path('api/', include('meapi.urls')),
    path('admin/', admin.site.urls),
    path('', views.start, name='start'),
    path('room_select/', views.room_select, name='room_select'),

    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    #path('mailing/<str:room_name>/<str:user_email>/', Author_List.as_view(), name='mailing'), # ссылка на рассылку приглашений
    #path('mailing/<str:room_name>/', views.room, name='mailing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)