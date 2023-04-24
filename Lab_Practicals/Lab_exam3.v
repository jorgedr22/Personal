`timescale 1ns / 1ps

module EX3 (go,done,min,sum,Clk,Rst);
    input go, Clk, Rst;
    output reg done;
    output reg [7:0] min;
    output reg [12:0]sum;

    localparam [3:0] s0=0,s1=1,s2=2,s3=3,s4=4,s5=5,s6=6;

    reg [3:0] state;
    reg [7:0] temp;
    reg W_en,R_en;
    reg [3:0] i;
    reg [7:0] W_Data;
    wire [7:0] R_Data;

    Register16_8 A1(i, i, R_en, W_en, R_Data, W_Data, Clk, Rst);

    always @(posedge Clk) begin
        if(Rst)begin
            state <= s0;
        end
        else begin
            case(state)
                s0:begin
                    done <= 0;
                    sum <= 0;
                    min <= 255;
                    i <= 0;
                    W_en <= 0;
                    R_en <= 0;
                    if (go) state <= s1;
                    else state <= s0;
                end
                s1:begin
                    if (i<16) begin
                        R_en <= 1;
                        state <= s2;
                    end
                    else state <= s6;
                end    
                s2:begin
                    temp <= R_Data;
                    if (temp < min) begin
                    state <= s3;
                    end
                    else if (temp >= 128) begin
                    W_en <= 1;
                    state <= s4;
                    end
                    else state <= s5;
                end
                s3:begin
                    if (temp >= 128) begin
                    W_en <= 1;
                    min <= temp;
                    state <= s4;
                    end
                    else state <= s5;
                end
                s4:begin
                    W_Data <= (temp - 128);
                    state <= s5;
                end
                s5:begin
                    sum <= (sum + temp);
                    i <= i + 1;
                    state <= s1;
                end
                s6:
                    done <= 1;
                default:
                    state <= s0;
            endcase
       end
    end

//    always @* begin
//        case (state)
//            s0:begin
//                done <= 0;
//                sum <= 0;
//                min <= 255;
//                i <= 0;
//            end
//            s2:
//                temp <= R_Data;
//            s3:
//                min <= temp;
//            s4:
//                W_Data <= (temp - 128);
//            s5:begin
//                sum <= (sum + temp);
//                i <= i + 1; 
//            end
//            s6:
//                done <= 1;
//        endcase
//    end

endmodule
