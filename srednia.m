function [w]= srednia(obraz)
    [x,y,~] = size(obraz);
    r = obraz(:,:,1);
    g = obraz(:,:,2);
    b = obraz(:,:,3);
    cent(1) = x/2;
    cent(2) = y/2;

    box_r = r(cent(1)-50:cent(1)+50,cent(2)-50:cent(2)+50);
    box_g= g(cent(1)-50:cent(1)+50,cent(2)-50:cent(2)+50);
    box_b = b(cent(1)-50:cent(1)+50,cent(2)-50:cent(2)+50);
    
    w(1) = mean(box_r,'all');
    w(2) = mean(box_g,'all');
    w(3) = mean(box_b,'all');
    

end