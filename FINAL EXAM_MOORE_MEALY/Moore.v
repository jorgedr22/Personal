module Moore (b,x,Rst,Clk);
    input b,Rst,Clk;
    output reg x;

    parameter [2:0] s0=0,s1=1,s2=2,s3=3;
    reg [2:0] state;

    always @(posedge CLK) 
    begin
        if(Rst) begin
            x <= 0;
            state <= s0;
        end
        else sta
        begin
            case(state)
                s0:begin
                    x <= 0;
                    if(b) state <= s1;
                    else state <= s0;
                end
                s1:begin
                    if (~b) state <= s2;
                    else state <= s1;
                end
                s2:begin
                    if (b) state <= s3;
                    else state <= s0;
                end
                s3:begin
                    x <= 1;
                    if (b) state <= s1;
                    else state <= s0;
                end
            endcase
        end
    end



endmodule