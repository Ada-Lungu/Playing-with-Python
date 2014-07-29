__author__ = 'ada'

class Printer:
    # how many pages/minute
    # if it is busy, has currentTask working
    # how much time remaining from the current task
    def __init__(self, ppm): # pagerate could be 5pages/min or 10pages/min
    self.pagerate = ppm
    self.currentTask = None
    self.timeRemaining = 0 # for the tasks in the printer to be completed

    def tick_timer(self): # keeps updated the current time, sets the remaining time for the tasks completion
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1 # seconds
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self): # is the printer working, has tasks in progress or not
        if self.currentTask != None:
            return True
        else:
            return False

    def start_next(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * self.pagerate # getPages method will be defined in task class


import random

class Task:
    def __init__(self,time_task_insertion):
    self.time_task_insertion = time_task_insertion
    self.pages = random.randrange(1, 21) # random no of pages the task will have

    def getStamp(self):
        return self.time_task_insertion

    def getPages(self):
        return self.pages

    def waitingTime(self, currentTime):
        return currentTime - self.time_task_insertion # timpul cat s-a asteptat pana la current time


# we want to calculate the waiting time for different pagerate

from Pythonds.basic.queue import Queue
import random

def simulation(time_completion_tasks, ppm):

    labprinter = Printer(ppm)
    printQueue = Queue()
    waiting_times = []

    for currentTime in range(time_completion_tasks):

        if newPrintTask():
            task = Task(currentTime)
            printQueue.enqueue(task)



    def newPrintTask():
        num = random.randrange(1,181)
        if num == 180:
            return True
        else:
            return False



















