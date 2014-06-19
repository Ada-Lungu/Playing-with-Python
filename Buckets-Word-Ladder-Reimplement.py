__author__ = 'ada'

from Graph_Implementation import Vertex, Graph

# read the file and take the four-lettered words

# rewrite for any number
def four_lettered_words(number_of_letters):
    four_lettered_words = []
    words_file = ("/usr/share/dict/words", "r")

    for each_line in words_file:
        word = each_line[:-1]
        if len(word) == number_of_letters:
            four_lettered_words.append(word)
    return four_lettered_words


def create_word_ladder_graph(words):

    # dictionary with the buckets. One bucket composed of: as Key - bucket_name + Values - the words that fit in that bucket
    pattern_to_vertices_list = {}
    ladder_words_graph = Graph()
    for w in words:
        ladder_words_graph.create_and_add_vertex_from_info(w)

    # Lazy vs. Early Initialization
    # n_w_p["buc_"] = {buck, bucu}
    # n_w_p["_uck"] = {buck, luck"}

    """for each_word in words:
        for each_letter_pos in range(len( each_word)): # len(each_word) = va fi un integer, can not execute "for", for is used for a sequence, an array ==> range(len(each_word))
            bucket_name = each_word[:each_letter_pos] + "_" + each_word[each_letter_pos+1:] """

    # we can't use FOR loop only with an array/list, we can't use it on a graph ==> get_vertices - gives us a list with the vertices
    for each_vertex in ladder_words_graph.get_vertices(): # ne uitam ce caracteristici are Vertexul in Graph_implementation: id, neighbours
        # Graphul are: vertices and edges - graphul e un dict [[vertex1_id, {V2:w1,v3:w2,v4:w3}]; vertex2: {n1,n2,n3} ... }]]
        # or [[vertex1_id, [V2,v3,v4]; vertex2: {n1,n2,n3} ... }]] without weights

        # ???? is it mandatory to use .id ==> for now get vertices gives us a list with only the words, without neighbours
        for each_letter_pos in range(len(each_vertex.id)):
            pattern = each_vertex.id[each_letter_pos:] + "_" + each_vertex.id[:each_letter_pos+1]

            # we append the buckets in the dictionary
            # if the bucket_name already exists in the dictionary
            if pattern in pattern_to_vertices_list:
                pattern_to_vertices_list[pattern].append[each_vertex] # ???? add_vertex: de ce? este un dictionar, nu un graph, sau?

            else:
                # if the bucket_name does not exist
                pattern_to_vertices_list[pattern] = [each_vertex]

    # next step: in the graph - all the words within one bucket will be connected as neighbours

    # ??? in cazul asta each_name + next_name sunt strings si la graph ar trebui sa add_edge vertexi?
    for collection_of_neigh_vertices in pattern_to_vertices_list.values():
        for each_vertex in collection_of_neigh_vertices:
            for next_vertex in collection_of_neigh_vertices:
                if each_vertex != next_vertex:
                    ladder_words_graph.add_edge(each_vertex, next_vertex)

    return ladder_words_graph


my_words = ["loop", "loot", "fine"]

my_graph = create_word_ladder_graph(my_words)

print my_graph.string_as_dot()
























