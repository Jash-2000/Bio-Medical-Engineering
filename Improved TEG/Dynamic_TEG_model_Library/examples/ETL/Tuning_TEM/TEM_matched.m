clear all
load matched
%% TEM geometrical parameters
l=1e-3; % l is the thermoelectric leg length, m
l_cw=1.5e-3;% l_cw is the length of ceramic wafer m
f=2*127*0.0028*0.0028/(0.062*0.062); % f is the fill factor -
a=0.062*0.062; % a is the area of a TEM m2.
n=127;% n is the pair of legs

%% Opertional parameters


%% Tuning parameters
Tune_tr =1;
ct1 = 6.3195; 
ct2 = -5.337;
Tune_er=0.5;

%% material parameters
load N
load P
%Format for P and N is as follow:
%Temperature(K), Seeback coefficient(V/K), Electrical resistance (ohm.m), Thermal conductivity (W/m.K)
