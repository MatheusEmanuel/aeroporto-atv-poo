#Author: Matheus Emanuel Cincinato Pinto
#coding: utf-8

from Pessoa import Pessoa
from pycpfcnpj import cpfcnpj

class Passageiro(Pessoa):
    def __init__(self):
        self._Add_Dados_Passageiro()
    @classmethod
    def _Add_Dados_Passageiro(cls):
        print("="*79 + "\n" +"="*29 + " DADOS DO PASSAGEIRO " + "="*29 + "\n"+ "="*79 )
        cls._Nome = str(input("\n\t\tInforme o nome do passageiro: "))
        cls._CPF = str(input("\t\tInsira o CPF: "))
        while ((cpfcnpj.validate(cls._CPF) == False) or (cpfcnpj.validate(cls._CPF) == False)):
            print("\t\tCPF: INVÁLIDO!")
            cls._CPF = str(input("\t\tInsira o CPF: "))
        cls._RG = str(input("\t\tInsira o RG: "))