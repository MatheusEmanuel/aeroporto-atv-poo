#Author: Matheus Emanuel Cincinato Pinto
#coding: utf-8

from random import randrange

class Passagem:
    def __init__(self):
        self._Origem = None
        self._Destino = None
        self._Preco = None
        self._Classe = None
        self._AplicarDesc = None
        self._Desconto = None
        self._Definir_Passagem()
    @classmethod
    def _Definir_Passagem(cls):
        print("\n" + "="*79 + "\n" +"="*30 + " DADOS DA PASSAGEM " + "="*30 + "\n"+ "="*79 + "\n")
        cls._Origem = str(input("\t\tInforme a origem do voo: "))
        cls._Destino = str(input("\t\tInforme o destino do voo: "))
        cls._Classe = str(input("\n\tDetermine um classe\n\t\t1-Economica\n\t\t2-Executiva\n\t\t3-Primeira Classe\n\tInforme a classe: "))
        while True:
            if (cls._Classe == '1' or cls._Classe == '2' or cls._Classe == '3'):
                break
            else:
                cls._Classe = str(input("\tClasse inexistente.\n\tInforme a classe: "))
        if (cls._Classe == '1'):
            cls._Preco = float(randrange(200,2000))
        elif (cls._Classe == '2'):
            cls._Preco = float(randrange(1000,2000))
        elif (cls._Classe == '3'):
            cls._Preco = float(randrange(2000,4000))
        else:
            cls._Classe = input("\tClasse inexistente\n\n\tEscolha a classe:\n\t\t1-Economica\n\t\t2-Executiva\n\t\t3-Primeira Classe\n\tInforme a classe: ")
        cls._AplicarDesc = str(input("\n\tDeseja aplicar desconto na passagem.\n\t\t1=Sim\n\t\t2=Não\n\tEscolha uma opção: "))
        while True:
            if (cls._AplicarDesc == '1'):
                cls._Desconto = float(input("\tInforme em % o desconto: "))
                cls._Preco = cls._Preco - (cls._Preco * cls._Desconto / 100)
                print("\tDesconto aplicado com sucesso.")
                break
            elif (cls._AplicarDesc == '2'):
                print("\tNão foi aplicado desconto.")
                break
            else:
                print("\tOpção inválida.")
                cls._AplicarDesc = str(input("\tEscolha uma opção: "))