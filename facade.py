from controller import Controller

class Facade:
    def __init__(self, controller):
        self.controller = controller

    def run_system(self):
        self.controller.view.create_main_window(self.controller.model.get_accumulator(), self.controller.model.get_counter(), 
            self.controller.get_run(), self.controller.model.get_halt())
        

def main():
    application = Facade(Controller())
    application.run_system()
    
if __name__ == "__main__":
    main()
