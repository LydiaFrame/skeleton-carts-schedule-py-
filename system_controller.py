import datetime
from schedule import Schedule
from cart_assignment import CartAssignment
from up_next_widget import UpNextWidget

class SystemController:
    def __init__(self):
        self.schedule = Schedule()
        self.cart_assignments = []
        self.widget = UpNextWidget()

    def upload_schedule(self):
        self.schedule.collect_bagger_data()

    def generate_cart_assignments(self):
        current_time = datetime.datetime.strptime("07:00", "%H:%M")
        end_time = datetime.datetime.strptime("22:00", "%H:%M")
        last_assigned = {}  # Keeps track of last assignment time per bagger

        while current_time <= end_time:
            available_baggers = []

            for bagger in self.schedule.baggers:
                if bagger.is_available(current_time):
                    last_time = last_assigned.get(bagger.name)
                    if not last_time or (current_time - last_time).total_seconds() >= 3600:
                        available_baggers.append(bagger)

            if available_baggers:
                selected_bagger = available_baggers[0]
                assignment = CartAssignment(current_time, selected_bagger.name)
                self.cart_assignments.append(assignment)
                last_assigned[selected_bagger.name] = current_time

            current_time += datetime.timedelta(minutes=30)

    def print_cart_schedule(self):
        print("\n🛒 Cart Schedule\n------------------------------")
        for assignment in self.cart_assignments:
            print(assignment)

    def update_up_next_widget(self):
        if self.cart_assignments:
            self.widget.update_display(self.cart_assignments[0])