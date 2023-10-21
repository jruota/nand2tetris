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
    // initialization
    @SCREEN
    D=A
    // NOTE: always make sure that 16384 <= word <= 24575 to avoid addressing
    //       memory outside the screen-map
    @word // address of current 16-bit word of screen map
    M=D
    @8191 // 256*32-1 -> rows*columns-1 where column 32 16-bit words
    D=D+A
    @maxword // last 16-bit word in the screen-map
    M=D
(MAIN)
    @KBD
    D=M
    @BLACKEN
    D;JGT
    @WHITEN
    D;JEQ
    @MAIN
    0;JMP
(BLACKEN)
    @word
    A=M
    M=-1
    @maxword
    D=M
    @word
    D=D-M
    @MAIN
    D;JEQ
    @word
    M=M+1
    @MAIN
    0;JMP
(WHITEN)
    @word
    A=M
    M=0
    @word
    D=M
    @SCREEN
    D=D-A
    @MAIN
    D;JEQ
    @word
    M=M-1
    @MAIN
    0;JMP
