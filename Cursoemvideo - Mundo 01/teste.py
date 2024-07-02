# imports
from abc import ABC, abstractmethod

#abstract class Imposto
class Imposto (ABC):
  @abstractmethod
  def calcula(orcamento): pass

#concrete classes that implements interface Imposto
class ICMS(Imposto):
  def calcula(orcamento):
    return orcamento.valor * 0.18

class ISS(Imposto):
  def calcula(orcamento):
    return orcamento.valor * 0.05

class PIS(Imposto):
  def calcula(orcamento):
    return orcamento.valor * 0.01

class COFINS(Imposto):
  def calcula(orcamento):
    return orcamento.valor * 0.03

#Calculador de Impostos
class CalculadorDeImpostos:
  def calcula(orcamento, imposto):
    return imposto.calcula(orcamento)

#orçamento
class Orçamento:
  def __init__(valor):
    self.valor = valor

#execuçao
items = dict()
while True:
  item = items

#
icms = ICMS()
iss = ISS()
pis = PIS()
cofins = COFINS()