def hack_code(c, d, j):

    def comp():
        if (c.find("M") >= 0):
            a_bit = "1"
        else:
            a_bit = "0"

        if (c == "0"):
            comp_binary = "101010"
        elif (c == "1"):
            comp_binary = "111111"
        elif (c == "-1"):
            comp_binary = "111010"
        elif (c == "D"):
            comp_binary = "001100"
        elif (c == "A" or c == "M"):
            comp_binary = "110000"
        elif (c == "!D"):
            comp_binary = "001101"
        elif (c == "!A" or c == "!M"):
            comp_binary = "110001"
        elif (c == "-D"):
            comp_binary = "001111"
        elif (c == "-A" or c == "-M"):
            comp_binary = "110011"
        elif (c == "D+1"):
            comp_binary = "011111"
        elif (c == "A+1" or c == "M+1"):
            comp_binary = "110111"
        elif (c == "D-1"):
            comp_binary = "001110"
        elif (c == "A-1" or c == "M-1"):
            comp_binary = "110010"
        elif (c == "D+A" or c == "D+M"):
            comp_binary = "000010"
        elif (c == "D-A" or c == "D-M"):
            comp_binary = "010011"
        elif (c == "A-D" or c == "M-D"):
            comp_binary = "000111"
        elif (c == "D&A" or c == "D&M"):
            comp_binary = "000000"
        elif (c == "D|A" or c == "D|M"):
            comp_binary = "010101"           
        
        return a_bit + comp_binary

    def dest():
        if (d == ""):
            return "000"
        if (d == "M"): 
            return "001"
        if (d == "D"):
            return "010"
        if (d == "DM"):
            return "011"
        if (d == "A"):
            return "100"
        if (d == "AM"):
            return "101"
        if (d == "AD"):
            return "110"
        if (d == "ADM"):
            return "111"

    def jump():
        if (j == ""):
            return "000"
        if (j == "JGT"):
            return "001"
        if (j == "JEQ"):
            return "010"
        if (j == "JGE"):
            return "011"
        if (j == "JLT"):
            return "100"
        if (j == "JNE"):
            return "101"
        if (j == "JLE"):
            return "110"
        if (j == "JMP"):
            return "111"

    return comp() + dest() + jump()
