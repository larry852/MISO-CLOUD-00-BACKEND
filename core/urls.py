from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_auth.views import LoginView

from events.urls import router as events_router

router = routers.DefaultRouter()
router.registry.extend(events_router.registry)

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/create-user/', include('rest_auth.registration.urls')),
    path('api/api-auth/', LoginView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
