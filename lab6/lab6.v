`timescale 1ns / 1ps

module Lab6(go, sum, data, done, Clk, Rst);
    input go, Clk , Rst;
    output reg [7:0] sum;
    output reg [7:0] data;
    output reg done;
    
    wire [7:0] R_data;
    
    
    parameter [3:0]s0=0,
                   s1=1, 
                   s2=2, 
                   s3=3, 
                   s4=4, 
                   s5=5, 
                   s6=6;

    
    reg [3:0] state;
    reg [7:0] temp;
    reg R_en, W_en;
    reg [7:0] W_data;
    integer i;

    
    RegFile16x8 a1(i, i, R_en, W_en, R_data, W_data, Clk, Rst,debug_Reg0,debug_Reg1,debug_Reg2,debug_Reg3,debug_Reg4,debug_Reg5,debug_Reg6,debug_Reg7,debug_Reg8,debug_Reg9,debug_Reg10,debug_Reg11,debug_Reg12,debug_Reg13,debug_Reg14,debug_Reg15);

    always @(posedge Clk) begin
        if(Rst) begin
            state <= s0;
        end
        else begin
            case(state)
            s0: begin
                if(~go)begin
                    state <= s0;
                end
                else if(go) begin
                    i <= 0;
                    done <= 0;
                    sum <= 0;
                    R_en <= 0;
                    W_en <= 0;
                    state <= s1;
                end
            end
            s1: begin
                if(i<16)begin
                    R_en <= 1;
                    state <= s2; 
                end
                else begin
                    done <= 1;
                    state <= 6;
                end
            end
            s2: begin
                temp <= R_data;
                state <= s3;
            end            
            s3: begin
                if ((temp>47) && (temp<58))begin
                    W_en <= 1;
                    R_en <= 0;
                    W_data <= (temp - 48);
                    state <= s4;
                end
                else if(~((temp>47) && (temp<58)))begin
                    state <= s5;
                end
            end            
            s4: begin
                sum <= sum + (temp - 48);
                data <= W_data;
                state <= s5;
            end
            s5: begin
                W_en <= 0;
                i <= i + 1;
                state <= s1;
            end            
            s6: begin
                done <=0;
                state <= s0;
            end                                
        endcase
    end
end

endmodule
