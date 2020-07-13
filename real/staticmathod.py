class Table:

    @staticmethod
    def hoght_maker():
         return 'hight is 90'

    def color(self):
        a= self.hoght_maker()
        return a

a= Table()
print(a.color())
