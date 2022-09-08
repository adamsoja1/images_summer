x =  2072.38
y = 1554.29

psx =x/2
pxy = y/2

bx = x/5
by = y/5


sekcje = 5

kropki_x = x/(sekcje*2);
pkt_x = []

kropki_y = y/(sekcje*2)
pkt_y = []



    
for kr_x in range(1,sekcje+1): 
    temp1 = kr_x*kropki_x*2 - kropki_x
    pkt_x.append(temp1)
    pkt_y.append(kr_x*kropki_y*2 - kropki_y)
    
pkt = []

for i in range(0,len(pkt_x)):
    for j in range(0,len(pkt_x)):
        pkt.append((pkt_x[i],pkt_y[j]))


for i in range(25):
    x = round(pkt[i][0],2)
    y = round(pkt[i][1],2)
    print('-----------')
    print(f'x:{x} y:{y}')
    
    




srodek = (psx,pxy)
    

pkty=[]
for i in range(25):
    x = pkt[i][0] - srodek[0]
    y = pkt[i][1] - srodek[1]
    punkt = (x,y)
    pkty.append(punkt)

print('o ile przesunac')
for i in range(25):
    x = round(pkty[i][0],2)
    y = round(pkty[i][1],2)
    print('-----------')
    print(f'x:{x} y:{y}')

file = open('wynik.txt','w')

for i in range(25):
    x = round(pkty[i][0],2)
    y = round(pkty[i][1],2)
    file.write('---------\n')
    file.write(f'x:{x} y:{y}\n')
file.close()
# for i = 1:sekcje
#     for j = 1:sekcje
        
#         pkt{i,j} = [pkt_x(i), pkt_y(j)];

#     end
# end

# for i = 1:sekcje
#     for j = 1:sekcje

#         vek{i,j} = [pkt_x(i) - ps(1), pkt_y(j)-ps(2)];

#     end
# end