from collections import deque, namedtuple


def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key=lambda x: x[1])
    return sub_li

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return current_vertex, distances[dest]

respuesta = []

def iterar_casos(casos):        #Iteraciones para casos

    for x in range(casos):
        arcos = int(input())
        iterar_arcos(arcos, x + 1)

def iterar_arcos(arcos, caso_actual):        #Iteraciones para arcos

    edges = []

    for x in range(arcos):
        origen, destino, costo = input().split()        #Obtener origen, destino y costo para cada arco
        costo = int(costo)
        edges.append((origen, destino, costo))
        edges.append((destino, origen, costo))

    patrullas = list(input().split()) #Obtener ubicacion de las patrullas
    ubicacion_crimen, patrullas_necesitadas = input().split()   #Obtener ubicacion del crimen  y patrullas necesarias
    patrullas_necesitadas = int(patrullas_necesitadas)

    graph = Graph(edges)
    length = len(patrullas)
    respuesta.append(f'Caso: {caso_actual} ')

    caminos = []

    for x in range(length):

        caminos.append(graph.dijkstra(patrullas[x], ubicacion_crimen))

    Sort(caminos)
    mas_cercanas = caminos[:patrullas_necesitadas]
    for y in mas_cercanas:
        cadena = f'{y[0]} {y[1]}'
        respuesta.append(cadena)
    graph.edges.clear()
    caminos.clear()

#Entrada de datos
casos_prueba = int(input())
iterar_casos(casos_prueba)

for i in respuesta:
    print(i)
'''
2
6
a b 3
a c 1
b c 7
b e 1
c d 2
d e 7
c e a
b 3
4
a b 2
b z 3
c d 3
d z 3
a c
z 2
'''
