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

    def create_indivual(self, mini = 0, maxi = 2):
        #Crea un individuo
        individual = [np.random.randint(mini, maxi) for i in range(len(self.target))]
        return individual

    def create_population(self):
        #Crea una poblacion
        population = [self.create_indivual() for i in range(self.n_individuals)]
        return population

    def fitness(self, individual):
        fit = 0
        for i in range(len(individual)):
            if individual[i] == self.target[i]:
                fit+=1
        return fit
    
    def selection(self, poblacion):
        scores = [(self.fitness(i),i) for i in poblacion]
        score = [i[1] for i in sorted(scores)]
        selected = score[len(score)-self.n_selection:]
        return selected

    def reproducion(self,poblacion,selection):
        point = 0
        father = []
        for i in range(len(poblacion)):
            point = np.random.randint(1, len(self.target) -1)
            father = random.sample(selection,2)

            poblacion[i][:point] = father[0][:point]
            poblacion[i][point:] = father[1][point:]
        return poblacion

    def mutacion(self, poblacion):
        for i in range(len(poblacion)):
            if random.random() <= self.mutation_rate:
                point = random.randint(1, len(self.target)-1)
                new_value = np.random.randint(0,2)

                while new_value == poblacion[i][point]:
                    new_value = np.random.randint(0,2)
                poblacion[i][point] = new_value
        return poblacion

    def run_generation(self):
        poblacion = self.create_population()
        for i in range(self.n_generations):
            if self.verbose:
                print('---------')
                print('generacion: '+str(i))
                print('poblacion: ', poblacion)
            selected = self.selection(poblacion)
            poblacion=self.reproducion(poblacion, selected)
            poblacion=self.mutacion(poblacion)
            if self.target in poblacion:
                break
        return poblacion

NUMERO_FICHAS = 24

def pintar(x,y):
    flag = True
    for i in range(4):
        print('\n-------------')
        if flag:
            for l in x:
                valor = 'X' if l==1 else 'O'
                print(valor,end=' ')
        else:
            for l in y:
                valor = 'X' if l==1 else 'O'
                print(valor,end=' ')
        flag = not flag
        
def main():
    target = [1,0,1,0,1,0] 
    model = DNA(target, 0.02, 6, 5, 50, True)
    x=model.run_generation()
    print(x)
    if target in x:
        indice = x.index(target)
        valor = x.pop(indice)
        pintar(valor, valor[::-1])
    else:
        main()

if __name__ == '__main__':
    main()