import random
import numpy as np
from tqdm import trange 

class GeneticVC():
  def __init__(self, verts, adj_li, k):
    '''
    Parameterized vertex cover using a genetic algorithm.
    '''
    self.verts = verts
    self.adj_li = adj_li
    self.k = k
    self.pop = None

  def run(self, n, m):
    if self.pop is None:
      pop = self.init_pop(m)
    gen = 0
    for r in (t := trange(n)):
      fitness = self.get_fitness(pop)
      i = 0
      while i < m:
        new_pop = []
        indiv = random.choices(pop, weights=fitness, k=1)[0]
        p = random.random()
        if p <= 0.45:
          # reproduce
          new_pop.append(indiv)
        elif 0.45 < p and p <= 0.5:
          new_pop.append(self.mutate(indiv))
        else:
          indiv, indivv = random.choices(pop, weights=fitness, k=2)
          new_pop += self.crossover(indiv, indivv)
          i += 1
        i += 1
      pop += new_pop
      t.set_description(f"Population size: {len(pop)}; Progress")
    self.pop = pop
    return self
    
  def get_fittest(self):
    fitness = self.get_fitness(self.pop)
    i = np.argmax(fitness)
    return self.pop[i], fitness[i]

  def mutate(self, x):
    i = random.randint(0, len(x)-1)
    diff = list(set(self.verts) - set(x))
    x[i] = random.choice(diff)
    return x

  def crossover(self, x, y):
    assert(len(x) == len(y))
    i = random.randint(0, len(x)-1)
    l = x[:i]
    r = y[i:]
    return [l+r, r+l]

  def get_fitness(self, pop):
    # fitness based on edge coverage
    tot_edges = sum([len(adj) for adj in self.adj_li.values()]) // 2
    ret = []
    for indv in pop:
      ret.append(self.get_coverage(indv))
    ret = [v / tot_edges for v in ret]
    return ret

  def init_pop(self, pop_size):
    return [random.sample(range(0, len(self.verts)-1), self.k) for i in range(pop_size)]
    
  def get_coverage(self, verts):
    edges = []
    for p in verts:
      for q in self.adj_li[p]:
        if (q, p) not in edges and (p, q) not in edges:
          edges.append((p, q))
    return len(edges)

