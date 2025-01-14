from django.urls import path, include
from .views import WishlistViewSet, wishlist_page
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wishlist', WishlistViewSet)

urlpatterns = [
    path('', include(router.urls)),  # API-ендпоінти
    path('page/', wishlist_page, name='wishlist-page'),  # HTML-сторінка
]
