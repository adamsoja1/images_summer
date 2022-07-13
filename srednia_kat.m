function [w] = srednia_kat(obraz)

    [x,y,~] = size(obraz);
    r = obraz(:,:,1);
    g = obraz(:,:,2);
    b = obraz(:,:,3);

    box_r = r(1:100,1:100);
    box_g= g(1:100,1:100);
    box_b = b(1:100,1:100);

        
    w(1) = mean(box_r,'all');
    w(2) = mean(box_g,'all');
    w(3) = mean(box_b,'all');


end