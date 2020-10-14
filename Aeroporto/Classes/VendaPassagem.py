#Author: Matheus Emanuel Cincinato Pinto
#coding: utf-8

from Passageiro import Passageiro
from Passagem import Passagem
from Companhia import Companhia_Aerea
from TipoVoo import VooTipo


class Venda_de_Passagem(Passageiro,Passagem,Companhia_Aerea,VooTipo):
    def __init__(self):
        self._Definir_Companhia()
        self._Vender_Passagem()
        self._DefinirTipoVoo()
        self._ImprimirPassagem()
    @classmethod
    def _Vender_Passagem(cls):
        cls._Add_Dados_Passageiro()
        cls._Definir_Passagem()
    @classmethod
    def _ImprimirPassagem(cls):
        if (cls._TipoVoo == '1'):
            print("\n" + "=" * 79 + "\n" + "=" * 34 + " PASSAGEM " + "=" * 35 + "\n" + "=" * 79 + "\n")
            print("\n\t\t{} AGRADECE A PREFERENCIA.\n"
                  "\n\t\tDados da Passageiro"
                  "\n\t\t\tNome: {}"
                  "\n\t\t\tCPF: {}"
                  "\n\t\t\tRG: {}"
                  "\n\t\tDADOS DA PASSAGEM"
                  "\n\t\t\tOrigem: {}"
                  "\n\t\t\tDestino: {}"
                  "\n\t\t\tData ida/volta: {} - {}"
                  "\n\t\t\tHorario partida ida/volta: {} - {}"
                  "\n\t\t\tPreço: {}".format(cls._Companhia,cls._Nome,cls._CPF,cls._RG,cls._Origem,cls._Destino,cls._Ida,cls._Volta,cls._HoraPart1,cls._HoraPart2,cls._Preco))
            print("\n" + "=" * 79 + "\n" + "=" * 79)
        elif (cls._TipoVoo == '2'):
            print("\n" + "=" * 79 + "\n" + "=" * 35 + " PASSAGEM " + "=" * 35 + "\n" + "=" * 79 + "\n")
            print("\n\t\t{} AGRADECE A PREFERENCIA.\n"
                  "\n\t\tDados da Passageiro"
                  "\n\t\t\tNome: {}"
                  "\n\t\t\tCPF: {}"
                  "\n\t\t\tRG: {}"
                  "\n\t\tDADOS DA PASSAGEM"
                  "\n\t\t\tOrigem: {}"
                  "\n\t\t\tDestino: {}"
                  "\n\t\t\tData ida: {}"
                  "\n\t\t\tHorario partida: {}"
                  "\n\t\t\tPreço: {}".format(cls._Companhia,cls._Nome,cls._CPF,cls._RG,cls._Origem,cls._Destino,cls._Ida,cls._HoraPart1,cls._Preco))
            print("\n" + "=" * 79 + "\n" + "=" * 79)