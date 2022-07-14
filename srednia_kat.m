function [w] = srednia_kat(obraz)

    [x,y,~] = size(obraz);
    r = obraz(:,:,1);
    g = obraz(:,:,2);
    b = obraz(:,:,3);

    box_r = r(1:10,1:10);
    box_g= g(1:10,1:10);
    box_b = b(1:10,1:10);
    
        
    w(1) = mean(box_r,'all');
    w(2) = mean(box_g,'all');
    w(3) = mean(box_b,'all');


end