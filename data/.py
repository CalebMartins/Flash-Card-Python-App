import pandas

data = pandas.read_csv('flash-card-project\data\\french_words.csv')

list = [row.French for (index, row) in data.iterrows()]
print(list)
#B1DDC6