__author__ = 'ada'

from Graph_Implementation import Vertex, Graph

def letter_distance(word, another):
    counter = 0
    for i in range(len(word)):
        if word[i] != another[i]:
            counter += 1
    return counter


# one approach: we create a list with all the four-letter words in the file => we compare each word with the others and verify how many letters it differ
def build_word_graph():

    word_graph = Graph()

    file = open("/usr/share/dict/words", "r")
    for line in file:
        word = line[:-1]
        if len(word) == 4:
            word_graph.add_vertex(word)

    count = 0
    for word_v in word_graph.get_vertices():
        print str(count) + " : " + word_v.id
        count += 1
        for each_v in word_graph.get_vertices():
            if letter_distance(word_v.id, each_v.id) == 1:
                # print word_v.id + " - " + each_v.id
                word_v.add_undirected_neighbour(each_v)

    return word_graph

#2nd approach: take four-letter words from the file - create 4 buckets with combination of missing words, then when next 4 lettered word compare with the existing buckets, if not, create for it other 4
# we use a dictionary where we store as keys = the buckets, as values = the words that go into that bucket ==> the words in same buckets will be neighbours, connected in the graph
def build_word_graph_bucket():

    bucket_words_dict = {}
    four_word_graph = Graph()

    file = open("/usr/share/dict/words","r")
    for each_line in file:
        word = each_line[:-1]
        if len(word) == 4:
            four_word_graph.add_vertex(word) # actually a list with the vertices; the vertices: id + neighbours   [[v1_id, [n1,n2,n3]], [v2_id, [n2, n3]],] or  [[v1, {n1:3,n2:4,n3:5}, etc ]

# create a dictionary with buckets and words
    for word_vertex in four_word_graph:
        for each_letter in len(word_vertex.id): # poop
            bucket = word_vertex.id[:each_letter] + "_" + word_vertex.id[(each_letter+1):]
            # if the bucket exists
            if bucket in bucket_words_dict:
                bucket_words_dict[bucket].append(word_vertex.id)
            else:
            # if the bucket does not exist in dict
                bucket_words_dict[bucket] = word_vertex.id


# create edges between neighbours in graph: each bucket and the words values
    for bucket in bucket_words_dict:
        for each_value in bucket_words_dict.get(bucket): # dict.get(key) => values of that key
            for next_value in bucket_words_dict.get(bucket):
                if each_value != next_value:
                    #each_value.add_undirected_neighbour(next_value)
                    four_word_graph.add_edge(each_value, next_value)

    return four_word_graph





g = build_word_graph_bucket()
assert(len(g.get_vertices()) > 0 )
print len(g.get_vertices())
assert (g.get_vertex("nice").id=="nice")





















