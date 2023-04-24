`timescale 1ns / 1ps 

module Register16_8(R_Addr, W_Addr, R_en, W_en, R_Data, W_Data, Clk, Rst);

   input [3:0] R_Addr, W_Addr;
   input R_en, W_en;
   output reg [7:0] R_Data;
   input [7:0] W_Data;
   input Clk, Rst;
   
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
