timescale 1ns/1ps

module EX3 (go,done,min,sum,Clk,Rst);
    input go, CLK, Rst;
    output reg done;
    output reg [8:0] min, sum;

    localparam [3:0] = s0=0,s1=1,s2=2,s3=3,s4=4,s5=5,s6=6;

    reg [3:0] state;
    reg [7:0] temp;
    reg W_en,R_en;
    reg [4:0] i;
    reg [7:0] W_Data,R_Data;

    Register16_8 A1(i, i, R_en, W_en, R_Data, W_Data, Clk, Rst);

    always @(posedge Clk) begin
        if(Rst)begin
            state <= s0;
        end
        else 
            case(state)
                s0:
                    if (go) state <= s1;
                    else state <= s0;
                s1:
                    W_en <= 0;
                    R_en <= 0;
                    if (i<16) state <= s2;
                    else state <= s6;
                s2:
                    R_en <= 1;
                    if (temp<min) state <= s3;
                    else if (temp > 128) || (temp == 128) state <= s4;
                    else state <= s5;
                s3:
                    if(temp > 128) || (temp == 128) state <= s4;
                    else state <= s5;
                s4:
                    W_en <= 1;
                    state <= s5;
                s5:
                    state <= s1;
                s6:
                    done <= 1;
            endcase
    end

    always @(*) begin
        case (state)
            s0:
                done <= 0;
                sum <= 0;
                min <= 255
                i <= 0;
            s2:
                temp = R_Data;
            s3:
                min = temp;
            s4:
                R_Data = temp - 128;
            s5:
                sum = sum + temp;
                i = i + 1; 
            s6:
                done <= 1;

        endcase
    end





endmodule