from bagger import Bagger

class Schedule:
    def __init__(self):
        self.baggers = []

    def collect_bagger_data(self):
        count = int(input("Enter number of baggers: "))
        for _ in range(count):
            name = input("Enter bagger name: ")
            start = input("Enter start time (HH:MM, 24-hour): ")
            end = input("Enter end time (HH:MM, 24-hour): ")
            self.baggers.append(Bagger(name, start, end))