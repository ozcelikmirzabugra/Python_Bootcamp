import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")

# %% scatter plot
# boy vs kilo
sns.set_style("white")
plt.figure()
sns.scatterplot(x = "boy", y = "kilo", data = veri)
plt.title("boy vs kilo ")

# figure style
sns.set_style("darkgrid")
plt.figure()
sns.scatterplot(x = "boy", y = "kilo", data = veri)
plt.title("boy vs kilo ")

# figure style
sns.set_style("whitegrid")
plt.figure()
sns.scatterplot(x = "boy", y = "kilo", data = veri)
plt.title("boy vs kilo ")

# boy vs kilo cinsiyet tiplerine gore
plt.figure()
sns.scatterplot(x = "boy", y = "kilo", data = veri, hue = "cinsiyet")

# scatter plot with linear regression
plt.figure()
sns.regplot(x = "boy", y = "kilo", data = veri, marker = "+", scatter_kws = {"alpha":0.2})

# renk paletleri 
plt.figure()
sns.scatterplot(x = "boy", y = "kilo", data = veri, hue = "madalya", palette="Blues")

# sezona gore boy ve kilo karsilastirmasi
plt.figure()
sns.scatterplot(x='boy', y='kilo', data=veri ,hue="sezon" , palette="Accent")
plt.title('Boy ve Kilo Dağılımı - Beyaz Izgara Tema')
plt.show()

# %% line plot
plt.figure() 
sns.lineplot(x = "boy", y = "kilo", data = veri)

# categoric cizgi grafigi
plt.figure() 
sns.lineplot(x = "boy", y = "kilo", data = veri, hue = "madalya")

# %% histogram
plt.figure() 
sns.displot(veri, x = "kilo")

plt.figure() 
sns.displot(veri, x = "kilo", hue = "cinsiyet")

plt.figure()
sns.displot(veri, x = "kilo", col = "cinsiyet")

# iki boyutlu histogram
plt.figure()
sns.displot(veri, x = "kilo", y = "boy", kind = "kde", hue = "cinsiyet")

plt.figure()
sns.displot(veri, x = "kilo", y = "boy", kind = "kde", hue = "sezon")

# %% bar plot
plt.figure()
sns.barplot(x = "madalya", y = "yas", data = veri)

plt.figure()
sns.barplot(x = "madalya", y = "yas", data = veri, hue = "cinsiyet")

plt.figure()
sns.catplot(x = "madalya", y = "yas", data = veri, hue = "cinsiyet", col = "sezon", kind = "bar")

# spor vs boy cinsiyet kategorisine ve sezon sutununa gore
plt.figure()
sns.catplot(x= "spor", y="boy", data=veri, hue = "cinsiyet", col = "sezon", kind = "bar")
plt.xticks(rotation = 90)

# %% box plot 
plt.figure()
sns.boxplot(x = "sezon", y = "boy", data = veri)

plt.figure()
sns.boxplot(x = "sezon", y = "boy", data = veri, hue = "cinsiyet")

plt.figure()
veri_gecici = veri.loc[:, ["yas", "boy", "kilo"]]
sns.boxplot( data = veri_gecici, orient="h")

sns.catplot(x = "sezon", y = "boy", hue = "cinsiyet", col = "madalya", data = veri, kind = "box")

# cinsiyet vs yas, categori = madalya, col = sezon
sns.catplot(x = 'cinsiyet', y = 'yas', data = veri, hue='madalya', col='sezon', kind='box')

# %% heat map
veri_gecici = veri.loc[:, ["yas", "boy", "kilo"]]
correlation = veri_gecici.corr()

sns.heatmap(correlation, annot = True, fmt = ".2f", linewidths=0.5)

# %% violin plot 
sns.violinplot(x = "sezon", y = "boy", data = veri)

sns.violinplot(x = "sezon", y = "boy", data = veri, hue = "cinsiyet")

sns.violinplot(x = "sezon", y = "boy", data = veri, hue = "cinsiyet", split = True)

sns.catplot(x = "sezon", y = "boy", hue = "cinsiyet", col = "madalya", data =veri, kind = "violin", split = True)

# %% joint plot 
sns.jointplot(data =veri, x = "kilo", y = "boy", hue = "sezon", kind = "kde")

g = sns.jointplot(data =veri, x = "kilo", y = "boy")
g.plot_joint(sns.histplot)
g.plot_marginals(sns.boxplot)

# %% pairplot
sns.pairplot(veri)

g = sns.PairGrid(veri)
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot, kde = True)

# %% count plot 
sns.countplot(x = "spor", data = veri)
plt.xticks(rotation = 90)


