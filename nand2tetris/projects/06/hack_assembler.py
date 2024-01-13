# Quote from the book:
#    This version of the assembler assumes that the source assembly code is
#    error-free. Error checking, reporting, and handling can be added to later
#    versions of the assembler but are not part of project 6.

import argparse
import os

def hack_assembler():
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "fp", 
        help="File or file path to the file containing assembly instructions." +
             "Must end with '.asm' file extension.")
    args = parser.parse_args()
    
    # test if file ends with '.asm' file extension
    if (not args.fp.endswith(".asm", -4)):
        raise Warning("Filename must end in '.asm' file extension.")
        return

    # open input file containing assembly instructions
    inputf = open(args.fp, 'r')

    # open output file to write translated binary instructions
    outputf = open(
        os.path.dirname(args.fp) + 
        "/" + 
        os.path.basename(args.fp).split(".")[0] + 
        ".hack",
        "w")

    # close files
    inputf.close()
    outputf.close()
    return

################################################################################

if __name__ == "__main__":
    hack_assembler()
