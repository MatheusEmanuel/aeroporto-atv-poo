#Author: Matheus Emanuel Cincinato Pinto
#coding: utf-8

import time

class Horarios:
    def __init__(self):
        self._HoraPart = None
        self._DefinirHorarios()
    @classmethod
    def _DefinirHorarios(cls):
        cls._HoraPart = input("\tHorario: ")
        while True:
            try:
                time.strptime(cls._HoraPart, "%H:%M")
                return cls._HoraPart
            except ValueError:
                print("\tA hora digitada é inválida o correto seria 'H:M' ")
                cls._HoraPart = input("\tInforme o horario: ")