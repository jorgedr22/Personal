module Lab6_toplevel (CLK100MHZ, BTNU, LED, CA, CB, CC, CD, CE, CF, CG, AN);
    input CLK100MHZ;
    input BTNU; //BTNU is Reset
    output [0:0] LED; //LED[0] is done
    output CA, CB, CC, CD, CE, CF, CG; //segment a, b, ... g
    output [7:0] AN;  //enable each digit of the 8 digits
    //write your code to connect the modules as shown in Figure 1 (page 3)
    
    (* mark_debug = "true" *) wire [7:0] debug_Reg0;
    (* mark_debug = "true" *) wire [7:0] debug_Reg1;
    (* mark_debug = "true" *) wire [7:0] debug_Reg2;
    (* mark_debug = "true" *) wire [7:0] debug_Reg3;
    (* mark_debug = "true" *) wire [7:0] debug_Reg4;
    (* mark_debug = "true" *) wire [7:0] debug_Reg5;
    (* mark_debug = "true" *) wire [7:0] debug_Reg6;
    (* mark_debug = "true" *) wire [7:0] debug_Reg7;
    (* mark_debug = "true" *) wire [7:0] debug_Reg8;
    (* mark_debug = "true" *) wire [7:0] debug_Reg9;
    (* mark_debug = "true" *) wire [7:0] debug_Reg10;
    (* mark_debug = "true" *) wire [7:0] debug_Reg11;
    (* mark_debug = "true" *) wire [7:0] debug_Reg12;
    (* mark_debug = "true" *) wire [7:0] debug_Reg13;
    (* mark_debug = "true" *) wire [7:0] debug_Reg14;
    (* mark_debug = "true" *) wire [7:0] debug_Reg15;


    mux a2(LED, temp2, count, D);
    ClkDiv a3(CLK100MHZ,0,ClkOut);
    TwoDigitDisplay a4(CLK100MHZ,D,CA,CB,CC,CD,CE,CF,CG,AN);
    Lab6 a5(1, count, LED, ClkOut, BTNU, temp2);
    
endmodule