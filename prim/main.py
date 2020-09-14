class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}

    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def display(self):
        print('Vertices: ', end='')
        for v in self:
            print(v.get_key(), end=' ')
        print()

        print('Edges: ')
        for v in self:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key

    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight

    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()

    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]

    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to


def mst_prim(g):
    """Return a minimum cost spanning tree of the connected graph g."""
    mst = Graph()  # create new Graph object to hold the MST

    # if graph is empty
    if not g:
        return mst

    # nearest_neighbour[v] is the nearest neighbour of v that is in the MST
    # (v is a vertex outside the MST and has at least one neighbour in the MST)
    nearest_neighbour = {}
    # smallest_distance[v] is the distance of v to its nearest neighbour in the MST
    # (v is a vertex outside the MST and has at least one neighbour in the MST)
    smallest_distance = {}
    # v is in unvisited iff v has not been added to the MST
    unvisited = set(g)

    u = next(iter(g))  # select any one vertex from g
    mst.add_vertex(u.get_key())  # add a copy of it to the MST
    unvisited.remove(u)

    # for each neighbour of vertex u
    for n in u.get_neighbours():
        if n is u:
            # avoid self-loops
            continue
        # update dictionaries
        nearest_neighbour[n] = mst.get_vertex(u.get_key())
        smallest_distance[n] = u.get_weight(n)

    # loop until smallest_distance becomes empty
    while (smallest_distance):
        # get nearest vertex outside the MST
        outside_mst = min(smallest_distance, key=smallest_distance.get)
        # get the nearest neighbour inside the MST
        inside_mst = nearest_neighbour[outside_mst]

        # add a copy of the outside vertex to the MST
        mst.add_vertex(outside_mst.get_key())
        # add the edge to the MST
        mst.add_edge(outside_mst.get_key(), inside_mst.get_key(),
                     smallest_distance[outside_mst])
        mst.add_edge(inside_mst.get_key(), outside_mst.get_key(),
                     smallest_distance[outside_mst])

        # now that outside_mst has been added to the MST, remove it from our
        # dictionaries and the set unvisited
        unvisited.remove(outside_mst)
        del smallest_distance[outside_mst]
        del nearest_neighbour[outside_mst]

        # update dictionaries
        for n in outside_mst.get_neighbours():
            if n in unvisited:
                if n not in smallest_distance:
                    smallest_distance[n] = outside_mst.get_weight(n)
                    nearest_neighbour[n] = mst.get_vertex(outside_mst.get_key())
                else:
                    if smallest_distance[n] > outside_mst.get_weight(n):
                        smallest_distance[n] = outside_mst.get_weight(n)
                        nearest_neighbour[n] = mst.get_vertex(outside_mst.get_key())

    return mst


g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('mst')
print('display')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                    g.add_edge(dest, src, weight)
                else:
                    print('Edge already exists.')

    elif operation == 'mst':
        mst = mst_prim(g)
        print('Minimum Spanning Tree:')
        mst.display()
        print()

    elif operation == 'display':
        g.display()
        print()

    elif operation == 'quit':
        break

'''
Case 1:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest> <weight>
mst
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add vertex 4
What would you like to do? add vertex 5
What would you like to do? add vertex 6
What would you like to do? add vertex 7
What would you like to do? add edge 1 3 18
What would you like to do? add edge 1 2 10
What would you like to do? add edge 3 4 70
What would you like to do? add edge 3 2 6
What would you like to do? add edge 2 5 20
What would you like to do? add edge 5 6 10
What would you like to do? add edge 5 7 10
What would you like to do? add edge 6 7 5
What would you like to do? mst
Minimum Spanning Tree:
Vertices: 1 2 3 4 5 6 7 
Edges: 
(src=1, dest=2, weight=10) 
(src=2, dest=5, weight=20) 
(src=2, dest=1, weight=10) 
(src=2, dest=3, weight=6) 
(src=3, dest=2, weight=6) 
(src=3, dest=4, weight=70) 
(src=4, dest=3, weight=70) 
(src=5, dest=6, weight=10) 
(src=5, dest=2, weight=20) 
(src=6, dest=5, weight=10) 
(src=6, dest=7, weight=5) 
(src=7, dest=6, weight=5) 
 
What would you like to do? quit
 
Case 2:
Undirected Graph
Menu
add vertex <key>
add edge <src> <dest> <weight>
mst
display
quit
What would you like to do? add vertex 1
What would you like to do? add vertex 2
What would you like to do? add vertex 3
What would you like to do? add edge 1 2 10
What would you like to do? add edge 2 3 100
What would you like to do? add edge 1 3 50
What would you like to do? mst
Minimum Spanning Tree:
Vertices: 1 2 3 
Edges: 
(src=1, dest=2, weight=10) 
(src=1, dest=3, weight=50) 
(src=2, dest=1, weight=10) 
(src=3, dest=1, weight=50) 
 
What would you like to do? quit
'''