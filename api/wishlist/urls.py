from django.urls import path, include
from .views import WishlistViewSet, wishlist_page, add_to_wishlist, remove_from_wishlist
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wishlist', WishlistViewSet)

urlpatterns = [
    path('', include(router.urls)),  # API-ендпоінти
    path('page/', wishlist_page, name='wishlist-page'),  # HTML-сторінка
    path('add/<int:product_id>/', add_to_wishlist, name='wishlist-add'),  # Додавання в список бажань
    path('remove/<int:item_id>/', remove_from_wishlist, name='wishlist-remove'),  # Видалення зі списку бажань
]