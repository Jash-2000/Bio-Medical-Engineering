clear all
load test1
%% TEG geometrical parameters
l=1e-3; % l is the thermoelectric leg length, m
l_cw=1.5e-3;% l_cw is the length of ceramic wafer, m
l_TEM=l+2*l_cw;% l_l_TEM is the height of a TEM, m
f=2*127*0.0028*0.0028/(0.062*0.062); % f is the fill factor -
a=0.062*0.062; % a is the area of a TEM, m2.
n=127;% n is the pair of legs
M=1;% N is the numner of TEMs in a CV
side=2;% side is the number of heat exchanger channel
B=0.213*0.1143/2;% B is the area of a CV m2

%% Hot side heat exchanger parameters
M_hxr=0.16128;% M_hxr is the mass of the hot side heat exchanger, kg
C_hxr=500;% C_hxr is the heat capacity of the hot side heat exchanger,J/(kg,K)
M_ap=0.024066;% M_ap is the mass of the aluminate plate, kg
C_ap=900;% C_ap is the heat capacity of the aluminate plate,J/(kg,K)
l_hxr=0.213/2; % Length of the channel [m]
b_hxr=0.1143; % Width of the channel [m]
a_hxr=0.0127;% Height of the channel [m]
Nf_hxr=13*4.5; % Number of fins
tf_hxr=0.00032;% Fin thickness [m]

%% Cold side heat exchanger parameters
M_cxr=1.5045;% M_cxr is the mass of the cold side heat exchanger, kg
C_cxr =950; % C_cxr is the heat capacity of the cold side heat exchanger, J/(kg,K)
Di_cxr=2*0.0889*(0.01-2*0.0015)/(0.0889+0.01-2*0.0015); % Width of the channel [m]

%% Opertional parameters
 
T_cint = 286;
T_hint = 306.64;
r_int=0.5;
%% Tuning parameters
%TEM
Tune_tr =1;
ct1 = 6.3195; 
ct2 = -5.337;
Tune_er=0.5;

%HXR
ca1 = 0.99971;
ca2 = 0.00021632;
ca3 = 0.33723;
    

cb1 = 0.023;
cb2 = 0.8;
cb3 = 0.33;


%% material parameters
load N
load P
%Format for P and N is as follow:
%Temperature(K), Seeback coefficient(V/K), Electrical resistance (ohm.m), Thermal conductivity (W/m.K)
