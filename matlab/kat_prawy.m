function [w] = kat_prawy(obraz)

    [y,x,~] = size(obraz);
    r = obraz(:,:,1);
    g = obraz(:,:,2);
    b = obraz(:,:,3);

    box_r = r(y-111:y-100,100:111);
    box_g= g(y-111:y-100,100:111);
    box_b = b(y-111:y-100,100:111);
    
        
    w(1) = mean(box_r,'all');
    w(2) = mean(box_g,'all');
    w(3) = mean(box_b,'all');


end