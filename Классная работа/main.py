class A:
    def __init__(self,name):
        self.name = name
        self.age = 15
        #print('создаём нового ученика')

    #def hello(self,a):
        #print(a)
Yara = A('Yara')
Uri = A('U')
Uri.age = 29
Uri.massa = 96
print(Uri.name,Uri.age,Uri.massa)
print(Yara.name,Yara.age,Yara.massa)