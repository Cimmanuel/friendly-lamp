from django.utils import timezone
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import RGUUID
from .signals import generate_uuid


class RGUUIDView(APIView):
    def get(self, request, *args, **kwargs):
        generate_uuid.send(sender=self.__class__, request=self.request)

        results = {}
        instances = RGUUID.objects.all().order_by("-created")
        for instance in instances:
            results.update(
                {
                    timezone.localtime(instance.created).strftime(
                        "%Y-%m-%d %H:%M:%S.%f"
                    ): instance.id.hex,
                }
            )

        return Response(results, status=HTTP_200_OK)
