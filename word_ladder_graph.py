__author__ = 'ada'

from Graph_Implementation import Vertex, Graph

# counts the number of letters which differ between the two words
def number_of_different_letters(one, another):
    counter = 0
    for i in range(len(one)):
        if one[i] != another[i]:
            counter += 1
    return counter

assert (number_of_different_letters ("sage", "mage") == 1)


def add_four_letter_words_to_graph(word_graph):
    file = open("/usr/share/dict/words", "r")
    for line in file:
        word = line[:-1]
        if len(word) == 4:
            if (word.startswith("b")):
                word_graph.create_and_add_vertex_from_info(word)

# one approach: we create a list with all the four-letter words in the file =>
# we compare each word with the others and verify how many letters it differ
def build_word_graph():

    word_graph = Graph()

    add_four_letter_words_to_graph(word_graph)

    count = 0
    for word_v in word_graph.get_vertices():
        print str(count) + " : " + word_v.id

        count += 1
        for each_v in word_graph.get_vertices():
            if number_of_different_letters(word_v.id, each_v.id) == 1:
                # print word_v.id + " - " + each_v.id
                word_v.add_undirected_neighbour(each_v)

    return word_graph




words = ["root", "loot"]


g = build_word_graph()
assert(len(g.get_vertices()) > 0)
print "number of vertices in the graph: " + str(len(g.get_vertices()))


# assert (len(g.get_vertex("amir").get_connections()) > 0)


def most_connected_vertex(g):
    max_connections = 0
    most_connected_v = g.get_vertices()[0]

    for each_vertex in g.get_vertices():
        each_vertex_connections = len(each_vertex.get_neighbours_vertices())
        if each_vertex_connections > max_connections:
            max_connections = each_vertex_connections
            most_connected_v = each_vertex

    return most_connected_v

print most_connected_vertex(g)






















