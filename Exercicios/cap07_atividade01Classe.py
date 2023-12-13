"""
  Cap07 - Atividade 01
  Criar um Classe 

  Objetivos:
  Nesta atividade você vai criar uma objeto de classe, aprendendo sobre os metodos e propriedades e usar metodos especiais. Irá também aprender a consumir esta classe.

  Comandos utilizados:
  Classe, __init__, __str__, Propriedades e Metodos de uma classe
"""
from num2words import num2words
class recibo:
  
  def __init__(self, nome):
    self.nome = nome
    self._valor = 0
    self._descricao = ''

  def __str__(self):
    texto = 'Recebemos de {} a quantia de R$ {:.2f} ({}))' . format(self.nome, self._valor, self.extenso())
    descricao = '\nReferente {}' . format(self._descricao) if (self._descricao!='') else ''
    dados = '{}\n{}{}' . format('Recibo'.center(len(texto), '*'), texto, descricao)
    return(dados)

  def descricao(self, value):
    self._descricao = value

  @property
  def valor(self):
    return(self._valor)
    
  @valor.setter
  def valor(self, value):
    self._valor = value

  def extenso(self ):
    vExtenso = num2words(self._valor,lang='pt_BR', to='currency')
    return vExtenso


