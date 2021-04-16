function [ A ] = plate_fin_hxr_A(l_hxr,b_hxr,a_hxr,N_f,t_f,k_fin,h)
%PLATE_FIN Summary of this function goes here


%% calcuated A_t
A_b=2*(b_hxr*l_hxr-N_f*t_f*l_hxr);
A_f=2*(N_f-1)*l_hxr*(a_hxr-t_f);

%% calcuate eta
L_f=a_hxr/2-t_f;
m_f=(2*h/(k_fin*t_f)*(1+t_f/l_hxr))^0.5;
n_f=tanh(m_f*L_f)/(m_f*L_f);
A=A_b+A_f*n_f;

end