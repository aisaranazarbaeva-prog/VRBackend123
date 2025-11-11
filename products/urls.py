from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, BrandViewSet, CategoryViewSet

router = DefaultRouter()
router.register('brands', BrandViewSet)
router.register('categories', CategoryViewSet)
router.register('items', ProductViewSet)

urlpatterns = router.urls
