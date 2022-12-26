class Eva:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return '- ' + self.name
eva_1=Eva('Mazda')
eva_2=Eva('Honda')
eva_3=Eva('Lada')
dict_1={'Ирма':eva_1,'Тарани':eva_2,'Корнелия':eva_3}
for n in dict_1:
    print(n,dict_1[n])
