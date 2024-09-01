from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, LoginView, LogoutViewSet, RoleViewSet

router = DefaultRouter()
router.register(r'users', RegisterViewSet),
router.register(r'roles', RoleViewSet),
router.register(r'logout', LogoutViewSet, basename='logout')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
