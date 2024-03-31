import pytest
import uvsim
from gui import GUI
from tkinter import *
from unittest.mock import patch, MagicMock, Mock
from tkinter import filedialog



@pytest.fixture
def model():
    return uvsim.UVSim()

# Test Initialization
def test_initialization():  #1 Test Initilization of object.
    model = uvsim.UVSim()
    assert model.counter == 0
    assert model.accumulator == 0
    assert model.program == []
 
# Test Run: Halt
def test_halt(): #4
    model = uvsim.UVSim()
    model.run_program = True
    model.program = ["4300"]
    result = model._halt()
    assert model.run_program == False   # If halt instruciton is reached, program will return True

# Test Location Checker
def test_check_location():  #5 Testing a function that validates memory indexes.
    model = uvsim.UVSim()
    model.program = [2,4,6,8,20,12] # the length of this memory is 6
    result = model._check_location(3)  # Valid index of memory, will return location
    assert result == 3

    try:
        model._check_location(-2)   # -2 is invalid index of memory
    except IndexError as e:
        assert str(e) == "Location Index out of range"

    try: 
        model._check_location(6)  # This is over the max index of memory which is 5 as seen above (Length is 6, max index is 5)
    except IndexError as e:
        assert str(e) == "Location Index out of range"


# Test I/O Operations
def test_write():   #6 Tests function that prints a word to screen from specified memory location.
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5","6","7","8","9"]
    result = model._write(8)           # This should return what is being printed to the console
    assert result == "9"

def test_write():   #7 Bound check
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5","6","7","8","9"]
    try:
        model._write(105)   # Out of bounds index (should raise an index error)
    except IndexError as e:
        assert str(e) == "Location Index out of range"

    try: 
        model._write(-20) # Out of bounds index (should raise an index error)
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_read(model): #8 Tests reading input and storing it to memory location
    model.program = ["1","2","3","4","5","6"]
    result = model._read("1234", 5)
    assert result == "1234" and model.program[5] == "1234"

    try:
        result = model._read("12345", 5)
    except ValueError as e:
        assert str(e) == "Invalid Input"

    try:
        result = model._read(2, 2)
    except ValueError as e:
        assert str(e) == "Invalid Type"
    

def test_read_2(model): #9 Memory bound check
    with patch("builtins.input", side_effects=['-6789']): # all invalid input will be ignored
        model.program = ["1","2","3","4","5","6"]
        
        try:
            model._read("1100", 10)
        except IndexError as e:
            assert str(e) == "Location Index out of range"

        try:
            model._read("1100",-20)
        except IndexError as e:
            assert str(e) == "Location Index out of range"

# Test Load/Store Operations
def test_store():   #10 Tests store function that stores accumulator to memory location 
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"] # Memory bound is 0-4
    model.accumulator = 1099
    model._store(2)         # Value of Accumulator, 1099, is stored at memory location 2
    assert model.program[2] == "1099"

    model.accumulator = 5
    model._store(3) # Store function will add on extra 0s if it doesn't have a length of 4 and a negative if it is negative
    assert model.program[3] == "0005"

    model.accumulator = 50
    model._store(3)
    assert model.program[3] == "0050"

    model.accumulator = -5
    model._store(3)
    assert model.program[3] == "-0005"


def test_store_bound(): #11
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"] # Memory bound is 0-4

    try:                # Under bound check, memory at location -2 doesn't exist
        model._store(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._store(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_load():    #12 Tests load function that loads accumulaotr with value from memory location
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"]
    model._load(2)      # Loads the value at memory location 2, 3, to the accumulator
    assert 3 == model.accumulator
    
def test_load_bound(): #13
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"] 

    try:                # Under bound check, memory at location -2 doesn't exist
        model._load(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._load(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"



# Test Arithmetic Operations
# ADD TESTS WITH INPROPER VALUE TYPE 
    
def test_add():     #14 Test add function and bounds check
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"]
    model.accumulator = 10
    model._arithmetic(30, 2)   # This will add acumulator (10) and memory location 2 (3) and store the result (13) in accumulaotr 
    assert model.accumulator == 13 

    try:                # Under bound check, memory at location -2 doesn't exist
        model._arithmetic(30, -2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._arithmetic(30, 5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_subtract():    #15 Test subtraction function and bounds check
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"]
    model.accumulator = 10
    model._arithmetic(31, 2)  # This will subtract the value at memory location 2 (3) from the value in accumulaotr (10) and store result (7) in accumulator
    assert model.accumulator == 7

    try:                # Under bound check, memory at location -2 doesn't exist
        model._arithmetic(31, -2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._arithmetic(31, 5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_multiply():       #16 Test Multiply function and bounds check
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"]
    model.accumulator = 10
    model._arithmetic(32, 2)  # Multiplies accumulator (10) and memory location 2 (3). Stores result (30) in accumulator
    assert model.accumulator == 30

    try:                # Under bound check, memory at location -2 doesn't exist
        model._arithmetic(32, -2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._arithmetic(32, 5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_divide():      #17 Test Divide function, integer division, division by 0, and bounds check
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","0"]

    model.accumulator = 10
    model._arithmetic(33, 1)    # Divides accumulator (10) by memory location 1 (2). Stores result (2) in accumulator
    assert model.accumulator == 5

    model.accumulator = 10
    model._arithmetic(33, 2)    # Divides accumulator (10) by memory location 2 (3). Stores integer division result (3) in accumulator
    assert model.accumulator == 3

def test_arithmetic():
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"]
    model.accumulator = 10

    try: 
        model._arithmetic(320, 3)
    except ValueError as e:
        assert str(e) == "Invalid Opcode"

    model.accumulator = 10
    try:
        model._arithmetic(33, 4) # Divides accumulator (10) by memory location 4 (0). Should raise an error, divison by 0 is impossible
    except ValueError as e:
        assert str(e) == "Divide by Zero"

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._arithmetic(33, -2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"

    try:            
        model._arithmetic(33, 5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


# Test Control Operations
def test_branch():  #18 Tests branch to location 8. Also makes sure branch is within memory bound.
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]
    model._branch(40, 8)    # Changes program counter to branch location 8
    assert model.counter == 8   

def test_branch_bound(): #19
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch(40, -2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch(40 ,10)     # Over bound check, memory at location 10 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"



def test_branchneg():   #20 Tests branch on negative, positive, and zero values of accumulator. Also checks branch is within memory bound.
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]
    model.accumulator = -5
    model._branch(41, 5)    # Will change counter to location 5 as accumulator (-5) is negative. 
    assert model.counter == 5

    model.accumulator = 0
    model._branch(41, 7)    # Will not change counter to location 7 as accumulator (0) is not negative.
    assert model.counter == 6

    model.accumulator = 1   
    model._branch(41, 8)    # Will not change counter to location 8 as accumulator (1) is not negative.
    assert model.counter == 7

def test_branchneg_bound(): #21
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch(41, -2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch(41, 10)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_branchzero():  #22 ests branch on negative, positive, and zero values of accumulator.  Also checks branch is within memory bound.
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]
    model.accumulator = 0
    model._branch(42, 5)   # Will change counter to location 6 as accumulator is zero. 
    assert model.counter == 5

    model.accumulator = 5
    model._branch(42, 6)  # Will not change counter to location 6 as accumulator is not zero.
    assert model.counter == 6

    model.accumulator = -5  
    model._branch(42, 7)   # Will not change counter to location 7 as accumulator is not zero. 
    assert model.counter == 7


def test_branchzero_bound(): #23
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch(42, -2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch(42, 10)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


# Tests creation of the text editor by creating and writing to the editor
def test_text_editor():
    view = GUI()

    view._text_editor()
    view.text.config(state="normal")
    view.text.insert(END, "Hello")
    view.text.config(state="disabled")
    content = view.text.get("1.0","end-1c")

    assert content == "Hello"

# Tests creation of the console
def test_console():
    view = GUI()
    view._create_program_display(0,0,"void","void")

    view.console.config(state="normal")
    view.console.insert(END, "Hello")
    view.console.config(state="disabled")
    content = view.console.get("1.0","end-1c")

    assert content == "Hello"

# Tests creation of the accumulator label
def test_accumulator():
    view = GUI()
    model = uvsim.UVSim()
    model.accumulator = 10
    view._create_program_display(model.get_accumulator(),model.get_counter,"void","void")

    accum = view.labels[0]
    assert accum.cget("text") == "Accumulator: \n10" 

# Tests creation of the counter label
def test_counter():
    view = GUI()
    model = uvsim.UVSim()
    model.counter = 10
    view._create_program_display(model.get_accumulator(),model.get_counter(),"void","void")

    count = view.labels[1]
    assert count.cget("text") == "Counter: \n10"

# Tests the update labels method
def test_update_labels():
    view = GUI()
    model = uvsim.UVSim()
    model.counter = 10
    view._create_program_display(model.get_accumulator(),model.get_counter(),"void","void")

    accum = view.labels[0]
    count = view.labels[1]

    view._update_labels(accum, count, 25, 40)
    assert count.cget("text") == "Counter: \n40"
    assert accum.cget("text") == "Accumulator: \n25"


# Tests the append to console method
def test_append_console():
    view = GUI()

    view._create_program_display(0, 0, "void", "void")
    view.append_console("Hello")

    content = view.console.get("1.0","end-1c")
    assert content == "Hello\n"

# Tests loading a valid file
def test_load_valid_txt():
    view = GUI()
    root = Tk()


    my_frame = Frame(root, background = "white")
    text = Text(my_frame, width=40, height = 20, font=("Arial",16), selectbackground="gray", selectforeground="black", undo=True, bg="lightgray", fg="black",insertbackground="black")
    with open("program.txt","r") as file_in:
        file_content = file_in.read()

    view.process_file("program.txt", text)
    content = text.get("1.0","end-1c")
    assert file_content == content

# Tests loading a non existent file
def test_load_invalid_txt():
    view = GUI()
    root = Tk()

    my_frame = Frame(root, background = "white")
    text = Text(my_frame, width=40, height = 20, font=("Arial",16), selectbackground="gray", 
                selectforeground="black", undo=True, bg="lightgray", fg="black",insertbackground="black")
    with open("program.txt","r") as file_in:
        file_content = file_in.read()

    try:
        view.process_file("eder.txt", text)     # eder.txt file doesn't exist so it cannot proccess it
    except ValueError as e:
        assert str(e) == "No such file or directory: 'eder.txt'"

# Tests saving the text to a file
def test_save():
    view = GUI()
    root = Tk()

    my_frame = Frame(root, background = "white")
    text = Text(my_frame, width=40, height = 20, font=("Arial",16), selectbackground="gray", 
                selectforeground="black", undo=True, bg="lightgray", fg="black",insertbackground="black")
    
    text.config(state="normal")
    text.insert(END, "Hello")
    text.config(state="disabled")
    content = text.get("1.0","end-1c")

    # Implementation of save method
    file_path = "eder.txt"
    if file_path:
        try:
            with open(file_path, 'w') as file:
                text_content = text.get("1.0","end-1c")
                file.write(text_content) #Write text box content to file

            #Tell the User the Filed was saved
            text.config(state="normal")
            text.insert(END, f"File saved: {file_path}\n")
            text.config(state="disabled")
        except Exception as e:
            text.config(state="normal")
            text.insert(END, f"Error saving file: {str(e)}\n")
            text.config(state="disabled")
            "Error saving file:"

        
        with open(file_path, "r") as file:
            text_content = file.read()
            assert text_content == content

