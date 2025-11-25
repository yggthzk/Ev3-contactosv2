from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactoViewSet, RegisterView

router = DefaultRouter()#la default 8000
router.register(r'contactos', ContactoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
]