from ..veritabani.models import SopaDeneme

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=SopaDeneme)
def do_smt(sender, **kwargs):
    print("dış hellooo")