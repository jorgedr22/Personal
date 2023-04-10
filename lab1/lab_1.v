`timescale 1ns / 1ps

module lab1(A, B, C, D, I0, I1, I2);
    input A, B, C, D;
    output reg I0, I1, I2;
    
    always @ (A, B, C, D)
        begin 
        // I0 <= ~A & ~B & ~C & D | ~A & ~B & C & ~D | ~A & B & ~C & ~D | ~A & B & C & D | A & ~B & ~C & ~D | A & ~B & C & D | A & B & ~C & D |A & B & C & ~D;

        I0 <= A^B^C^D;

        I1 <= ~A & ~B & C & D | ~A & B & ~C & D | ~A & B & C & ~D | ~A & B & C & D | A & ~B & ~C & D | A & ~B & C & ~D | A & ~B & C & D | A & B & ~C & ~D | A & B & ~C & D | A & B & C & ~D ;

        I2 <= A & B & C & D; 
    end
endmodule
