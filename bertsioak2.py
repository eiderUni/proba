'''
Created on 27 feb. 2018

@author: AdminPremiaLocal
'''

if __name__ == '__main__':
    pass

print('bertsioak2')
print('bertsioak2')

class Lasterketa:
    def __init__(self,data,izena,herria,hasiera_tokia,helmuga_tokia,distantzia,desnibel_positiboa,desnibel_negatiboa):
        self.data = data
        self.izena = izena
        self.herria = herria
        self.hasiera_tokia = hasiera_tokia
        self.helmuga_tokia = helmuga_tokia
        self.distantzia = distantzia
        self.desnibel_positiboa = desnibel_positiboa
        self.desnibel_negatiboa = desnibel_negatiboa
    def Bistaratu(self):
        print(self.izena)

lasterketa1 = Lasterketa('21/02/2018', 'Kalamendi', 'Ondarroa', 'Itsasaurre', 'Kalamendi punta', 10.6, 1200, 600)
lasterketa1.Bistaratu()