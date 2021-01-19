class Diff:

    def __init__(self, ratio = 1):
        if not isinstance(ratio, (int,float)):
            raise ExamException('La ratio non è un istanza')
        self.ratio = ratio

    def compute (self, dati):
        if type(dati) is not list:
            raise ExamException('la lista di numeri non è una lista')

        for i in dati:
            if type (i) is not int:
                raise ExamException('uno dei caratteri inseriti non è un numero')

        if self.ratio==0:
            raise ExamException('ratio è uguale a zero')

        arr = []
        for i in range(1, len(dati)):
            diff = dati[i]-dati[i-1]
            
            diff /= self.ratio
            arr.append(diff)

        return arr 

class ExamException(Exception):
    pass 

diff = Diff()
result = diff.compute([2,4,8,16])
print (result)
