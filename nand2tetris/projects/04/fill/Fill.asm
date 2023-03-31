// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// initialize current screen address
@SCREEN
D=A
@screenaddress
M=D

// main loop
(MAIN)
    @KBD
    D=M

    // no key pressed
    @WHITE
    D;JEQ

    // any key pressed
    @BLACK
    D;JGT

// turn pixels white
(WHITE)
    // set current screen address to white
    @screenaddress
    A=M
    M=0

    // update screenaddress
    @screenaddress
    D=M-1
    @SCREEN
    D=D-A

    // outside of screen map?
    @SETTOSTART
    D;JLT
    // else
    @screenaddress
    M=M-1

    // back to main loop
    @MAIN
    0;JMP

// turn pixels black
(BLACK)
    // set current screen address to black
    @screenaddress
    A=M
    M=-1

    // update screenaddress
    @screenaddress
    D=M+1
    @SCREEN
    D=D-A
    @8191 // 256 rows * 32 rows of 16-bit words, subtract 1 (@SCREEN first addr)
    D=D-A

    // outside of screen map?
    @SETTOEND
    D;JGT
    // else
    @screenaddress
    M=M+1

    // back to main loop
    @MAIN
    0;JMP

(SETTOSTART)
    @SCREEN
    D=A
    @screenaddress
    M=D

    // back to main loop
    @MAIN
    0;JMP

(SETTOEND)
    @SCREEN
    D=A
    @8191 // 256 rows * 32 rows of 16-bit words, subtract 1 (@SCREEN first addr)
    D=D+A
    @screenaddress
    M=D

    // back to main loop
    @MAIN
    0;JMP