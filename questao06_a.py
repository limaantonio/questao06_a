#Classe Pessoa
class Pessoa:
    def __init__(self, matricula, nome, nota):
        self.matricula = matricula
        self.nome = nome
        self.nota = nota

    def imprime(self):
        print("Maticula: %d, Nome: %s, Nota: %f\n"%(self.matricula,self.nome,self.nota))
    

#Função de ordenação
def ordena(Array, n, o):
    aux = 0
    i = 0
    j = 0
    
    if o == 1:
        for i in range(n-1):
            for j in range(n-i-1):
                if(Array[j].matricula > Array[j+1].matricula):
                    aux = Array[j]
                    Array[j] = Array[j+1]
                    Array[j+1] = aux

    if o == 2:
        for i in range(n-1):
            for j in range(n-i-1):
                if(Array[j].nome > Array[j+1].nome):
                    aux = Array[j]
                    Array[j] = Array[j+1]
                    Array[j+1] = aux
       
    if o == 3:
        for i in range(n-1):
            for j in range(n-i-1):
                if(Array[j].nota > Array[j+1].nota):
                    aux = Array[j]
                    Array[j] = Array[j+1]
                    Array[j+1] = aux

#Main

Array = []
i = 0
n = int(input("Digite o tamanho para o vetor.\n"))

while i < n:
    mat = int(input("Matricula: \n"))
    name = input("Nome: \n")
    nota = float(input("Nota: \n"))

    p = Pessoa(mat, name, nota)
    Array.append(p)
    i += 1
    
o = int(input("Escolha uma forma de ordenação:\n [1]: Ordenar por Matricula\n [2]: Ordenar por Nome\n [3]: Ordenar por Nota\n"))

ordena(Array, n, o)

print("Vetor de Pessoas ordenado:\n")
for i in range(n):
    Array[i].imprime()