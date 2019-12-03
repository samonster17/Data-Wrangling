import pandas as pd
mat = {'Student' :['Ice Bear', ' Panda', 'Grizzly'], 'Math': [ 80,95,79 ]}
eletronic = {'Student' :['Ice Bear', ' Panda', 'Grizzly'], 'Electronics': [ 85,81,83 ]}
gea = {'Student' :['Ice Bear', ' Panda', 'Grizzly'], 'GEAS': [ 90,79,93 ]}
esa = {'Student' :['Ice Bear', ' Panda', 'Grizzly'], 'ESAT': [ 93,89,88 ]}
m=pd.DataFrame(mat,columns=['Student', 'Math'])
e=pd.DataFrame(eletronic,columns=['Student', 'Electronics'])
g=pd.DataFrame(gea,columns=['Student', 'GEAS'])
s=pd.DataFrame(esa,columns=['Student', 'ESAT'])
A = pd.merge(m,e)
B = pd.merge(g,s)
C = pd.merge(A,B)
