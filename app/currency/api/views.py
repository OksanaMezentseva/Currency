from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from currency.api.serializers import RateSerializer
from currency.models import Rate


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
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)

    @action(detail=True, methods=('POST',))
    def buy(self, request, *args, **kwargs):
        rate = self.get_object()
        # print(rate)  # send buy request
        sz = self.get_serializer(instance=rate)
        return Response(sz.data)
