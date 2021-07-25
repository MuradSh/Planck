""" 
    v = speed
    s = distance
    t = time
    a = acceleration
    specify = [
        "p-t" -> position-time graph
        "v-t" -> velocity-time graph
        "a-t" -> acceleration-time graph
    ]
    -------
    all arguments, except specify, are given as series
    ------- 
    TODO: add summary of the graph?
"""
def motion_graph(
        v=[],s=[],t=[],a=[],specify="",  #data
        color="#00aaff" #information about graphs
        ):
    if specify=="p-t":
        draw_graph(s,t,"Position","Time",color)
    elif specify=="v-t":
        draw_graph(v,t,"Velocity","Time",color)
    elif specify=="a-t":
        draw_graph(a,t,"Acceleration","Time",color)
    else:
        raise ValueError("Please specify the type of graph you want. Options are: 'p-t','v-t','a-t'")
# helper function for motion_graph

def draw_graph(series1,series2,ylabel,xlabel,color="#00aaff",line=False):
        # make all arguments pandas.Series
        if not isinstance(series1,pd.Series):
            series1 = pd.Series(va for va in series1)
        if not isinstance(series2,pd.Series):
            series2 = pd.Series(v for v in series2)
        # create a dataframe
        df = pd.DataFrame()
        df = df.assign(series1=series1.values)
        df = df.assign(series2=series2.values)
        #plot
        if line:
            g = sns.lineplot(x="series2",y="series1",data=df,color=color);    
        else:
            g = sns.pointplot(x="series2",y="series1",data=df,color=color);    
        g = (g.set(ylabel=ylabel, xlabel=xlabel))    
        
        
        
        
 """
    v = velocity
    vi = initial velocity
    vf = final velocity
    s = position
    si = initial position
    sf = final position
    dt = change in time
    a = acceleration
    specify = [
        "p-t" -> position-time
        "v-t" -> velocity-time
    ]
    plane = either horizontal(h) or vertical(v). The equations change based on the plane.
"""
def smart_motion_graph(
    v=None,vi=None,vf=None,s=None,si=None,sf=None,dt=None,a = None, specify="",freeFall=False,
    color="#00aaff" #information about graphs
    ):
    
    if freeFall==True:
        a=-G
    
    if dt==None and specify:
        raise ValueError("Please specify change in time(dt)")
        
    if specify=="p-t":
        # SCENARIO 1: Uniform motion We have v, si and time. sf = si+v*dt
        if((v!=None or vi!=None) and si!=None and a==None):
            v = vi if v==None else v
            sf = si+v*dt
            #series for all variables
            s_dt = pd.Series(va for va in range(1,dt+1,round(dt*0.1)))
            s_s = pd.Series([],dtype=pd.StringDtype())
            for i in range(0,dt,round(dt*0.1)):
                sf = si+v*i
                s_s.at[sf] = sf            
            draw_graph(s_s,s_dt,"Position","Time",line=True)  
        # SCENARIO 2: Constant acceleration: We have a,vi, si and time. sf = si+vf*dt+0.5*a*(dt)^2
        elif((v!=None or vi!=None) and (si!=None or s!=None) and a!=None):
            vi = vi if v==None else v
            si = si if s==None else s
            vf = vi+a*dt
            s_s = pd.Series([],dtype=pd.StringDtype())
            s_dt = pd.Series(va for va in range(1,dt+1,round(dt*0.1)))
            for i in range(0,dt,round(dt*0.1)):
                sf = si+vi*i+0.5*a*(i**2)                
                s_s.at[sf] = sf
            draw_graph(s_s,s_dt,"Position","Time",line=True,color=color)
        else: 
            raise ValueError("Please provide the necessary arguments. If it's uniform motion then v,si and time. If it's motion with constant acceleration then a,vi,si and time")
    elif specify=="v-t":
        # SCENARIO 1: GIVEN : vi, a, dt. Equation vf = vi+a*dt
        if((v!=None or vi!=None) and a!=None):
            s_dt = pd.Series(va for va in range(1,dt+1,round(dt*0.1)))
            s_v = pd.Series([],dtype=pd.StringDtype())
            for i in range(0,dt,round(dt*0.1)):
                vf = vi+a*i
                s_v.at[vf] = vf            
            draw_graph(s_v,s_dt,"Velocity","Time",line=True,color=color)
        else:
            raise ValueError("Please provide the necessary arguments - vi, a, dt")