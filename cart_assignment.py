class CartAssignment:
    def __init__(self, time, bagger_name):
        self.time = time
        self.bagger_name = bagger_name

    def __str__(self):
        return f"{self.time.strftime('%I:%M %p')} - {self.bagger_name}"