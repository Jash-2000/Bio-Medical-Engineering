function [ u_ocv ] = u_ocv( Rh,Rc,Th,Tc,RT,Spn,r_ints,R_load)

%T1_T2 Summary of this function goes here
%   Detailed explanation goes here

Kh=1/Rh;
Kc=1/Rc;
KT=1/RT;

y0=[Th;Tc];
options=optimset('Display','off');
[y,fval]=fsolve(@(y)[Kh*(Th-y(1))-KT*(y(1)-y(2))-Spn*y(1)*(Spn*(y(1)-y(2))/(R_load+r_ints))+0.5*(Spn*(y(1)-y(2))/(R_load+r_ints))^2*r_ints...
     Spn*(y(1)-y(2))*(Spn*(y(1)-y(2))/(R_load+r_ints))-(Spn*(y(1)-y(2))/(R_load+r_ints))^2*r_ints-Kh*(Th-y(1))+Kc*(y(2)-Tc)],y0,options);
T1=y(1); %K
T2=y(2); %K
dT=T1-T2; %K
u_ocv=Spn*dT;%V
end