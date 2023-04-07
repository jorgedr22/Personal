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
                   s6=6,
                   s7=7; 

    
    reg [3:0] state;
    reg [7:0] temp;
    reg  W_en;
    reg [7:0] W_data;
    reg [3:0] i;

    
    RegFile16x8 a1(i, i, 1, W_en, R_data, W_data, Clk, Rst);

    always @(posedge Clk) begin
        if(Rst) begin
            state = s0; // run a while loop to read all the values of the register before going to s0?
        end
        else begin
            case(state)
            s0: begin
                if(~go)begin
                    state = s0;
                end
                else if(go) begin
                    state = s1;
                end
            end
            s1: begin
                state = s2;
            end
            s2: begin
                if(i<16)begin
                    state = s3;
                end
                else if(~(i<16))begin
                    state = s7;
                end
            end            
            s3: begin
                if(temp>47)begin
                    state = s4;
                end
                else if(~(temp>47))begin 
                    state = s6;
                end
            end            
            s4: begin
                if(temp<58)begin
                    state = s5;
                end
                else if(~(temp<58))begin
                    state = s6;
                end
            end
            s5: begin
                state = s6;
            end            
            s6: begin
                state = s2;
            end             
            s7: begin
                state = s0;
            end                   
        endcase
    end
end

    always @(*) begin
            case(state)
            s0: begin        
            end
            s1: begin
                done = 0;
                sum = 0;
                i = 0; 
            end
            s2: begin
            end            
            s3: begin
                temp = R_data;
                data = R_data;
            end            
            s4: begin
            end
            s5: begin
               W_en = 1;
               W_data = (temp - 48); 
               sum = (sum + W_data);
            end            
            s6: begin
               W_en = 0;            
               i = i + 1;
            end             
            s7: begin
                done = 1;
            end                   
        endcase
    end    
endmodule
