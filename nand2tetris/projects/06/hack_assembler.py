# Quote from the book:
#   This version of the assembler assumes that the source assembly code is
#   error-free. Error checking, reporting, and handling can be added to later
#   versions of the assembler but are not part of project 6.

import argparse
import os

import hack_parser

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

    # open input file containing assembly instructions
    inputf = open(args.fp, 'r')
    
    # loop over input file
    hack_parser.hack_parser(inputf)

    # close file
    inputf.close()
    return

################################################################################

if __name__ == "__main__":
    hack_assembler()
