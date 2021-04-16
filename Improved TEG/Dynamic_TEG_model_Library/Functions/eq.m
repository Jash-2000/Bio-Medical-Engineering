syms KT Kh Kc Texh Tcol P_outs x y 
[x,y]=solve(Kh*(Texh-x)-KT*(x-y)-P_outs, P_outs-Kh*(Texh-x)+Kc*(y-Tcol),x,y);