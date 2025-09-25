medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
km = medida / 1000
hm = medida / 100
dam = medida / 10
print('A medida de {}m corresponde a:  \n {}cm  \n {}mm \n {}dm \n {}km \n {}hm  \n {}dam '.format(medida, cm, mm, dm, km, hm, dam))
