function [figures] = glowna_petla(numer,ilosc)

    figures(1)= figure();
    for i=1:ilosc
        wartosc = numer + i;
        obraz = imread("zdj_day1/IMG00" + num2str(wartosc) + ".JPG");
        w = srednia(obraz);
        plot(i,w(1),'r*',i,w(2),'g*',i,w(3),'b*')
        title('Dla wartosci centrum 100x100')
        hold on;
        grid on;
        wynikR(i) = w(1);
        wynikB(i) = w(3);
        wynikG(i) = w(2);
    
    end
    
   figures(2) = figure();
    for i=1:100
        wartosc1 = numer + i;
        obraz1 = imread("zdj_day1/IMG00" + num2str(wartosc1) + ".JPG");
        w_kat = srednia_kat(obraz1);
        plot(i,w_kat(1),'r*',i,w_kat(2),'g*',i,w_kat(3),'b*')
        title('Dla wartosci lewego gornego rogu(100x100)')
        hold on;
        grid on;
        wynikR_kat(i) = w_kat(1);
        wynikB_kat(i) = w_kat(3);
        wynikG_kat(i) = w_kat(2);
    
    end
    
    
    j=1;
    for i=1:10
      
        wynikR_R(i) = mean(wynikR(j:i*10));
        wynikG_G(i) =  mean(wynikG(j:i*10)); 
        wynikB_B(i) =  mean(wynikB(j:i*10)); 
    
        wynikR_R_k(i) = mean(wynikR_kat(j:i*10)); 
        wynikG_G_k(i) =  mean(wynikG_kat(j:i*10)); 
        wynikB_B_k(i) =  mean(wynikB_kat(j:i*10)); 
    
        j = j + 10;
    end
    
    t = [15:10:105];
    t0 = t(1);
    e = log2(t/t0);
    
    
    figures(3) = figure();
    plot(e,wynikR_R,'r*',e,wynikG_G,'g*',e,wynikB_B,'b*')
    xlabel('Czas log_2(t/t_0)')
    ylabel('Wartość pikseli')
    title('Wykres działania kamery mikroskopowej z zależności od czasu ekspozycji[centrum obrazow]')
    
    
    figures(4) = figure();
    plot(e,wynikR_R_k,'r*',e,wynikG_G_k,'g*',e,wynikB_B_k,'b*')
    xlabel('Czas log_2(t/t_0)')
    ylabel('Wartość pikseli')
    title('Wykres działania kamery mikroskopowej z zależności od czasu ekspozycji[lewy gorny rog obrazu]')
    r = [1:10];

    p = anovan(r,{wynikR_R,wynikG_G,wynikB_B});

end