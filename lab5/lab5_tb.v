`timescale 1ns / 1ps
`include "Adder_6bits.v"
`include "Adder_12bits.v"
`include "Comparator_6bits.v"
`include "Comparator_8bits.v"
`include "Controller.v"
`include "mux8bits_2x1.v"
`include "RegFile_32x8.v"
`include "Register_6bits.v"
`include "Register_8bits.v"
`include "Register_12bits.v"
`include "Subtractor_8bits.v"

module lab5_tb;
    reg Clk, Rst, go;
    wire [11:0] sum;
    wire done;
    
    
    lab5 a1(Clk, Rst, go, sum, done);
    
    always 
    begin
        Clk <= 0;
        #100;
        Clk <= 1;
        #100;
    end
    
    initial
    begin
        $dumpfile("lab5_tb.vcd");
        $dumpvars(0,lab5_tb);

        Rst <= 1'b1; go <= 0;
        @ (posedge Clk);
        #50 Rst <= 1'b0; 
        @ (posedge Clk);
        @ (posedge Clk);
        #50 go <= 1;
        @ (posedge Clk);
        #50 go <= 0;
    end
endmodule

