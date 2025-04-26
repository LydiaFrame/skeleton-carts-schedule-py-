import datetime

class Bagger:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = datetime.datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.datetime.strptime(end_time, "%H:%M")

    def is_available(self, time):
        return self.start_time <= time <= self.end_time