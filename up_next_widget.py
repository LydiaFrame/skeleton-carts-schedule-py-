class UpNextWidget:
    def update_display(self, assignment):
        print(f"\n📲 UpNextWidget: {assignment.bagger_name} is scheduled for {assignment.time.strftime('%I:%M %p')}\n")