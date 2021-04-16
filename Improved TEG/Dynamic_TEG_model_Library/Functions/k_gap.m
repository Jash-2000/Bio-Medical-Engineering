function [ k_gap ] = k_gap( T_hm,T_cm,ka,v,alpha,Pr,Beta,l,a,f )

eps=2/3; %emissivity 
sb=5.67E-8; %W/m^2-K^4
g=9.81; %m/s^2

%%calculate the air gap (conductance & radiation) 
VF=(sqrt(1+l.^2/a)-l/sqrt(a)).^2;
Krad=4*sb*VF*((T_hm+T_cm)/2)^3/(2*(1-eps)/eps+1./VF)*(1-f)*a;
Kcond=ka*a*(1-f)./l;
Ra=g*Beta*(T_hm-T_cm)*l.^3/(v*alpha);
    if Ra>1708
        Kcon=ka*a*(1-f)./l*(0.069*Ra.^(1/3)*Pr^0.074);
    else
        Kcon=Kcond;
    end
    
k_gap=Kcon+Krad; % thermal conductance of TEM + air gap W/K


end


