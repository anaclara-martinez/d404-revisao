from django.db import models

# Create your models here.


class Filme(models.Model):
    genero_acao = 'ac'
    genero_aventura = 'av'
    genero_comedia = 'cm'
    genero_drama = 'dr'
    genero_ficcao = 'fc'
    genero_romance = 'rm'
    genero_terror = 'tr'
    genero_opcoes = [
        (genero_acao, 'Ação'),
        (genero_aventura, 'Aventura'),
        (genero_comedia, 'Comédia'),
        (genero_drama, 'Drama'),
        (genero_ficcao, 'Ficção'),
        (genero_romance, 'Romance'),
        (genero_terror, 'Terror'),
    ]
    nome =  models.CharField(max_length=120)
    genero = models.CharField(max_length=2, choices=genero_opcoes, default=None)
    sinopse = models.TextField()
    lancamento = models.DateField()
    duracao = models.PositiveIntegerField()
    classificacao_indicativa = models.PositiveIntegerField()
    cartaz = models.ImageField(upload_to='media')

    def __str__(self):
        return self.nome