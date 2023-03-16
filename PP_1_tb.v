`timescale 1ns / 1ps
module PP_1_tb();
reg x,y,Rst,Clk;
wire q;

always begin
        Clk <= 0;
        #100;
        Clk <= 1;
        #100;
    end

PP_1 tb(x,y,Rst,Clk,q);

initial 
begin
    Rst<=1;x<=0;y<=0;
    //traverse SA->SB->SC->SD
    @(posedge Clk);
    #50 Rst<=0;x<=1;y<=0;
    
    @(posedge Clk);
    #50 x<=0;y<=1;
    
    @(posedge Clk); 
    #50 x<=0;y<=0;


end

endmodule
