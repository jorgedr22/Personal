module sample (A,B,C,D,E);

input A,B,C;
output D,E;

wire w1;
and g1(w1,A,B);
not g2(E,C);
or g3(D,w1,E);
    
endmodule