from rest_framework.routers import DefaultRouter

from currency.api.views import RateViewSet

# from currency.api.views import RateApiView, RateDetailApiView

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')

urlpatterns = [
    # path('rates/', RateApiView.as_view(), name='rates-list'),
    # path('rates/<int:pk>/', RateDetailApiView.as_view(), name='rates-details')
]

urlpatterns += router.urls
