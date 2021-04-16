clear all
%% TEM geometrical parameters
l=1e-3; % l is the thermoelectric leg length, m
l_cw=1.5e-3;% l_cw is the length of ceramic wafer, m
f=2*127*0.0028*0.0028/(0.062*0.062); % f is the fill factor -
a=0.062*0.062; % a is the area of a TEM, m2.
n=127;% n is the pair of legs
l_TEM=l+2*l_cw;% l_l_TEM is the height of a TEM,m

%% Opertional parameters
I=4.1; % I is the current, A
T_h1=396;
T_h2=381;
T_c1=288;
T_c2=288;


%% Tuning parameters
Tune_tr=1;
ct1 = 6.3195; 
ct2 = -5.337;
Tune_er=0.5;

%% material parameters
load N
load P
%Format for P and N is as follow:
%Temperature(K), Seeback coefficient(V/K), Electrical resistance (ohm.m), Thermal conductivity (W/m.K)
