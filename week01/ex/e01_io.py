class IOcontainer:
    msg = ""
    def read_input(self):
        self.msg = input("")
    def print_message(self):
        print("Nothing to display." if not(len(self.msg)) else self.msg)
    def reset_message(self):
        self.msg = ""