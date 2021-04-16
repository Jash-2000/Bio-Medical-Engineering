clear all
load OCV
load matched
%% TEM geometrical parameters
l=2.2e-3; % l is the thermoelectric leg length, m
l_cw=0.93e-3;% l_cw is the length of ceramic wafer m
f=2*9*0.0017*0.0017/(0.016*0.013); % f is the fill factor -
a=0.016*0.013; % a is the area of a TEM m2.
n=9;% n is the pair of legs
M=1;
%% Opertional parameters
I=0; % I is the current, A
T_c=273+25;

%% Tuning parameters
Tune_tr=1;
ct1 =  0.5165;
ct2 = 1883.9;
Tune_er=0.684;

%% material parameters
load N
load P
%Format for P and N is as follow:
%Temperature(K), Seeback coefficient(V/K), Electrical resistance (ohm.m), Thermal conductivity (W/m.K)
