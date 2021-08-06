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


projectile_motion_graph(angle=75,vi=1311,specify="y-x",color="#FF0000")
projectile_motion_graph(angle=45,vi=1329,y=0,specify="y-x",color="#FFFF00")
projectile_motion_graph(angle=15,vi=1229,y=0,specify="y-x",color="#FF0000")
projectile_motion_graph(angle=30,vi=1393,y=0,specify="y-x",color="#0000FF")
projectile_motion_graph(angle=60,vi=1321,y=0,specify="y-x",color="#0000FF")

projectile_motion_graph(angle=25,vi=99,specify="x-y",color="#FF0000")
projectile_motion_graph(angle=45,vi=99,specify="x-y",color="#FF0000")

