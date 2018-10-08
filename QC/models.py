from django.db import models
import magic
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Material(models.Model):
    material_text = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default="in process")

    def __str__(self):
        return self.material_text


class Media(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mime_type = models.CharField(max_length=32)
    file = models.FileField(upload_to='')

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Media)
def update(sender, instance, **kwargs):
    f = instance.file.open()
    instance.mime_type = magic.from_buffer(f.read(), mime=True)
