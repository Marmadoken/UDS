import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import statsmodels.stats.api as sms

from sklearn.linear_model import LinearRegression

#---1---
#Загрузить данные
xl = pd.ExcelFile("data.xls")
df = xl.parse("Data")
print(df)
print()
print()


# количество строк и столбцов
print('количество строк и столбцов')
print(df.shape)
print()
print()

#Получить имена полей таблицы данных
print('Имена полей таблицы данных')
print (df.columns)
print()
print()



# вычисляется сводная статистика, относящаяся к столбцам
#разброс значений, среднее и медиана
print('''вычисляется сводная статистика, относящаяся к столбцам
разброс значений, среднее и медиана''')
print(df.describe())

#графики
z=df['kol_svetofor'].plot()
plt.ylabel('Количество светофоров')
plt.xlabel('Участки дороги')
#plt.show()


z=df['polosi'].plot()
plt.ylabel('Количество полос')
plt.xlabel('Участки дороги')
#plt.show()


z=df['kol_svetoforex'].plot()
plt.ylabel('Количество светофоров по требованию')
plt.xlabel('Участки дороги')
#plt.show()


# строим 2 гистрограммы рядом
#
fig, axs = plt.subplots(1,2)
axs[0].hist(df['kol_legk'], bins=20)
axs[0].set_title('Количество легкого транспорта ')
axs[1].hist(df['polosi'], bins=20)
axs[1].set_title('Количество полос')
#plt.show()



# строим 3 гистрограммы рядом
#
fig, axs = plt.subplots(1,3)
axs[0].hist(df['kol_legk'], bins=20)
axs[0].set_title('Количество \nлегкого транспорта ')
axs[1].hist(df['kol_gruz1'], bins=20)
axs[1].set_title('Количество \nгрузового транспорта \n(1,5т – 3т)  ')
axs[2].hist(df['kol_gruz2'], bins=20)
axs[2].set_title('Количество \nгрузового транспорта \n(3т – 5т)  ')
#plt.show()

# строим 3 гистрограммы рядом
#
fig, axs = plt.subplots(1,2)
axs[0].hist(df['kol_svetofor'], bins=20)
axs[0].set_title('Количество \nсветофоров ')
axs[1].hist(df['kol_gruz1'], bins=20)
axs[1].set_title('Количество \nдорожных знаков  ')
#plt.show()

#уникальные значения
print('Уникальные значения поля "Количество камер слежения "')
z1=df['kol_camer'].unique()
print(z1)

print('Уникальные значения поля "Количество автобусов "')
z2=df['kol_bus'].unique()
print(z2)



#Таблица сопряженности
# Chi-square test of independence

## ниже несколько таблиц (можно оставить все или выбрать одну или несколько)
# 1) таблица, показывающая взаимосвязь
print('взаимосвязь между количеством полос и количеством грузового транспорта')
df2=pd.crosstab(df['polosi'], df['kol_gruz1'] )
print(df2)

chi2, prob, dff, expected = stats.chi2_contingency(df2)
print ("test Statistics: ", "%.5f" %(chi2), "\n",
       "p-value: ", "%.5f" %(prob), "\n")

print('взаимосвязь между количеством полос и количеством легкового транспорта')
df2=pd.crosstab(df['polosi'], df['kol_legk'] )
print(df2)

chi2, prob, dff, expected = stats.chi2_contingency(df2)
print ("test Statistics: ", "%.5f" %(chi2), "\n",
       "p-value: ", "%.5f" %(prob), "\n")

#---
print('Подмножество <4 полосы движения')
df_sub1=df.query("polosi<4")
print (df_sub1)

# количество строк и столбцов
print(df_sub1.shape)


#Описательные статистики
# вычисляется сводная статистика, относящаяся к столбцам
#разброс значений, среднее и медиану
print(df_sub1.describe())

#сколько легковых машин
print('сколько легковых машин попадают в соответствующие категории')
print(df_sub1['kol_legk'].value_counts())

#сколько светофоров
print('сколько светофоров попадают в соответствующие категории')
print(df_sub1['kol_svetofor'].value_counts())



print('Подмножество >=4 полосы движения')

df_sub2=df.query("polosi>=4")
print (df_sub2)

# количество строк и столбцов
print(df_sub2.shape)


#Описательные статистики
# вычисляется сводная статистика, относящаяся к столбцам
#разброс значений, среднее и медиану
print(df_sub2.describe())

#сколько легковых машин
print('сколько легковых машин попадают в соответствующие категории')
print(df_sub2['kol_legk'].value_counts())

#сколько светофоров
print('сколько светофоров попадают в соответствующие категории')
print(df_sub2['kol_svetofor'].value_counts())




print('Сравнение')


#--9--
#Доверительный интервал для t-теста (разница между средними значениями)
# например для двух подмножеств
z1=df_sub1['polosi']
z2=df_sub2['polosi']
cm=sms.CompareMeans(sms.DescrStatsW(z1), sms.DescrStatsW(z2))
print (cm.tconfint_diff())



# например для двух подмножеств
z1=df_sub1['ostrov_bezop']
z2=df_sub2['ostrov_bezop']
cm=sms.CompareMeans(sms.DescrStatsW(z1), sms.DescrStatsW(z2))
print (cm.tconfint_diff(usevar='pooled'))


# сводная таблица (pivot_table) для перечисленных полей
# сгруппированный по  полосам
# считантся общее(суммарное)б можно что-то общее, что-то суммарное
df101=df.pivot_table(['kol_camer', 'kol_legk', 'kol_gruz1'],
                   ['polosi'],aggfunc={'kol_camer':'sum', 'kol_legk':'sum', 'kol_gruz1':'sum'})
print(df101)

print('строки с пустыми значениями (количество)')
print(df.isnull().sum())

#выбираем одно поле
y = df.kol_legk



# удаляем несущественные из dataframe
x=df.drop(['pod_perehod','rasdelitel','ostrov_bezop','otboinik','ogr_skorosti','dor_znaki','napr_dvizhenia'], axis=1)
x=x.drop(['kol_bus', 'kol_vel','nal_vel','nal_trot','kol_cezd','nal_tram','nal_trol','nal_most','nal_tunnel'], axis=1)
x=x.drop(['nal_putpr', 'dlit_red_signal', 'kol_svetoforex' ], axis=1)

x1=x.drop('kol_legk', axis=1)

print(y)
print(x1)


# строим модель
model1 = LinearRegression()
model1.fit(x1, y)

# печатаем коэффициенты
print(model1.coef_)
print()

# предсказываем, количество легковых автомобилей, например, на таких значениях
yy= model1.predict([[2,	2,0,0,  3, 78,	32, 5,0]])
print(yy)



#выбираем одно поле
y = df.kol_gruz1
x2=x.drop('kol_gruz1', axis=1)

print(y)
print(x2)


# строим модель
model2 = LinearRegression()
model2.fit(x2, y)

# печатаем коэффициенты
print(model2.coef_)
print()

# предсказываем, количество легковых автомобилей, например, на таких значениях
yy= model2.predict([[2,	2,0,0,  3, 78,	32, 5,0]])
print(yy)
