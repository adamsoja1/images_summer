from for_nd2_files import main,display_plots
import os


czasy = [1,2,4,6,8,10,20,40,60,80,100,200,400,600,800,1000,2000,4000,6000,8000,10000,20000,40000,60000,80000,100000,200000,400000]
folder = 'seria1'
pliki = sorted(os.listdir(folder))
if '.DS_Store' in pliki:
    pliki.remove('.DS_Store')
    


seria = 10
ilosc_zdjec = len(pliki)
t = []
for i in range(0,ilosc_zdjec):
    t.append(czasy[i])

ilosc = len(t) * seria


y = main(ilosc,seria,folder,t)

display_plots(y, t, 5,'seria_1')