from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from currency.api.v1.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.filters import RateFilter, SourceFilter, ContactUsFilter
from currency.models import Rate, Source, ContactUs
from currency.paginators import RatesPagination

from currency.throttlers import AnonCurrencyThrottle

from currency.choices import RateCurrencyChoices

from currency import constants


# class RateApiView(generics.ListCreateAPIView):
#     queryset = Rate.objects.all().select_related('source')
#     serializer_class = RateSerializer  # json.dumps, json.loads
#
#
# class RateDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    # renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = RatesPagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = RateFilter
    ordering_fields = ('id', 'created', 'buy', 'sale')
    # throttle_classes = (AnonCurrencyThrottle,)

    @action(detail=True, methods=('POST',))
    def buy(self, request, *args, **kwargs):
        rate = self.get_object()
        # print(rate)  # send buy request
        sz = self.get_serializer(instance=rate)
        return Response(sz.data)

    @action(detail=False, methods=('GET',))
    def latest(self, request, *args, **kwargs):
        latest_rates = []

        cached_rates = cache.get(constants.LATEST_RATE_CACHE)
        if cached_rates:
            return Response(cached_rates)

        for source_obj in Source.objects.all():
            for currency in RateCurrencyChoices:
                latest = Rate.objects.filter(
                    source=source_obj,
                    currency=currency) \
                    .order_by('-created') \
                    .first()

                if latest:
                    latest_rates.append(RateSerializer(instance=latest).data)

        cache.set(constants.LATEST_RATE_CACHE, latest_rates, 60 * 60 * 24 * 7)

        return Response(latest_rates)


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = SourceFilter


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    search_fields = ['name', 'subject', 'message']
    filterset_class = ContactUsFilter
    ordering_fields = ('id', 'created', 'email_from',)
