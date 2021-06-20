import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt



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
