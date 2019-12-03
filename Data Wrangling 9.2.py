import pandas as pd
data = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2',], 'Dimension': ['Length','Width','Height','Length','Width','Height'], 'Value': [6,4,2,5,3,4]}
messy_data = pd.DataFrame (data,columns = ['Box','Dimension','Value'])
tidy_data = messy_data.pivot_table (index = ['Box'], columns = 'Dimension', values = 'Value').reset_index()
volume = {'Volume': [48,60]}
volume_data = pd.DataFrame (volume, columns = ['Volume'])
tidy_data ['Volume'] = volume_data
