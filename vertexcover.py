#!/usr/bin/env python3
from geneticvc import GeneticVC

def correct_adj_li(adj_li):
  for k in adj_li.keys():
    adj_li[k] = [v for v in adj_li[k] if v != k]

    for v in adj_li[k]:
      if k not in adj_li[v]:
        adj_li[v].append(k)

  for k in adj_li.keys():
    adj_li[k] = sorted(list(set(adj_li[k])))
  
if __name__ == "__main__":
  verts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  adj_li = {
    0: [2, 3, 6],
    1: [9, 3, 1, 7, 4],
    2: [6, 3, 1, 8],
    3: [9, 1, 6],
    4: [8, 2, 6, 1],
    5: [9, 1, 3],
    6: [6],
    7: [2],
    8: [8],
    9: [5]
  }

  correct_adj_li(adj_li)

  gen_vert = GeneticVC(verts, adj_li, k=5)
  gen_vert.run(n=50, m=10)
  fittest, fitness_score = gen_vert.get_fittest()
  print(fittest, fitness_score)

