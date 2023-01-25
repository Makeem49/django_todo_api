from rest_framework.routers import DefaultRouter

from todos.viewset import TodoViewSet, TodoGenericViewSet

router = DefaultRouter()
router.register('', TodoGenericViewSet, basename='products')
urlpatterns = router.urls