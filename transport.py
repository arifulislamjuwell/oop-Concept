class Transport:
    __transportId=''
    __transportname=''
    __AcORNonAc=''

    def Transpor(self):
        return None

    def __init__(self,transportId,transportname,AcORNonAc):
        self.__transportId = transportId
        self.__transportname = transportname
        self.__AcORNonAc = AcORNonAc

    def getTransportId(self):
        return self.__transportId

    def getTransportname(self):
        return self.__transportname

    def getAcORNonAc(self):
        return self.__AcORNonAc

    def display(self):
        print("Transport Information :")
        print("-------------------------------")
        print("Transport Id :"+str(self.__transportId))
        print("Transport Name :"+str(self.__transportname))
        print("Ac/Non AC :"+self.__AcORNonAc)
