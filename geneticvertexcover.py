import random

class GeneticVertexCover():
  def __init__(self, k):
    '''
    Parameterized vertex cover using a genetic algorithm.
    '''
    self.k = k
    self.verts = None
    self.adj_li = None
    self.pop = None

  def fit(self, verts, adj_li):
    self.verts = verts
    self.adj_li = adj_li

  def run(self, n, gen_size):
    if self.pop is None:
      pop = [6, 2, 1, 7]
    gen = 0
    for r in range(n):
      fitness = self.get_fitness(pop)
      i = 0
      while i < gen_size:
        new_pop = []
        indiv = self.select(pop)
        p = random.random()
        if p <= 0.3:
          new_pop.append(self.reproduce(indiv))
        elif 0.3 < p and p <= 0.6:
          new_pop.append(self.mutate(indiv))
        else:
          indivv = self.select(pop)
          new_pop += self.crossover(indiv, indivv)
          i += 1
        i += 1
      pop += new_pop
    self.pop = pop
    
  def reproduce(self, x):
    return x

  def mutate(self, x):
    return x

  def crossover(self, x, y):
    return [x, y]

  def select(self, pop):
    i = random.randint(0, len(pop)-1)
    return pop[i]

  def get_fitness(self, pop):
    return [1] * len(pop)
