from django.db import models

class Enquete(object):
    
    def __init__(self, texto, data_publicacao):
        self.texto = texto
        self.data_publicacao = data_publicacao