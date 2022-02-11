from geneticprogram import GeneticVertexCover

def correct_adj_li(adj_li):
  for k in adj_li.keys():
    # make symmetric
    adj_k = []
    for v in adj_li[k]:
      if k not in adj_li[v]:
        adj_li[v].append(k)
      if k != v:
        adj_k.append(v)
    adj_li[k] = adj_k

  # remove duplicates and sort
  for k in adj_li.keys():
    adj_li[k] = sorted(list(set(adj_li[k])))
  
if __name__ == "__main__":
  k = 5
  verts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  adj_li = {
    1: [2, 3, 6],
    2: [10, 3, 1, 7, 4],
    3: [6, 3, 1, 8],
    4: [9, 10, 6],
    5: [8, 2, 6, 1],
    6: [9, 1, 3],
    7: [6],
    8: [2],
    9: [8],
    10: [5]
  }
  correct_adj_li(adj_li)

  gen_vert = GeneticVertexCover(k)
  gen_vert.fit(verts, adj_li)
  gen_vert.run(n=10, gen_size=20)
  print(gen_vert.pop)

