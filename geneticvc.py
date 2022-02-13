import random
from numpy import argmax
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
    self.tot_edges = sum([len(adj) for adj in adj_li.values()]) // 2

  def run(self, n, m):
    pop = self._init_pop(m)
    fitness = self._get_fitness(pop)
    for r in (t := trange(n)):
      i = 0
      new_pop = []
      while i < m:
        indiv = random.choices(pop, weights=fitness, k=1)[0]
        p = random.random()
        if p <= 0.45:
          # reproduce
          new_pop.append(indiv)
        elif p > 0.45 and p <= 0.5:
          # mutate
          i = random.randint(0, len(indiv)-1)
          diff = list(set(self.verts) - set(indiv))
          indiv[i] = random.choice(diff)
          new_pop.append(indiv)
        else:
          # crossover
          indiv, indivv = random.choices(pop, weights=fitness, k=2)
          i = random.randint(0, len(indiv)-1)
          l = indiv[:i]
          r = indivv[i:]
          new_pop += [l+r, r+l]
          i += 1
        i += 1
      pop += new_pop
      fitness += self._get_fitness(new_pop)
      t.set_description(f"Population size: {len(pop)}; Progress")
    self.pop = pop
    return self
    
  def get_fittest(self):
    fitness = self._get_fitness(self.pop)
    i = argmax(fitness)
    return self.pop[i], fitness[i]

  def _init_pop(self, pop_size):
    return [random.sample(range(0, len(self.verts)-1), self.k) for i in range(pop_size)]

  def _get_fitness(self, pop):
    # fitness based on edge coverage
    return [(self._get_coverage(indv) / self.tot_edges) for indv in pop]

  def _get_coverage(self, verts):
    edges = set()
    for p in verts:
      for q in self.adj_li[p]:
        if p < q:
          edges.add((p, q))
        else:
          edges.add((q, p))
    return len(edges)

