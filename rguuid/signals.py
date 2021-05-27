from django.dispatch import Signal, receiver

from .models import RGUUID

generate_uuid = Signal()


@receiver(generate_uuid)
def generate_new_uuid(request, **kwargs):
    _ = RGUUID.objects.create()
    return None
