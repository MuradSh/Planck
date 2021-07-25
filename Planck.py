import seaborn as sns
import matplotlib.py as plt
import pandas as pd


s = pd.Series([0,2,4,18,32,50])
t= pd.Series([1,2,3,4,5,6])
motion_graph(specify="p-t",s=s,t=t,color="#1a2b3f");


v = pd.Series([0,2,4,6,8,8,8,6,4,2,0])
t= pd.Series([1,2,3,4,5,6,7,8,9,10,11])
motion_graph(specify="v-t",v=v,t=t);


a = pd.Series([0,2,4,6,8,8,8,6,4,2,0])
t= pd.Series([1,2,3,4,5,6,7,8,9,10,11])
motion_graph(specify="a-t",a=a,t=t);

smart_motion_graph(vi=5.3,dt=50,specify="v-t",freeFall=True)