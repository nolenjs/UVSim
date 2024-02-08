import pytest
import uvsim
from unittest.mock import patch

'''
TODO
Valid Input: Test multiple valid input arguments, include different opcodes
'''
@pytest.fixture
def model():
    return uvsim.UVSim()

# Test Initialization
def test_initialization():  #1 Test Initilization of object.
    with open("program.txt","w") as f:
         f.write("1005\n")
         f.write("1105\n")
         f.write("2005\n")
         f.write("4207\n")
         f.write("4009\n")

    model = uvsim.UVSim()
    assert model.counter == 0
    assert model.accumulator == 0
    assert model.program == ["1005","1105","2005","4207","4009"]


# Test Run: Valid Input
def test_valid_input(): #2
    model = uvsim.UVSim()
    program = ["1000", "1100", "1001","1101","2000","3001","2102", "1102" ,"4300"]   # Valid Input
    with patch('builtins.input', side_effect=["-0001","-0020"]):
        model.program = program
        result = model.run() # Program ran to completion and terminated at halt instruction
        assert result == True # Halt instruction returns True

# Test Run: Invalid Input
def test_invalid_input():   #3 Tests invalid input
    model = uvsim.UVSim()
    model.program = ["1100", "2100", "4ha3"]    # Invalid Input
    try:
        model.run() # If input is invalid while running code, the program will raise a syntax error
    except SyntaxError as e:
        assert str(e) == 'Invalid Operation'


# Test Run: Halt
def test_halt(): #4
    model = uvsim.UVSim()
    model.program = ["4300"]
    result = model.run()
    assert result == True   # If halt instruciton is reached, program will return True


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
    with patch('builtins.input', side_effect=["1234"]):
        model.program = ["1","2","3","4","5","6"]
        result = model._read(5)
        assert result == "1234"

        assert model.program[5] == "1234"

def test_read_2(model): #9 Memory bound check
    with patch("builtins.input", side_effects=['-6789']): # all invalid input will be ignored
        model.program = ["1","2","3","4","5","6"]
        
        try:
            model._read(10)
        except IndexError as e:
            assert str(e) == "Location Index out of range"

        try:
            model._read(-20)
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


def test_subtract():    #15 Test subtraction function and bounds check
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"]
    model.accumulator = 10
    model._subtract(2)  # This will subtract the value at memory location 2 (3) from the value in accumulaotr (10) and store result (7) in accumulator
    assert model.accumulator == 7

    try:                # Under bound check, memory at location -2 doesn't exist
        model._subtract(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._subtract(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


def test_multiply():       #16 Test Multiply function and bounds check
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","5"]
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


def test_divide():      #17 Test Divide function, integer division, division by 0, and bounds check
    model = uvsim.UVSim()
    model.program = ["1","2","3","4","0"]

    model.accumulator = 10
    model._divide(1)    # Divides accumulator (10) by memory location 1 (2). Stores result (2) in accumulator
    assert model.accumulator == 5

    model.accumulator = 10
    model._divide(2)    # Divides accumulator (10) by memory location 2 (3). Stores integer division result (3) in accumulator
    assert model.accumulator == 3



    model.accumulator = 10
    try:
        model._divide(4) # Divides accumulator (10) by memory location 4 (0). Should raise an error, divison by 0 is impossible
    except ValueError as e:
        assert str(e) == "Divide by Zero"

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._divide(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"

    try:            
        model._divide(5)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"


# Test Control Operations
def test_branch():  #18 Tests branch to location 8. Also makes sure branch is within memory bound.
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]
    model._branch(8)    # Changes program counter to branch location 8
    assert model.counter == 8   

def test_branch_bound(): #19
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch(10)     # Over bound check, memory at location 10 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"



def test_branchneg():   #20 Tests branch on negative, positive, and zero values of accumulator. Also checks branch is within memory bound.
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

def test_branchneg_bound(): #21
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch_neg(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch_neg(10)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"




def test_branchzero():  #22 ests branch on negative, positive, and zero values of accumulator.  Also checks branch is within memory bound.
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]
    model.accumulator = 0
    model._branch_zero(5)   # Will change counter to location 6 as accumulator is zero. 
    assert model.counter == 5

    model.accumulator = 5
    model._branch_zero(6)  # Will not change counter to location 6 as accumulator is not zero.
    assert model.counter == 5

    model.accumulator = -5  
    model._branch_zero(7)   # Will not change counter to location 7 as accumulator is not zero. 
    assert model.counter == 5


def test_branchzero_bound(): #23
    model = uvsim.UVSim()
    model.program = [1,2,3,4,5,6,7,8,9,10]

    try:                # Under bound check, memory at locatoin -2 doesn't exist
        model._branch_zero(-2)
    except IndexError as e:
        assert str(e) == "Location Index out of range"
    
    try:            
        model._branch_zero(10)     # Over bound check, memory at location 5 doesn't exist
    except IndexError as e:
        assert str(e) == "Location Index out of range"
