`timescale 1ps/1ps
`include "sample.v" 

module sample_tb();
    reg A,B,C;

    wire D,E;

    sample uut(A,B,C,D,E);

    initial begin
        $dumpfile("sample_tb.vcd");
        $dumpvars(0,sample_tb);

        A=0;
        B=0;
        C=0;
        #50

        A=1;
        B=1;
        C=1;
        #100

        A=0;
        B=0;
        C=0;
        #50

        $display("Test complete");

    end    
endmodule