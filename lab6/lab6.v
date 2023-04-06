`timescale 1ns / 1ps

module Lab6(go, count, done, Clk, Rst, temp2);
    input go, Clk , Rst;
    output reg [5:0] count;
    output reg done;
    output reg [6:0] temp2;
    reg [7:0] temp, W_data;
    reg R_en,W_en;
    reg [13:0] k;
    reg [3:0]i;
    wire [7:0] R_data;
  
   parameter [3:0] s1=1, 
                   s2=2, 
                   s3=3, 
                   s4=4, 
                   s5=5, 
                   s6=6, 
                   s_done= 7,
                   s_wait= 8,
                   s_disp = 9,
                   s_wait2 = 10,
                   s_disp2 = 11,
                   s_disp_done = 12;
    
    reg [3:0]state;
    
    RegFile16x8 a1(i, i, 1, W_en, R_data, W_data, Clk, Rst);

    always @(posedge Clk) begin
        if(Rst) begin
            state = s1;
        end
        else begin
            case(state)
                s1: begin
                    i = 0;
                    count = 0;
                    k = 0;
                    if(go) begin
                        state = s2;
                    end
                    else begin
                        state = s1;
                    end
                end      
                          
                s2: begin
                    if (i < 16) begin
                        if(count==8)begin
                            state = s_done;
                        end
                        else begin
                        state = s3;
                        end
                    end
                end                        
                s3: begin
                    temp = R_data;
                    temp2 = R_data;
                    state = s4;
                end            
                    
                s4: begin
                    if((temp > 47) && (temp < 58)) begin
                        state = s5;
                    end
                    else begin
                        state = s6;
                    end
                end 
                               
                s5: begin
                    W_data = temp - 48;
                    count = count + 1;
                    temp2 = W_data;
                    state = s6;
                end 
                               
                s6: begin
                    i = i + 1;
                    state = s2;
                end            
                    
                s_disp: begin
                    k = 0;
                    state = s_wait2;
                end 
                s_done: begin
                    i = 0;
                    k = 0;
                    state = s_wait;
                end
                s_wait: begin
                    k = k + 1;
                    if(k < 10000) begin
                        state = s_wait;
                    end
                    else begin
                        state = s_disp;
                    end
                end
                s_wait2: begin
                    k = k + 1;
                    if (k < 10000) begin
                        state = s_wait2;
                    end
                    else begin
                        state = s_disp2;
                    end
                end
                s_disp2: begin
                    i = i + 1;
                    k = 0;
                    if(i < 14) begin
                        state = s_wait2;
                    end
                    else begin
                        state = s_disp_done;
                    end
                end
                s_disp_done: begin
                    state = s_disp_done;
                end
                default: begin
                    state = s1;
                end        
        endcase
     end
     
     end
     always@(*)begin
     case(state) 
           s1: begin;
               R_en = 1;
           end
           s2: begin
               done = 0;
           end
           s3: begin
           end   
           s4: begin
           end
           s5: begin
               W_en = 1;
           end
           s6: begin
               W_en = 0;
           end
           s_done: begin
               done = 0;         
           end
           s_wait: begin
               done = 0;
           end
           s_disp: begin
               done = 1;
           end
           s_wait2: begin
               done = 1;
           end
           s_disp2: begin
               done = 1;
           end
           s_disp_done: begin
               done = 1;
           end
       endcase
  end   
endmodule
