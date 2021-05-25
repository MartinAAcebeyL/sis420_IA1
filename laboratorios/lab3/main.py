import numpy as np 
import random

class DNA(): 
    def __init__(self, target, mutation_rate, n_individuals, n_selection, n_generations, verbose = True):
        self.target = target 
        self.mutation_rate = mutation_rate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generations = n_generations
        self.verbose = verbose
        self.tamano = len(self.target[0])
        #print(self.tamano)

    def create_indivual(self, mini = 0, maxi = 2):
        #Crea un individuo
        individuo = []
        for k in range(len(self.target)):              
            list_aux = []
            for j in range(self.tamano):
                list_aux.append(np.random.randint(mini, maxi))
            individuo.append(list_aux)
        return individuo

    def create_population(self):
        poblacion = []
        for i in range(self.n_individuals):
            poblacion.append(self.create_indivual())
        return poblacion

    def fitness(self, individual):
        fit = 0
        for i in range(len(individual)):
            target, individuo = self.target[i], individual[i]
            #print('\ni: {} target {} individuo {}'.format(i, target, individuo),end=' ')
            for j in range(len(target)):
                #print('j: {} obj: {} ind: {}'.format(j, target[j], individuo[j]))
                if target[j] == individuo[j]:
                    fit += 1
            #print(fit)
        return fit
 
    def selection(self, poblacion):
        scores = []
        for i in poblacion:
            #print('i',i)
            scores.append([self.fitness(i), i])
        
        score = [i[1] for i in sorted(scores)]
        #print('score', score)
        selected = score[len(score)-self.n_selection:]
        return selected

    def reproducion(self,poblacion,selection):
        #point = 0
        father = []
        for i in range(len(poblacion)):
            father = random.sample(selection,2)
            cromosoma1 = father[0]
            cromosoma2 = father[1]
            l1 = len(cromosoma1)
            l2 = len(cromosoma2)

            poblacion[i][0:l1 // 2] = father[0][l1 // 2:l2]
            poblacion[i][0:l2 // 2] = father[1][l2 // 2:l1]

        """for i in range(len(poblacion)):
            point = np.random.randint(1, len(self.target) -1)
            father = random.sample(selection,2)
            print('point father',point,father)
            poblacion[i][:point] = father[0][:point]
            poblacion[i][point:] = father[1][point:]"""
        return poblacion

    def mutacion(self, poblacion):
        for i in range(len(poblacion)):
            if random.random() < self.mutation_rate:
                #punto a modificar
                point = random.randint(0, len(self.target)-1)
                #valor  a modificar
                new_value = []
                for i in range(self.tamano):
                    new_value.append(np.random.randint(0,2))
                """while new_value == poblacion[i][point]:
                    new_value = np.random.randint(0,2)"""
                poblacion[i][point] = new_value

        
        return poblacion

    def run_generation(self,v=0):
        poblacion = self.create_population() if v==0 else v
        
        #while self.target not in poblacion:
        for i in range(self.n_generations):
            if self.verbose:
                print('---------')
                print('generacion: '+str(i+1))
                print('poblacion: ')
                mostrar(poblacion)
            selected = self.selection(poblacion)
            poblacion=self.reproducion(poblacion, selected)
            poblacion=self.mutacion(poblacion)
            if self.target in poblacion:
                break       
        return poblacion


def dec_to_bin(x):
    return int(bin(x)[2:])

def dec_ascci_bin_str():
    valor = input('de su password menor a 4 letras: ')
    password = list(valor)

    while len(password)!=4:
        main()
    
    password_ascii = []
    for i in password:
        password_ascii.append(ord(i))
    
    password_bin = []
    for i in password_ascii:
        password_bin.append(dec_to_bin(i))
    #aumentar los 0 que faltan
    BIT = 8
    password_bin_str = []
    for i in password_bin:
        x = len(str(i))
        if x < 8:
            add_ceros = BIT - x
            cero = '0'*add_ceros
            password_bin_str.append(cero+str(i))
    x = []
    for i in password_bin_str:
        number_list = []
        for y in i:
            number_list.append(int(y))
        x.append(number_list)
    return x

def mostrar(a):
    n = 1
    for i in a:
        print('{} {}'.format(n,i))
        n+=1

def main():
    valor = dec_ascci_bin_str()
    target = valor
    model = DNA(target, 0.02, 10, 5,200, True)
    model.run_generation()

    print('objetivo: ')
    print(target)
    
if __name__ == '__main__':
    
    main()