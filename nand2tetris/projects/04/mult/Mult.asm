// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

    // initialize counter
    @counter
    M=0

    // initialize product
    @R2
    M=0

    // is (R0 == 0)?
    @R0
    D=M
    @END
    D;JEQ

(LOOP)
    // check loop condition (counter >= R1)
    // this also tests (R1 == 0)
    @counter
    D=M
    @R1
    D=M-D    // (R1 - counter)
    @END
    D;JLE

    @R0
    D=M
    @R2
    M=M+D
    @counter
    M=M+1

    // goto LOOP
    @LOOP
    0;JMP

(END)
    @END
    0;JMP