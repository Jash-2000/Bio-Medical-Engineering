function [ T1 ] = T1(  Rh,Rc,Th,Tc,RT,r_ints,I,Spn)

%T1_T2 Summary of this function goes here
%   Detailed explanation goes here

Kh=1/Rh;
Kc=1/Rc;
KT=1/RT;

y0=[Th;Tc];
options=optimset('Display','off');
[y,fval]=fsolve(@(y)[Kh*(Th-y(1))-KT*(y(1)-y(2))-Spn*y(1)*I+0.5*I^2*r_ints...
     Spn*(y(1)-y(2))*I-I^2*r_ints-Kh*(Th-y(1))+Kc*(y(2)-Tc)],y0,options);
T1=y(1); %K
T2=y(2); %K
dT=T1-T2; %K
 
 
end
