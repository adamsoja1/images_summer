clc;
clear all;
close all;

obraz = imread('badanie_bieli/IMG00291.JPG');


kekw1 = min(min(obraz(:,:,1)));
kekw2 = min(min(obraz(:,:,2)));
kekw3 = min(min(obraz(:,:,3)));



kekw11 = max(max(obraz(:,:,1)));
kekw22 = max(max(obraz(:,:,2)));
kekw33 = max(max(obraz(:,:,3)));



