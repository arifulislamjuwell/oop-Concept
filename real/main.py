from abc import ABC, ABCMeta, abstractmethod


class User:
    allowed_sex = ['male', 'female']
    versity= 'Daffodil International University'

    def __init__(self, first_name,last_name, age, address):
        self.first= first_name
        self.last= last_name
        self.__age= age
        self.__address= address

    @classmethod
    def allowed_sex(cls, para):
        print('class method')
        for i in cls.versity:
            print( str(para+i))


    @staticmethod
    def age_after_4_years(age):
        print('static method')
        return age+4

    @property
    def age(self):
        return int(self.__age)
    
    @age.setter
    def age(self, age):
        self.__age=age
    
    def get_full_name(self):
        return self.first +' '+ self.last

    def get_descripttion(self):
        return 'my name is {}, my age {}, address is {}'.format(self.get_full_name(), self.age, self.__address)


class Student(User):
    def __init__(self, first_name, last_name, age, address, student_id, credit):
        super().__init__(first_name, last_name, age, address)
        self.credit= credit
        self.id= student_id
    
    def get_descripttion(self):
        print('{} my id is{}, my credis is {}'.format(super().get_descripttion(), self.id, self.credit))


class Cgpa(Student):
    def __init__(self, first_name, last_name, age, address, student_id, credit):
        super().__init__(first_name, last_name, age, address, student_id, credit)



a= User('ariful', 'juwel', 45,'narail')


# a.allowed_sex('sex :')
# User.allowed_sex('sex is: ')
# User.age_after_4_years(4)
# a.age_after_4_years(8)
# a.get_descripttion()

b= Student('ariful', 'juwel', 45,'narail',1285, 65)
b.get_descripttion()
c= Cgpa('ariful', 'juwel', 45,'narail',1285, 65)