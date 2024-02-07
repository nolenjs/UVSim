import uvsim
'''
TODO
Initialization: Add another check to make sure the program read the file correctly 
Valid Input: Test multiple valid input arguments, include different opcodes
Invalid Input: Test multiple invalid input arguments, include inputs with different length and letter values (not digit)
Input without Halt: A program without a halt instruction should raise an error or else it will be stuck in an infinite loop
Read: Test the read function that has input within it
Halt: Ensure halt opcode works
Arithmetic Operations: Add tests with inproper and different data types

'''
# Test Initialization
def test_initialization():  # Test Initilization of object. 
    model = uvsim.UVSim()
    assert model.counter == 0
    assert model.accumulator == 0
    # Another idea for creating self.program: initiliaze a list of 0000 with 
    # a length of 100. When creating the uvsim object, insert the program as
    # a paramter

# Test Run: Valid Input
def test_valid_input():
    model = uvsim.UVSim()

# Test Run: Invalid Input
def test_invalid_input():
    model = uvsim.UVSim()

# Test Run: Input With No Halt Instruction
def test_input_halt():
    model = uvsim.UVSim()

# Test Location Checker
def test_check_location():  # Testing a function that validates memory indexes.
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
def test_write():   # Tests function that prints a word to screen from specified memory location.
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9]
    model.program[9] == "Correct Location at 9"
    result = model._write(9)           # This should return what is being printed to the console
    assert result == "Correct Location at 9"

    try:
        model._write(105)   # Out of bounds index (should raise an index error)
    except IndexError as e:
        assert str(e) == "Location Index out of range"

    try: 
        model._write(-20) # Out of bounds index (should raise an index error)
    except IndexError as e:
        assert str(e) == "Location Index out of range"

    

def test_read():    # Tests reading input and storing it to memory location   # THIS ONE HAS AN INPUT, LOOK UP HOW TO TEST WITH INPUT
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6]
    input = model._read(5)      # This stores the input to the specified memory location which is 5
    assert input == model.program[5] 

    
    try:
        model._read(10)
    except IndexError as e:
        assert str(e) == "Location Index out of range"

    try:
        model._read(-20)
    except IndexError as e:
        assert str(e) == "Location Index out of range"



# Test Load/Store Operations
def test_store():   # Tests store function that stores accumulator to memory location 
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5] # Memory bound is 0-4
    model.accumulator = 1099
    model._store(2)         # Value of Accumulator, 1099, is stored at memory location 2
    assert model.program[2] == model.accumulator

    try:                # Under bound check, memory at location -2 doesn't exist
        model._store(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._store(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"

def test_load():    # Tests load function that loads accumulaotr with value from memory location
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5] 
    model.program[2] = 1099
    model._load(2)      # Loads the value at memory location 2, 1099, to the accumulator
    assert model.program[2] == model.accumulator
    
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
    
def test_add():     # Test add function and bounds check
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5]
    model.accumulator = 10
    model._add(2)   # This will add acumulator (10) and memory location 2 (3) and store the result (13) in accumulaotr 
    assert model.accumulator == 13 

    try:                # Under bound check, memory at location -2 doesn't exist
        model._add(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._add(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_subtract():    # Test subtraction function and bounds check
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5]
    model.accumulator = 10
    model._subract(2)  # This will subtract the value at memory location 2 (3) from the value in accumulaotr (10) and store result (7) in accumulator
    assert model.accumulator == 7

    try:                # Under bound check, memory at location -2 doesn't exist
        model._subract(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._subract(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_multiply():       # Test Multiply function and bounds check
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5]
    model.accumulator = 10
    model._multiply(2)  # Multiplies accumulator (10) and memory location 2 (3). Stores result (30) in accumulator
    assert model.accumulator == 30

    try:                # Under bound check, memory at location -2 doesn't exist
        model._multiply(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._multiply(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_divide():      # Test Divide function, integer division, division by 0, and bounds check
    model = uvsim.UVSim()
    model.program = [1,2,3,4,0]

    model.accumulator = 10
    model._divide(1)    # Divides accumulator (10) by memory location 1 (2). Stores result (2) in accumulator
    assert model.accumulator == 2

    model.accumulator = 10
    model._divide(2)    # Divides accumulator (10) by memory location 2 (3). Stores integer division result (3) in accumulator
    assert model.accumulator == 3



    model.accumulator = 10
    try:
        model._divide(4) # Divides accumulator (10) by memory location 4 (0). Should raise an error, divison by 0 is impossible
    except ValueError as e:
        assert str(e) == "Divide by zero"

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._divide(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._divide(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    


# Test Control Operations
def test_branch():  # Tests branch to location 8. Also makes sure branch is within memory bound.
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]
    model._branch(8)    # Changes program counter to branch location 8
    assert model.counter == 8   

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch(10)     # Over bound check, memory at location 10 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"



def test_branchneg():   # Tests branch on negative, positive, and zero values of accumulator. Also checks branch is within memory bound.
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]
    model.accumulator = -5
    model._branch_neg(5)    # Will change counter to location 5 as accumulator (-5) is negative. 
    assert model.counter == 5

    model.accumulator = 0
    model._branch_neg(7)    # Will not change counter to location 7 as accumulator (0) is not negative.
    assert model.counter == 5

    model.accumulator = 1   
    model._branch_neg(8)    # Will not change counter to location 8 as accumulator (1) is not negative.
    assert model.counter == 5

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch_neg(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch_neg(10)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"



def test_branchzero():  # ests branch on negative, positive, and zero values of accumulator.  Also checks branch is within memory bound.
    model = uvsim.UVSim()   
    model.program = [1,2,3,4,5,6,7,8,9,10]
    model.accumulator = 0
    model._branch_zero(5)   # Will change counter to location 5 as accumulator is zero. 
    assert model.counter == 5

    model.accumulator = 5
    model._branch_zero(6)  # Will not change counter to location 6 as accumulator is not zero.
    assert model.counter == 5

    model.accumulator = -5  
    model._branch_zero(7)   # Will not change counter to location 7 as accumulator is not zero. 
    assert model.counter == 5

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch_zero(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch_zero(10)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"

# def test_halt():
#     model = uvsim.UVSim()
#     model.program = [1,2,3,4,5]