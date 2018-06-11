class Graph(dict):
  def __init__(self,  vs=[], es=[]):
    for v in vs:
      self.add_vertex(v)
    for e in es:
      self.add_edge(e)

  def add_vertex(self, v):
    self[v] = 