from system_controller import SystemController

if __name__ == "__main__":
    controller = SystemController()
    controller.upload_schedule()
    controller.generate_cart_assignments()
    controller.print_cart_schedule()
    controller.update_up_next_widget()