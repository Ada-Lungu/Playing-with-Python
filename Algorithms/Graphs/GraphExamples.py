__author__ = 'ada'


from GraphImplementation import Vertex, Graph

# 1000 most frequent letter words

vertex0 = Vertex("v0")
vertex1 = Vertex("v1")
vertex2 = Vertex("v2")
vertex3 = Vertex("v3")
vertex4 = Vertex("v4")
vertex5 = Vertex("v5")

assert (vertex0.id == "v0")
assert (vertex0.get_neighbours_vertices() == [])

vertex0.add_neighbour(vertex1, 5)
vertex0.add_neighbour(vertex5, 2)
vertex1.add_neighbour(vertex2, 4)
vertex2.add_neighbour(vertex3, 9)
vertex3.add_neighbour(vertex4, 7)
vertex3.add_neighbour(vertex5, 3)
vertex4.add_neighbour(vertex0, 1)
vertex5.add_neighbour(vertex4, 8)
vertex5.add_neighbour(vertex2, 1)

assert (vertex1 in vertex0.get_neighbours_vertices())
assert (vertex5 in vertex0.get_neighbours_vertices())

assert (vertex0.get_weight(vertex1) == 5)

assert (vertex0.shortest_path(vertex1, []) == 5)
# assert (vertex0.shortest_path(vertex2) == 3)


# g = Graph({vertex0, vertex1, vertex2}, 3)


#print g.dijkstras_shortest_path(vertex0, vertex5)

orash1 = Vertex("Arad") # obiect de tip Vertex cu id Arad
orash2 = Vertex("Timisoara")
orash3 = Vertex("Cluj-Napoca")
orash4 = Vertex("Brasov")
orash5 = Vertex("Sibiu")
orash6 = Vertex("Constanta")


orash1.add_neighbour(orash2, 50)
orash1.add_neighbour(orash3, 250)
orash1.add_neighbour(orash4, 460)
orash1.add_neighbour(orash5, 600)
orash1.add_neighbour(orash6, 700)


orash2.add_neighbour(orash3, 330)
orash2.add_neighbour(orash4, 430)
orash2.add_neighbour(orash5, 290)
orash2.add_neighbour(orash6, 780)

orash3.add_neighbour(orash4, 273)
orash3.add_neighbour(orash5, 175)
orash3.add_neighbour(orash6, 670)

orash4.add_neighbour(orash5, 140)
orash4.add_neighbour(orash6, 400)

orash5.add_neighbour(orash6, 500)

orash5.id = "Victoria"
assert(orash5.id == "Victoria")


assert (orash1.is_path(orash2, []))
assert (not orash2.is_path(orash1, []))


g = Graph()

for orash in [orash1,orash2,orash3,orash4, orash5, orash6]:
    g.add_vertex_object(orash)

