__author__ = 'ada'

from Graph_Implementation import Vertex, Graph

# a Bucket is nothing else than... a list of vertices. with a name.
class VerticesWithSamePattern():
    def __init__(self, pattern, initial_vertices=[]):
        self.name = pattern
        self.vertices = initial_vertices

    def add_vertex(self, v):
        print v.id + " added to: " + self.name
        self.vertices.append(v)

    def get_vertices(self):
        return self.vertices

f = VerticesWithSamePattern("foo_")
assert (len(f.vertices) == 0)

f.add_vertex(Vertex("food"))
f.add_vertex(Vertex("foot"))
assert(f.vertices[0].id=="food")
assert(f.name == "foo_")

book = Vertex("book")
b = VerticesWithSamePattern("boo_", [book, Vertex("boot")])
print b.name
print b.vertices




#2nd approach: take four-letter words from the file - create 4 buckets with
# combination of missing words, then when next 4 lettered word compare with
# the existing buckets, if not, create for it other 4
# we use a dictionary where we store as keys = the buckets, as values = the
# words that go into that bucket ==> the words in same buckets will be neighbours,
# connected in the graph

def build_word_graph_bucket(words):

    # old solution: bucket_dict contained a list of Vertices
    # new solution: bucket_dict contains a Bucket! so everywhere
    # where we used bucket_dict as a list, the code will now... break! must be fixed
    buckets_dict = {}
    four_word_graph = Graph()
    for w in words:
        four_word_graph.create_and_add_vertex_from_info(w)

    # create a dictionary with buckets and words
    for word_vertex in four_word_graph.get_vertices():
        for each_letter in range(len(word_vertex.id)): # {r_ot: "root, raut,"  _oot: poot, root}
            bucket_name = word_vertex.id[:each_letter] + "_" + word_vertex.id[(each_letter+1):]
            #
            # if the bucket exists
            if bucket_name in buckets_dict:
                # buckets_dict[bucket_name].append(word_vertex)
                buckets_dict[bucket_name].add_vertex(word_vertex)
            else:
            # if the bucket does not exist in dict
            #     sol. 1
                # buckets_dict[bucket_name] = [word_vertex]
                # sol. 2
                buckets_dict[bucket_name] = VerticesWithSamePattern(bucket_name, [word_vertex])
                # sol. 3
                # buckets_dict[bucket_name] = Bucket(bucket_name)
                # buckets_dict[bucket_name].add_word(word_vertex)

# Statically Typed -> Java, Scala
# Dynamically Typed -> Python, Smalltalk

# create edges between neighbours in graph: each bucket and the words values
    for bucket in buckets_dict:
        for each_vertex in (buckets_dict.get(bucket)).get_vertices(): # dict.get(key) => values of that key
            for next_value in (buckets_dict.get(bucket)).get_vertices():
                if each_vertex != next_value:
                    #each_value.add_undirected_neighbour(next_value)
                    four_word_graph.add_edge(each_vertex, next_value)

    return four_word_graph


def number_letters_words_starting_with_letter(number_letters, start_letter):
    interesting_words = []
    #file = open("/usr/share/dict/words", "r")
    file = open("", "r")
    for each_line in file:
        word = each_line[:-1]
        if len(word) == number_letters and word[0] == str(start_letter):
            interesting_words.append(word)
    return interesting_words



words = ["root", "loot"]

g = build_word_graph_bucket(number_letters_words_starting_with_letter(5,"b"))
assert(len(g.get_vertices()) > 0)
print len(g.get_vertices())
#assert (g.get_vertex("root").id=="root")

print g.string_as_dot()

g.save_dot_to_file("a_4_letteredwords_graph_reprezentation.dot")
g.save_dot_to_file("/Users/ada/Desktop/a_4_words.dot")
