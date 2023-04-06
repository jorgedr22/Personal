`timescale 1ns / 1ps

//7-bit 2x1 multiplexor
//if s = 1, D = I1
//else, D = I0

module mux(s, I1, I0, D);
    input [6:0] I1, I0;
    input s;
    output reg [6:0] D;
    
    always @ (s,I0,I1) begin
        if (s) begin
            D = I1;
        end
        else begin
            D = I0;
        end
    end

endmodule
