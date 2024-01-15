# Quote from the book:
#   The Parser encapsulates access to the input assembly code. In particular,
#   it provides a convenient means for advancing through the source code,
#   skipping comments and white space, and breaking each symbolic instruction
#   into its underlying components.

import os

import hack_code

def hack_parser(inputf):
    # constants
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2

     # symbol table
    symbol_table = {
        "R0":           0,
        "R1":           1,
        "R2":           2,
        "R3":           3,
        "R4":           4,
        "R5":           5,
        "R6":           6,
        "R7":           7,
        "R8":           8,
        "R9":           9,
        "R10":         10,
        "R11":         11,
        "R12":         12,
        "R13":         13,
        "R14":         14,
        "R15":         15,
        "SP":           0,
        "LCL":          1,
        "ARG":          2,
        "THIS":         3,
        "THAT":         4,
        "SCREEN":   16384,
        "KBD":      24576,
        }

    def hasMoreLines():
        # This function has no use, as Python handles reading files with a for
        # loop.
        return False
    
    def advance():
        nonlocal line
        # remove (inline) comments
        line = line.split("//")[0]
        # remove leading and trailing whitespace
        line = line.strip()
    
    def instructionType():
        if (line.startswith("@")):
            return A_INSTRUCTION
        if (line.startswith("(") and line.endswith(")")):
            return L_INSTRUCTION
        return C_INSTRUCTION
        
    def symbol():
        return line.strip("()@")
    
    def dest():
        c_instruction_parts = line.split("=")
        if (len(c_instruction_parts) > 1):
            return c_instruction_parts[0]
        else:
            return ""
    
    def comp():
        c_instruction_parts = line.split("=")
        if (len(c_instruction_parts) > 1):
            return c_instruction_parts[1].split(";")[0]
        else:
            return c_instruction_parts[0].split(";")[0]
        
    def jump():
        c_instruction_parts = line.split(";")
        if (len(c_instruction_parts) > 1):
            return c_instruction_parts[1]
        else:
            return ""
 
    # open output file to write translated binary instructions
    outputf = open(
        os.path.abspath(inputf.name).split(".")[0] + "1" + ".hack",
        "w")

    # loop over input file - FIRST PASS
    line_number = 0
    for line in inputf:
        advance()
        # ignore empty lines - comments have already been removed
        if (len(line) == 0):
            continue

        instruction_type = instructionType()
        if (instruction_type == A_INSTRUCTION or
            instruction_type == C_INSTRUCTION):
            line_number += 1
        elif (instruction_type == L_INSTRUCTION):
            instruction = symbol()
            symbol_table[instruction] = line_number

    # loop over input file - SECOND PASS
    variable_index = 16
    inputf.seek(0)  # go back to the start of the file
    for line in inputf:
        advance()
        if(len(line) == 0):
            continue

        instruction_type = instructionType()
        if (instruction_type == L_INSTRUCTION):
            continue
        elif (instruction_type == A_INSTRUCTION):
            instruction = symbol()
            if (instruction.isdecimal()):
                outputf.write(
                    "0" + 
                    format(int(instruction), "015b") + 
                    "\n")
            else:
                if (not instruction in symbol_table):
                    symbol_table[instruction] = variable_index
                    variable_index += 1
                outputf.write(
                    "0" +
                    format(int(symbol_table[instruction]), "015b") +
                    "\n")
        elif (instruction_type == C_INSTRUCTION):
            computation, destination, jump_to = comp(), dest(), jump()
            outputf.write(
                "111" + 
                hack_code.hack_code(computation, destination, jump_to) + 
                "\n")

    # close output file
    outputf.close()
            
################################################################################
        
if __name__ == "__main__":
    print("ADD " + 10 * "-")
    hack_parser(open("./add/Add.asm", "r"))
    print()
    print("MAXL " + 10 * "-")
    hack_parser(open("./max/MaxL.asm", "r"))
    print()
    print("MAX " + 10 * "-")
    hack_parser(open("./max/Max.asm", "r"))
    print()
    print("RECTL " + 10 * "-")
    hack_parser(open("./rect/RectL.asm", "r"))
    print()
    print("RECT " + 10 * "-")
    hack_parser(open("./rect/Rect.asm", "r"))
    print()
    print("PONGL " + 10 * "-")
    hack_parser(open("./pong/PongL.asm", "r"))
    print()
    print("PONG " + 10 * "-")
    hack_parser(open("./pong/Pong.asm", "r"))
