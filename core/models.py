from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(verbose_name='Data do Evento')
    criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'
    
    def __str__(self):
        return self.titulo

    def data_ajustada (self):
        return self.data.strftime('%d/%m/%Y %H:%M hrs')
    
    def get_data_input(self):
        return self.data.strftime('%Y-%m-%dT%H:%M')
    
    def get_evento_atrasado(self):
        if self.data < datetime.now():
            return True
        else:
            return False