figure(1)
for i=1:100
    wartosc = 149 + i;
    obraz = imread("IMG00" + num2str(wartosc) + ".JPG");
    w = srednia(obraz);
    plot(i,w(1),'r*',i,w(2),'g*',i,w(3),'b*')
    hold on;
    grid on;
    wynikR(i) = w(1);
    wynikB(i) = w(2);
    wynikG(i) = w(3);
end


j=1
for i=1:10
  
    wynikR_R(i) = mean(wynikR(j:i*10)); 
    wynikB_B(i) =  mean(wynikB(j:i*10)); 
    wynikG_G(i) =  mean(wynikG(j:i*10)); 
    j = j + 10;
end

t = [15:10:105];
t0 = t(1);
e = log2(t/t0);


figure(2)
plot(e,wynikR_R,'r*',e,wynikB_B,'b*',e,wynikG_G,'g*')
xlabel('Czas log_2(t/t_0)')
ylabel('Wartość pikseli')
title('Wykres działania kamery mikroskopowej z zależności od czasu ekspozycji')