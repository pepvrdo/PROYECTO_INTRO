from django.db import models
from django.contrib.auth.models import User
from .api import url_to_qr

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    contacto = models.CharField(max_length=30)
    num_contacto = models.IntegerField()
    texto = models.TextField(max_length=1000)
    qr_code = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.qr_code:
            num= str(self.num_contacto)
            texto_qr = f"{self.name} {self.apellido}\n{self.contacto}: {num}\nMensaje de ayuda: {self.texto}"
            self.qr_code = url_to_qr(texto_qr)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'name: {self.name}'