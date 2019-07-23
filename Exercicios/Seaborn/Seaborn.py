import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

# Exercicio 1
sns.jointplot(x = 'fare', y = 'age', data = titanic)
## plt.show()

# Exercicio 2
sns.distplot(titanic['fare'], kde = False, bins = 30)
## plt.show()

# Exercicio 3
sns.boxplot(x = 'class', y = 'age', data = titanic)
## plt.show()

# Exercicio 4
sns.swarmplot(x = 'class', y = 'age', data = titanic)
## plt.show()

# Exercicio 5
sns.countplot(x = 'sex', data = titanic)
## plt.show()
plt.close(fig='all')

# Exercicos 6
corr = titanic.corr()
print(corr)

sns.heatmap(corr)
## plt.show()
plt.close(fig='all')

# Exercicio 7
g = sns.FacetGrid(data = titanic, col = 'sex')
g.map(plt.hist, 'age')
plt.show()