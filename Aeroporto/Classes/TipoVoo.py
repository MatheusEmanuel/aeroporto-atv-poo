#Author: Matheus Emanuel Cincinato Pinto
#coding: utf-8

from Data_Valida import Data
from Horario import Horarios

class VooTipo(Horarios,Data):
    def __init__(self):
        self._Ida = None
        self._FatIda = None
        self._HoraPart1 = None
        self._cls._FatHora1 = None
        self._Volta = None
        self._FatVolta = None
        self._HoraPart2 = None
        self._cls._FatHora2 = None
        self._TipoVoo = None
    @classmethod
    def _DefinirTipoVoo(cls):
        cls._TipoVoo = str(input("\n\tTipo de voo.\n\t\t1 = Ida e Volta\n\t\t2 = Só ida\n\tEscolha uma das opções: "))
        while True:
            if (cls._TipoVoo == '1' or cls._TipoVoo == '2'):
                break
            else:
                cls._TipoVoo = str(input("\tTipo de voo inexistente.\n\tEscolha uma das opções: "))
        if (cls._TipoVoo == '1'):
            print("\n\tInforme a data de ida.")
            cls._Ida = Data._Data_Valida()
            cls._FatIda = cls._Ida.split('/')
            cls._HoraPart1 = Horarios._DefinirHorarios()
            cls._FatHora1 = cls._HoraPart1.split(':')
            print("\n\tInforme a data de volta.")
            cls._Volta = Data._Data_Valida()
            while True:
                cls._FatVolta = cls._Volta.split('/')
                if int(cls._FatIda[0]) > int(cls._FatVolta[0]):
                    print("\tDia inválida!")
                    cls._Volta = Data._Data_Valida()
                elif int(cls._FatIda[1]) > int(cls._FatVolta[1]):
                    print("\tMes inválido!")
                    cls._Volta = Data._Data_Valida()
                elif int(cls._FatIda[2]) > int(cls._FatVolta[2]):
                    print("\tAno inválido")
                    cls._Volta = Data._Data_Valida()
                else:
                    break
            cls._HoraPart2 = Horarios._DefinirHorarios()
            if cls._Ida == cls._Volta:
                while True:
                    cls._FatHora2 = cls._HoraPart2.split(':')
                    if int(cls._FatHora1[0]) >= int(cls._FatHora2[0]) and int(cls._FatHora1[1]) >= int(
                        cls._FatHora2[1]):
                        print("\tHora de volta inválida.")
                        cls._HoraPart2 = Horarios._DefinirHorarios()
                    else:
                        break
        elif (cls._TipoVoo == '2'):
            print("\n\tInforme a data de ida.")
            cls._Ida = Data._Data_Valida()
            cls._HoraPart1 = Horarios._DefinirHorarios()