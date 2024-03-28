from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import filedialog

class GUI:              # Eder Sandoval
    def __init__(self):
        self.root = Tk()
        #self.simulator = UVSim()
        self.my_frame = Frame(self.root, background = "white")
        self.console = Text(self.my_frame, height=20, width=35, background="lightgray",bd=1, relief="solid", highlightbackground="black",
                             highlightcolor="black", highlightthickness=1,fg="black", wrap="word",state="disabled") # state="disabled"
        self.text_content = [] 
        self.labels = []

    def _text_editor(self):     # Left side of the screen
        # Create Main Frame
        my_frame = Frame(self.root, background="white")
        my_frame.grid(row=1, column=1, columnspan=2)

        basic_ml_label = Label(my_frame, text="BasicML Program", fg="black", bg="white")
        basic_ml_label.grid(row=0, column=0, columnspan=4, sticky="ew")


        # Create Scrollbar
        text_scroll = Scrollbar(my_frame)
        text_scroll.grid(row=1, column=3, sticky="ns")


        # Create Text Box
        text = Text(my_frame, width=40, height = 20, font=("Arial",16), selectbackground="gray", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, bg="lightgray", fg="black",insertbackground="black")
        text.grid(row=1, column=0, columnspan=3)

        # Configure Scrollbar
        text_scroll.configure(command=text.yview)

        # Empty Label
        empty = Label(my_frame, text="\n",bg="white")
        empty.grid(row=2,column=1)

        #Load From File Button
        load_file=Button(my_frame, text="Load From File", width=20, height=2, bg="white", command=lambda: self.load_from_file(text))
        load_file.grid(row=3,column=0)

        #Save To File Button
        save_file=Button(my_frame, text="Save to File", width=20, height=2, bg="white", command=lambda: self.save_to_file(text))
        save_file.grid(row=3, column=2)

        # Load Button
        load = Button(my_frame, text="Load", width=12, height = 2, bg="white", command=lambda: self.receive_text(text))  # command=command1
        load.grid(row=3, column=1)

    def receive_text(self, content):
        program_string =  content.get("1.0","end-1c")
        self.text_content = program_string.split('\n')
        #Program Loaded Feedback
        self.console.config(state="normal")
        self.console.insert(END, "Program Loaded into Memory\n")
        self.console.config(state="disabled")

    def load_from_file(self, text):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt")])
        if file_path: 
            self.process_file(file_path, text)

    def process_file(self, file_path, text):
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
                text.delete("1.0","end-1c")
                text.insert("end-1c",file_contents)
        except Exception as e:
            print(str(e))

    def save_to_file(self,text):
        file_path=filedialog.asksaveasfilename(title="Save as File", filetypes=[("Text files", "*.txt")], defaultextension=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    text_content = text.get("1.0","end-1c")
                    file.write(text_content) #Write text box content to file
                #Tell the User the Filed was saved
                self.console.config(state="normal")
                self.console.insert(END, f"File saved: {file_path}\n")
                self.console.config(state="disabled")
            except Exception as e:
                self.console.config(state="normal")
                self.console.insert(END, f"Error saving file: {str(e)}\n")
                self.console.config(state="disabled")
                "Error saving file:"
                    
            

    def _create_program_display(self, accum_value, count_value, cm1, cm2):  # Right side of the screen    # need command 1 and command 2 parameters for run and stop button
        # Function that dispalys the accumulator, counter, run and stop buttons, and console
        # frame = Frame(self.root)
        #my_frame = Frame(self.root, background = "white")
        self.my_frame.grid(row =1, column=4, columnspan=2)
        
        # Create UVSim label    Row 0
        uvsim_label = Label(self.my_frame, text="UVSim", fg="black", bg="white", height=3)
        uvsim_label.grid(row=0, column=0, columnspan=4, sticky="ew")

        # Create Accumulator and Counter Displays Row 1 and 2
        accumulator = Label(self.my_frame, text = f"Accumulator: \n{accum_value}", bg="lightgray", fg="black", width=12, height=2,
                            bd=1, relief="solid", highlightbackground="black",highlightcolor="black",highlightthickness=1, anchor="w", justify="left")
        
        counter = Label(self.my_frame, text=f"Counter: \n{count_value}", bg="lightgray", fg="black", width=12, height=2,
                        bd=1, relief="solid", highlightbackground="black",highlightcolor="black",highlightthickness=1, anchor="w", justify="left")

        accumulator.grid(row=1, column=0)
        counter.grid(row=1, column=1)

        # Create Empty Label
        empty = Label(self.my_frame, text="\n",bg="white")
        empty.grid(row=2,column=0)


        # Create Run and Stop Buttons Row 3
        run_button = Button(self.my_frame, text="Run", width=8, height = 2, bg="white", command=cm1)  # command=command1
        stop_button = Button(self.my_frame, text="Stop", width=8, height=2, bg="white", command=cm2)  # command=command2

        run_button.grid(row=3, column=0)
        stop_button.grid(row=3, column = 1)
        

        # Create the Console Row 4 and 5
        console_label = Label(self.my_frame, text="Console", bg="white", fg="black")
        console_label.grid(row=4, column=0, sticky="ew")

        text_scroll = Scrollbar(self.my_frame)
        text_scroll.grid(row=5, column=4, sticky="ns")

        self.console = Text(self.my_frame, height=15, width=35, background="lightgray",bd=1, relief="solid", highlightbackground="black",
                             highlightcolor="black", highlightthickness=1,fg="black",yscrollcommand=text_scroll.set, wrap="word",state="disabled") # state="disabled"

        self.console.grid(row=5, column=0, columnspan=4)
        self.labels.append(accumulator)
        self.labels.append(counter)
        self._update_labels(accumulator, counter, accum_value, count_value)

    def _update_labels(self, a, c, accum_value, count_value):
        a.config(text=f"Accumulator: \n{accum_value}")
        c.config(text=f"Counter: \n{count_value}")
        # self.root.after(1000, self._update_labels, a, c, accum_value, count_value)

    def create_main_window(self, a, c, cm1, cm2):
        self.root.title("UVSim")
        self.root.configure(bg="white")     # changes background color to white
        self.root.configure(bd=3, relief="solid", highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.root.geometry("920x650")   # dimensions of starting gui
        uvsim_label = Label(self.root, text="UVSim",bg="white", fg="black") # Place UVSim label outside frames in corner
        uvsim_label.grid(row=0, column=0, sticky="ew")
        empty_label = Label(self.root, text="                ",bg="white")


        self._text_editor() # This takes up column 1 and 2
        empty_label.grid(row=0, column=3)   # This takes up column 3
        self._create_program_display(a, c, cm1, cm2) # This takes up column 4 and 5
        self.root.mainloop()