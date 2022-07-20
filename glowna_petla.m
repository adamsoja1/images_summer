function [figures] = glowna_petla(numer,ilosc,t,seria,sciezka)
   t0 = t(2) - t(1);
    e = log(t/t0);

    figures(1)= figure();
    for i=1:ilosc
        wartosc = numer + i;
        obraz = imread(sciezka + "/IMG0" + num2str(wartosc) + ".JPG");
        w = srednia(obraz);
        plot(i,w(1),'r*',i,w(2),'g*',i,w(3),'b*')
        title('Dla wartosci centrum 100x100')
        hold on;
        grid on;
        wynikR(i) = w(1);
        wynikB(i) = w(3);
        wynikG(i) = w(2);
    
    end
  
%     
   figures(2) = figure();
    for i=1:ilosc
        wartosc1 = numer + i;
        obraz1 = imread(sciezka + "/IMG0" + num2str(wartosc1) + ".JPG");
        w_kat = srednia_kat(obraz1);
        plot(i,w_kat(1),'r*',i,w_kat(2),'g*',i,w_kat(3),'b*')
        

        title('Dla wartosci lewego gornego rogu(100x100)')
        hold on;
        grid on;
        wynikR_kat(i) = w_kat(1);
        wynikB_kat(i) = w_kat(3);
        wynikG_kat(i) = w_kat(2);
    
    end

   figures(3) = figure();
    for i=1:ilosc
        wartosc2 = numer + i;
        obraz2 = imread(sciezka + "/IMG0" + num2str(wartosc2) + ".JPG");
        w_kat = kat_prawy(obraz2);
        plot(i,w_kat(1),'r*',i,w_kat(2),'g*',i,w_kat(3),'b*')
        

        title('Dla wartosci lewego dolnego rogu(100x100)')
        hold on;
        grid on;
        wynikR_kat(i) = w_kat(1);
        wynikB_kat(i) = w_kat(3);
        wynikG_kat(i) = w_kat(2);
    
    end

   figures(4) = figure();
    for i=1:ilosc
        wartosc2 = numer + i;
        obraz2 = imread(sciezka + "/IMG0" + num2str(wartosc2) + ".JPG");
        w_kat = kat_prawy_do(obraz2);
        plot(i,w_kat(1),'r*',i,w_kat(2),'g*',i,w_kat(3),'b*')
        

        title('Dla wartosci prawego gornego rogu(100x100)')
        hold on;
        grid on;
        wynikR_kat(i) = w_kat(1);
        wynikB_kat(i) = w_kat(3);
        wynikG_kat(i) = w_kat(2);
    
    end

   figures(5) = figure();
    for i=1:ilosc
        wartosc2 = numer + i;
        obraz2 = imread(sciezka + "/IMG0" + num2str(wartosc2) + ".JPG");
        w_kat = kat_prawy_dolny(obraz2);
        plot(i,w_kat(1),'r*',i,w_kat(2),'g*',i,w_kat(3),'b*')
        

        title('Dla wartosci prawy dolnego rogu(100x100)')
        hold on;
        grid on;
        wynikR_kat(i) = w_kat(1);
        wynikB_kat(i) = w_kat(3);
        wynikG_kat(i) = w_kat(2);
    
    end

%     length(e)
%   
%     figure()
%     plot(e,wynikR,'r*', e,wynikG,'g*', e,wynikB,'b*')
%     xlabel('Czas log_2(t/t_0)')
%     ylabel('Wartość pikseli')
%    
%     
    j=1;
    for i=1:length(t)

      if mod(i,2) ~= 0

        wynikR_R1 = mean(wynikR(i:i+1));
        wynikG_G2 =  mean(wynikG(i:i+1)); 
        wynikB_B3 =  mean(wynikB(i:i+1)); 
    
        wynikR_R_k1 = mean(wynikR_kat(i:i+1)); 
        wynikG_G_k2 =  mean(wynikG_kat(i:i+1)); 
        wynikB_B_k3 =  mean(wynikB_kat(i:i+1)); 
      end
        
        wynikR_R(i) = wynikR_R1
        wynikG_G(i) =  wynikG_G2
        wynikB_B(i) =  wynikB_B3
    
        wynikR_R_k(i) = wynikR_R_k1
        wynikG_G_k(i) =  wynikG_G_k2
        wynikB_B_k(i) =  wynikB_B_k3
      
      
    end
%         j=1;
%     for i=1:length(t)
%       
%         wynikR_R(i) = mean(wynikR(j:i*10));
%         wynikG_G(i) =  mean(wynikG(j:i*10)); 
%         wynikB_B(i) =  mean(wynikB(j:i*10)); 
%     
%         wynikR_R_k(i) = mean(wynikR_kat(j:i*10)); 
%         wynikG_G_k(i) =  mean(wynikG_kat(j:i*10)); 
%         wynikB_B_k(i) =  mean(wynikB_kat(j:i*10)); 
%     
%         j = j + seria;
%     end

    
   figure();
    plot(e,wynikR_R,'r*',e,wynikG_G,'g*',e,wynikB_B,'b*')
    xlabel('Czas log_2(t/t_0)')
    ylabel('Wartość pikseli')
    title('Wykres działania kamery mikroskopowej z zależności od czasu ekspozycji[centrum obrazow]')
    
    
    figure()
    plot(e,wynikR_R_k,'r*',e,wynikG_G_k,'g*',e,wynikB_B_k,'b*')
    xlabel('Czas log_2(t/t_0)')
    ylabel('Wartość pikseli')
    title('Wykres działania kamery mikroskopowej z zależności od czasu ekspozycji[lewy gorny rog obrazu]')
    r = [1:10];

    arr = cat(1,wynikR_R,wynikG_G,wynikB_B);
    arr = rot90(arr,-1)
    gr = {'R','G','B'};
    p = anova1(arr,gr);

    figure()
    plot(e,wynikR_R,'b.',e,wynikR_R_k,'r.')
    xlabel('Czas log_2(t/t_0)')
    ylabel('Wartość pikseli')
%commit
end