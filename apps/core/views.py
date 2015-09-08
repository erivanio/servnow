from rest_framework.generics import ListAPIView
from apps.core.models import Client
from apps.core.serializer import ClientSerializer


class ApiClientView(ListAPIView):
    model = Client
    serializer_class = ClientSerializer
    queryset = Client.objects.filter(status=True)
    paginate_by = 10

