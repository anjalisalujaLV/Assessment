

1
"""

import numpy as np
def grayscale_f(data):
  data[0][0][2]=(data[0][0][2]*0.2989) +(data[0][0][2]*0.5870) + (data[0][0][2]*0.1140)
  return data

rgb_image=np.array([[[255,0,0],[0,255,0],[0,0,255]],
                     [[255,255,0],[255,0,255],[0,255,255]],
                     [[127,127,127],[200,200,200],[50,50,50]]])

print(grayscale_f(rgb_image))

"""2"""

data=np.array([23,34,45,65,76,81])

"""3"""

array=np.array([[[255,0,0],[0,255,0],[0,0,255]],
                     [[255,255,0],[255,0,255],[0,255,255]],
                     [[127,127,127],[200,200,200],[50,50,50]]])

array=array.flatten(order='A')
array=array.reshape((3,9),order='A')
array

"""4

I will store the athlete data in 2D array, then using index [:] as it has to be from first till last, using different functions of numpy,like mean and all stats function, perfromance can be computed column wise with axis=1.

5
"""

import numpy as np
data=np.array([[11,12,13],[23,24,35],[32,43,31]])
data1=np.mean(data,axis=1)
data1

"""6"""

arr=np.array([[25,30,35,40,45,50,55],
      ['New York','Los Angeles','Chicago','Houston','Phoenix','Miami','Boston']])
arr1=np.array([20,35,40,42,47,50,53])
for i in range(7):
  arr[0][i]=arr1[i]

print(arr)

"""7"""

import pandas as pd
data={'Name':['Alice','Bob','Charlie','David','Eve','Frank','Grace'],
      'Age':[25,30,35,40,45,50,55],
      'City':['New York','Los Angeles','Chicago','Houston','Phoenix','Miami','Boston'],
      'Department':['HR','IT','Finance','Marketing','Sales','IT','HR']}

df=pd.DataFrame(data)
df=df[(df['Age']<45) & (df['Department']!='HR')]
df=df[['Name','City']]
print(df)

"""8"""

data={'Product':['Apples','Bananas','Cherries','Dates','Elderberries','Flour','Grapes'],
      'Category':['Fruit','Fruit','Fruit','Fruit','Fruit','Bakery','Fruit'],
    'Price':[1.20,0.50,3.00,2.50,4.00,1.50,2.00],
      'Promotion':[True,False,True,True,False,True,False]}

df=pd.DataFrame(data)
df=df[df['Category']=='Fruit']
avg_price=df['Price'].mean()
df=df[(df['Price']>avg_price)]
df=df[df['Promotion']==False]
df.reset_index(drop=True,inplace=True)
print(df)

"""9"""

import pandas as pd
employee_data={'Employee':['Alice','Bob','Charlie','David'],
               'Department':['HR','IT','Finance','IT'],
               'Manager':['John','Rachel','Emily','Rachel']}

project_data={'Employee':['Alice','Charlie','Eve'],
              'Project':['P1','P3','P2']}

employee_df=pd.DataFrame(employee_data)
project_df=pd.DataFrame(project_data)

final_df=pd.merge(employee_df,project_df,on='Employee',how='outer')
print(final_df)

"""10"""

import pandas as pd
data={'Department':['Electronics','Electronics','Clothing','Clothing','Home Goods'],
      'Salesperson':['Alice','Bob','Charlie','David','Eve'],
      'Sales':[70000,50000,30000,40000,60000]}

df=pd.DataFrame(data)
avg_df=df[['Salesperson','Department','Sales']].groupby(['Salesperson','Department']).mean()
rank_df=df[['Department','Sales']].groupby(['Department']).mean().rank()
print(avg_df)
print(rank_df)