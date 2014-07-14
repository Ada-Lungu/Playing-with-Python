__author__ = 'ada'

from pythonds.basic.queue import Queue

def HotPotato(player_names, num):

    players_queue = Queue()
    round_counter = 0

    for each_player in player_names:
        players_queue.enqueue(each_player)

    while players_queue.size() > 1 and round_counter != num:
            front_player = players_queue.dequeue()
            players_queue.enqueue(front_player)
            round_counter += 1
    if round_counter == num:
        players_queue.dequeue()

    return players_queue.dequeue()

print (HotPotato(["Ada", "Fred", "Copola",], 5))





from pythonds.basic.queue import Queue

def HotPotato(player_names, num):

    players_queue = Queue()

    for each_player in player_names:
        players_queue.enqueue(each_player)

    while players_queue.size() > 1:
        for i in range(num):
            front_player = players_queue.dequeue()
            players_queue.enqueue(front_player)

        players_queue.dequeue()

    return players_queue.dequeue()

print (HotPotato(["Ada", "Fred", "Copola",], 5))








