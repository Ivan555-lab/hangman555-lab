from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('user', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='post')

urlpatterns = router.urls