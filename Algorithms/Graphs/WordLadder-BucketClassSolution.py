__author__ = 'ada'


from Algorithms.Graphs.GraphImplementation import Vertex, Graph

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
    word_graph = Graph()

    for w in words:
        word_graph.create_and_add_vertex_from_info(w)

    # create a dictionary with buckets and words
    for word_vertex in word_graph.get_vertices():
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

# create edges between neighbours in graph: each bucket and the words values
    for bucket in buckets_dict:
        for each_vertex in (buckets_dict.get(bucket)).get_vertices(): # dict.get(key) => values of that key
            for next_value in (buckets_dict.get(bucket)).get_vertices():
                if each_vertex != next_value:
                    #each_value.add_undirected_neighbour(next_value)
                    word_graph.add_edge(each_vertex, next_value)

    return word_graph


def ask_input_color_shortest_path(choose_color = ["red", "green", "purple"]):

    color_input = raw_input("Which color you want the path. Choose from:" + str(choose_color))
    while color_input not in choose_color:
        print "Please choose from: red, green or purple."
        color_input = raw_input("Which color you want the path: red, green or purple?")

    print "Nice choice, your path will be awesomely" + " " + color_input
    return color_input


def words_with_given_length_and_starting_letters(number_letters, starting_letters_list):
    interesting_words = []
    #file = open("/usr/share/dict/words", "r")
    #  /
    #  /Users
    #  /bin

    import os
    print os.getcwd()
    file = open("../../wordlists/en.txt","r")
    for each_line in file:
        word = each_line[:-1]
        if len(word) == int(number_letters) and word[0] in starting_letters_list:
            interesting_words.append(word)
    return interesting_words


def words_with_given_length_and_starting_letters_test(number_letters, starting_letters_list):
    interesting_words = []
    #file = open("/usr/share/dict/words", "r")
    #  /
    #  /Users
    #  /bin

#   file = open("wordlists/en.txt","r")
#   for each_line in file:
#        word = each_line[:-1]
    list_words = ["fool", "sage", "pool", "cool", "soul", "swings", "creepy", "chil"]
    for word in list_words:
        if len(word) == number_letters and word[0] in starting_letters_list:
            interesting_words.append(word)
    return interesting_words


# user input for words infos: what letters, no letters
# how we take more letters as input
def ask_input_words_infos():

    starting_letters_list = []

    how_many_starting_letters_input = raw_input("How many starting_letters_input")
    while not isinstance(int(how_many_starting_letters_input), int):
        print "Please use a number."
        how_many_starting_letters_input = raw_input("How many starting_letters_input")


    for i in range(int(how_many_starting_letters_input)):
        starting_letter_input = raw_input("What letter the words can start with?")
        starting_letters_list.append(starting_letter_input)

    number_letters_input = int(raw_input("Choose the words' number of letters: "))

    return number_letters_input, starting_letters_list

# convert string to integer => daca se poate converti, trebuie sa fie "3", "4", "5"



"""# breadth first search
def create_paths_from_start_vertex(start_vertex):
# each vertex will have as instant values: distance, predecessor, colour => they all have the "set" and "get" methods
# we first set these values of the start vertex
    start_vertex.set_distance(0)
    start_vertex.set_color("grey")
    will_be_visited_vertexes = Queue()
    will_be_visited_vertexes.enqueue(start_vertex)

    while will_be_visited_vertexes.size() > 0:
        curr_vertex = will_be_visited_vertexes.dequeue()
        for neighbour_vertex in curr_vertex.get_neighbours_vertices():
            if neighbour_vertex.get_color() == "white":
                neighbour_vertex.set_color("grey")
                neighbour_vertex.set_pred(curr_vertex)
                neighbour_vertex.set_distance(curr_vertex.get_distance() + 1)
                will_be_visited_vertexes.enqueue(neighbour_vertex)
        curr_vertex.set_color("black")


# the path from one vertex to another
def get_path_from_vertex1_to_vertex2(vertex1, vertex2):
    create_paths_from_start_vertex(vertex1)
    get_path_list_vertices = []
    x = vertex2
    while x != vertex1:
        get_path_list_vertices.append(x)
        x = x.get_pred()
    get_path_list_vertices.append(x)
    return get_path_list_vertices"""


def request_input_from_to_what_vertex(g, message_for_the_user):
    vertex_name = raw_input(message_for_the_user)
    print vertex_name
    return g.get_vertex(vertex_name)


"""def print_path_from_vertex1_to_vertex2(vertex1, vertex2):
    for vertex_visited in get_path_from_vertex1_to_vertex2(vertex1, vertex2):
        print vertex_visited.id"""


def print_and_recurse(v2, v1):
    if v2 == v1:
        return
    print v2.id()
    print_and_recurse(v2.get_pred(), v1)


#print words_with_given_length_and_starting_letters(4, ["s", "p", "f", "c"]) - functioneaza

#print ask_input_words_infos() - fuctioneaza

number_letters_input, starting_letters_list = ask_input_words_infos() # the variables from first tuple take the value of the second tuple
print starting_letters_list
print number_letters_input, starting_letters_list

print words_with_given_length_and_starting_letters(number_letters_input, starting_letters_list)



def create_5b_words_graph():

    g = build_word_graph_bucket(words_with_given_length_and_starting_letters(5, ["b"]))
    assert(len(g.get_vertices()) > 0)
    print len(g.get_vertices())

    #assert (g.get_vertex("root").id=="root")

    from_vertex_input = request_input_from_to_what_vertex(g, "From vertex...")
    to_vertex_input = request_input_from_to_what_vertex(g, "To vertex...")
    color = ask_input_color_shortest_path(["red", "green", "purple"])

    g.save_dot_to_file("5_lettered_english_words_one_edge_visualization.dot",
                       g.get_path_from_vertex1_to_vertex2(
                           from_vertex_input,
                           to_vertex_input),
                        color)

    #print g.get_vertex("bands").is_path(g.get_vertex("bonus"), [])
    #print g.get_vertex("bands").shortest_path(g.get_vertex("bonus"), [])

    g.print_path_from_vertex1_to_vertex2(
        from_vertex_input,
        to_vertex_input)

    # g.print_as_dot(
    #     g.get_path_from_vertex1_to_vertex2(
    #         from_vertex_input,
    #         to_vertex_input),
    #     ask_input_color_shortest_path(["red", "green", "purple"]))"""



#number_letters_input, starting_letters_list = ask_input_words_infos() # the variables from first tuple take the value of the second tuple

# same as line above
# number_letters_input = ask_input_words_infos()[0]
# starting_letters_list = ask_input_words_infos()[1]


fool_sage_graph = build_word_graph_bucket(words_with_given_length_and_starting_letters(number_letters_input, starting_letters_list))
print len(fool_sage_graph.get_vertices())


from_vertex_input = request_input_from_to_what_vertex(fool_sage_graph, "From vertex...")
to_vertex_input = request_input_from_to_what_vertex(fool_sage_graph, "To vertex...")
color = ask_input_color_shortest_path(["red", "green", "purple"])


fool_sage_graph.print_path_from_vertex1_to_vertex2(from_vertex_input, to_vertex_input)
#(fool_sage_graph.get_vertex("fool"), fool_sage_graph.get_vertex("sage"))

fool_sage_graph.save_dot_to_file("fool-sage-path.dot",
                                 fool_sage_graph.get_path_from_vertex1_to_vertex2(from_vertex_input, to_vertex_input),
                                 ask_input_color_shortest_path())


