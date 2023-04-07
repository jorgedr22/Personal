`timescale 1ns / 1ps

module RegFile16x8(R_Addr, W_Addr, R_en, W_en, R_Data, W_Data, Clk, Rst);
    input [3:0] R_Addr, W_Addr;
    input Clk, Rst, R_en, W_en;
    output reg [7:0] R_Data;
    input [7:0] W_Data;
    //simple memory declaration
    reg [7:0] RegFile [0:15];
    // Write procedure
    always @(posedge Clk) begin
            if (Rst == 1) begin
            RegFile[0] <= 8'd47;
            RegFile[1] <= 8'd56;
            RegFile[2] <= 8'd51;
            RegFile[3] <= 8'd48;
            RegFile[4] <= 8'd53;
            RegFile[5] <= 8'd55;
            RegFile[6] <= 8'd52;
            RegFile[7] <= 8'd39;
            RegFile[8] <= 8'd54;
            RegFile[9] <= 8'd49;
            RegFile[10] <= 8'd57;
            RegFile[11] <= 8'd50;
            RegFile[12] <= 8'd46;
            RegFile[13] <= 8'd53;
            RegFile[14] <= 8'd63;
            RegFile[15] <= 8'd57;
        end
            else if (W_en==1) begin
            RegFile[W_Addr] <= W_Data;
        end
end
// Read procedure
    always @(*) begin
        if (R_en==1)
        R_Data <= RegFile[R_Addr];
        else
        R_Data <= 8'bZZZZZZZZ;
    end
endmodule
