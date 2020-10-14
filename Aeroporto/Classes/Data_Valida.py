#Author: Matheus Emanuel Cincinato Pinto
#coding: utf-8

class Data:
    def __init__(self):
        self._Data = None
        self._Data_Valida()
    @classmethod
    def _Data_Valida(cls):
        cls._Data = input("\tData: ")
        if len(cls._Data) == 10:
            if cls._Data[2] == '/' and cls._Data[5] == '/':
                fatdata = cls._Data.split('/')
                if (int(fatdata[0]) <= 31 and int(fatdata[0]) >= 1):
                    if (int(fatdata[1]) <= 12 and int(fatdata[1]) >= 1):
                        if (len(fatdata[2]) == 4 and int(fatdata[2]) != 0000):
                            return cls._Data
                        else:
                            print("\tAno inválido.")
                            return cls._Data_Valida()
                    else:
                        print("\tMês inválido.")
                        return cls._Data_Valida()
                else:
                    print("\tDia inválido.")
                    return cls._Data_Valida()
            else:
                print("\tData de formato inválido. Correto = dd/mm/aaaa ")
                return cls._Data_Valida()
        else:
            print("\tData inserida é inválida. Correto = dd/mm/aaaa")
            return cls._Data_Valida()
