#Author: Matheus Emanuel Cincinato Pinto
#coding: utf-8

class Companhia_Aerea:
    def __init__(self):
        self._Companhia = None
    @classmethod
    def _Definir_Companhia(cls):
        cls._Companhia = str(input("Nome da companhia: "))