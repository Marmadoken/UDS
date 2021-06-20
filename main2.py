import pandas as pd


#---1---
#Загрузить данные
xl = pd.ExcelFile("data2.xlsx")
df = xl.parse("Data2")
print(df)
print()


df['sum'] = df.sum(axis=1)


df['intensiv']=df['l']+df['a1']*2.5+df['a2']*3.0+df['g1']*1.4+df['g2']*2.0
print(df)
print()
print()

print('Общая приведенная интенсивность на участке:',"%.2f" %(df['intensiv'].sum()))


v=int(input('Введите допустимую скорость (км/ч)'))

n=(3600*v)/(v+7+0.13*v*v)

print('Пропускная способность на участке:',"%.2f" %(n))

df['z']=df['intensiv']/n
print (df)
