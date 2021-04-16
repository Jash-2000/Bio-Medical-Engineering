figure
subplot(2,1,1)
plot(u1.time,u1.signals.values)
hold on
plot(T_out.time,T_out.signals.values)
subplot(2,1,2)
plot(abs(T_out.signals.values-u1.signals.values))