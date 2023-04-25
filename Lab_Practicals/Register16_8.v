`timescale 1ns / 1ps 

module Register16_8(R_Addr, W_Addr, R_en, W_en, R_Data, W_Data, Clk, Rst,debug_Reg0,debug_Reg1,debug_Reg2,debug_Reg3,debug_Reg4,debug_Reg5,debug_Reg6,debug_Reg7,debug_Reg8,debug_Reg9,debug_Reg10,debug_Reg11,debug_Reg12,debug_Reg13,debug_Reg14,debug_Reg15);

   input [3:0] R_Addr, W_Addr;
   input R_en, W_en;
   output reg [7:0] R_Data;
   input [7:0] W_Data;
   input Clk, Rst;
   
   output [7:0]debug_Reg0,debug_Reg1,debug_Reg2,debug_Reg3,debug_Reg4,debug_Reg5,debug_Reg6,debug_Reg7,debug_Reg8,debug_Reg9,debug_Reg10,debug_Reg11,debug_Reg12,debug_Reg13,debug_Reg14,debug_Reg15;
   
    (* mark_debug = "true" *) reg [7:0] RegFile [0:15];
    assign debug_Reg0 = RegFile[0];
    assign debug_Reg1 = RegFile[1];
    assign debug_Reg2 = RegFile[2];
    assign debug_Reg3 = RegFile[3];
    assign debug_Reg4 = RegFile[4];
    assign debug_Reg5 = RegFile[5];
    assign debug_Reg6 = RegFile[6];
    assign debug_Reg7 = RegFile[7];
    assign debug_Reg8 = RegFile[8];
    assign debug_Reg9 = RegFile[9];
    assign debug_Reg10 = RegFile[10];
    assign debug_Reg11 = RegFile[11];
    assign debug_Reg12 = RegFile[12];
    assign debug_Reg13 = RegFile[13];
    assign debug_Reg14 = RegFile[14];
    assign debug_Reg15 = RegFile[15];
   
   reg [7:0] RegFile [0:15];
   //write procedure
   always @(posedge Clk) begin
      if (Rst==1) begin
          RegFile[0] = 8'd254;
          RegFile[1] = 8'd169;
          RegFile[2] = 8'd156;
          RegFile[3] = 8'd250;
          RegFile[4] = 8'd145;
          RegFile[5] = 8'd247;
          RegFile[6] = 8'd128;
          RegFile[7] = 8'd232;
          RegFile[8] = 8'd249;
          RegFile[9] = 8'd105;
          RegFile[10] = 8'd189;
          RegFile[11] = 8'd172;
          RegFile[12] = 8'd65;
          RegFile[13] = 8'd180;
          RegFile[14] = 8'd218;
          RegFile[15] = 8'd39;
      end
      else if (W_en==1) begin
         RegFile[W_Addr] <= W_Data;
      end
   end
   // Read procedure
   always @* begin
      if (R_en==1)
         R_Data <= RegFile[R_Addr];
      else
         R_Data <= 32'hZZZZZZZZ;
   end
endmodule
