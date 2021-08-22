class Office:
    def __init__(self,name,age,varsity,year):
        self.name = name
        self.age = age
        self.varsity = varsity
        self.year = year

    def __str__(self):
       return self.name+"\n"+self.age+"\n"+self.varsity+"\n"+self.year


em = Office("Tahmid","23","Daffodil University","2021")
print(em)


