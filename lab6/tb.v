`timescale 1ns / 1ps

module tb();
    reg go, Clk, Rst;
    wire [5:0] count; 
    wire done;
    wire temp2;
    
    Lab6 Lab6_1(go, count, done, Clk, Rst,temp2);
    
    always begin
    Clk <= 0;
    #200;
    Clk <= 1;
    #200;
    end
    
    initial begin
    go=0;Rst=1;
    @(posedge Clk);
    #50; Rst=0;
    #50;
    go=1;
    @(posedge Clk);
    #50;
    go=0;
    end

    
endmodule
