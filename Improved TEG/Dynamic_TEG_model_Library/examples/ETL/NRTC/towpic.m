figure
subplot(2,1,1)
plot(p.time,p.signals.values)
hold on
plot(P_max.time,P_max.signals.values)
subplot(2,1,2)
plot(abs(P_max.signals.values-p.signals.values))