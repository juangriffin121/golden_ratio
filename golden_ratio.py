import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(14,10))
a=np.array([0,1])
b=np.array([np.sqrt(2),0])
o=np.array([0,0])
#ax.plot([o[0],(1/2)*b[0]+o[0]+a[0]],[o[1],(1/2)*b[1]+o[1]+a[1]],'r')
ax.plot([o[0],a[0]+o[0],a[0]+o[0]+b[0],o[0]+b[0],o[0]],[o[1],a[1]+o[1],a[1]+o[1]+b[1],o[1]+b[1],o[1]],'b')
ITS=16
for n in range(ITS):
  o=o+a+(1/2)*b
  a,b=((1/2)*b,-a)
  ax.plot([o[0],b[0]+o[0]],[o[1],b[1]+o[1]],'b')
  #ax.plot([o[0],(1/2)*b[0]+o[0]+a[0]],[o[1],(1/2)*b[1]+o[1]+a[1]],'r')
  
