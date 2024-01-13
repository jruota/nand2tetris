# Quote from the book:
#   The Parser encapsulates access to the input assembly code. In particular,
#   it provides a convenient means for advancing through the source code,
#   skipping comments and white space, and breaking each symbolic instruction
#   into its underlying components.

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
        else:
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
        # print("\tin comp() -> " + str(c_instruction_parts))
        if (len(c_instruction_parts) > 1):
            # print("\tin comp() -> " + str(c_instruction_parts[1].split(";")[0]))
            return c_instruction_parts[1].split(";")[0]
        else:
            return c_instruction_parts[0].split(";")[0]
        
    def jump():
        c_instruction_parts = line.split(";")
        if (len(c_instruction_parts) > 1):
            return c_instruction_parts[1]
        else:
            return ""
 
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
            # print("symbol -> " + instruction)
        if (instruction_type == C_INSTRUCTION):
            destination, computation, jump_to = dest(), comp(), jump()
            # print("dest -> " + destination)
            # print("comp -> " + computation)
            # print("jump -> " + jump_to) 
            
################################################################################
        
if __name__ == "__main__":
    hack_parser(open("./add/Add.asm", "r"))
    print()
    hack_parser(open("./max/MaxL.asm", "r"))
    print()
    hack_parser(open("./max/Max.asm", "r"))
    print()
    hack_parser(open("./rect/RectL.asm", "r"))
    print()
    print("RECT " + 10 * "-")
    hack_parser(open("./rect/Rect.asm", "r"))
