class mama:
    def __init__(self,sex):
        self.sex=sex


class objects(mama):
    def __init__(self,a,b,sex):
        self.name=a
        self.age=b
        super().__init__(sex)
    def testes(self):
        print(f'{self.name},{self.sex}')

b=objects(1,2,80)
c=b.testes()
print(b)
