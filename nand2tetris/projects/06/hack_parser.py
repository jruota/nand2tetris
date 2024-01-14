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

    def hasMoreLines():
        # This function has no use, as Python handles reading files with a for
        # loop.
        return False
    
    def advance():
        # This function has no use, as Python handles reading files with a for
        # loop.
        return
    
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

    # loop over input file
    for line in inputf:
        # remove (inline) comments
        line = line.split("//")[0]
        # remove leading and trailing whitespace
        line = line.strip()
        # ignore empty lines - comments have already been removed
        if (len(line) == 0):
            continue

        instruction_type = instructionType()
        if (instruction_type == A_INSTRUCTION or 
            instruction_type == L_INSTRUCTION):
            instruction = symbol()
            if (instruction.isdecimal()):
                outputf.write(
                    "0" + 
                    format(int(instruction), "015b") + 
                    "\n")
        if (instruction_type == C_INSTRUCTION):
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
