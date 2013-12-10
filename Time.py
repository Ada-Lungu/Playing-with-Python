class Time():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def print_time(self):
        print str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def increment(self, extra_seconds=1):
        self.seconds += extra_seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    # returns an int representing seconds
    def calculate_seconds_from_midnight(self):
        m = self.hours * 60 + self.minutes
        s = m * 60 + self.seconds
        return s


t1 = Time(1, 10, 11)
t2 = Time(2, 20, 21)
t1.print_time()
t2.print_time()

t1.increment(70)
t1.print_time()

print t1.calculate_seconds_from_midnight()

