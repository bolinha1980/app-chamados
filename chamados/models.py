from django.db import models

class Chamados(models.Model):
    solicitado_cham = models.CharField(max_length=150, blank=False)
    data_cham = models.DateTimeField()
    solicitante_cham = models.CharField(max_length=30, blank=False)
    msg_cham = models.CharField(max_length = 400, blank=False)
    status_cham = models.SmallIntegerField(blank=False)

    def __str__(self):
        return self.name                                       

