module PP_3(w,z,Rst,Clk);
    input w,Rst,Clk;
    output reg z;

    reg [7:0]State;
    localparam[3:0] = s0=0,s1=1,s2=2,s3=3,s4=4,s5=5,s6=6,s7=7;

always @(posedge Clk) begin
    if (Rst) begin
        State=s0;
        z=0;
    end
    else begin
        case (State)
            s0:begin
                if (w) begin
                    State=s1;
                end
                else if (~w) begin
                    State=s0;
                end
            end

            s1:begin
                if (~w) begin
                    State=s2;
                end
                else if (w) begin
                    State=s5;
                end
            end 

            s2:begin
                
            end

            s3:begin
                
            end

            s4:begin
                
            end

            s5:begin
                
            end

            s6:begin
                
            end

            s7:begin
                
            end

            default: 
        endcase
    end
end












endmodule