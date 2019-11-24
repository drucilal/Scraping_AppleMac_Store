
import seaborn as sns
import matplotlib.pyplot as plt
import mac as mac
# Count Plot 



def category_plot (y_value, dataset, color, ylabel):
	'''
	Generates a count plot between categorical variables
	y_value: chosen variable
	dataset: current dataset 
	color: choose a seaborn pallette
	ylabel: modify the title of the yaxis 
	'''
	sns.set(style = 'whitegrid', font_scale = 1.8, rc={"figure.figsize": (12, 13), 'grid.color': '0.9'},)
	x = sns.countplot(y = y_value, data = dataset , palette= color, order = dataset[y_value].value_counts().index)
	plt.xlabel('Count') 
	plt.ylabel(ylabel)
	return x


# Finding the mean 
def avg_plot (data, x, y, color):
	'''
	Group, aggregate (mean), sort
	Plot  the  average number of each y value
	data: dataset
	x: x value
	y : y value
	color = chosen color 
	'''
	s = data.groupby([x])[y].mean().sort_values().plot(kind = 'barh', color = color)
	return s

    # Finding the sum 
def add_plot (data, x, y, color):
	x = data.groupby([x])[y].sum().sort_values().plot(kind = 'barh', color = color)
	return x


	# Digging into apps
def apps_plot (data, x, y, color):
	sns.set(style = 'whitegrid', font_scale = 1.5, rc={"figure.figsize": (10, 13), 'grid.color': '0.9'},)
	x = sns.barplot(x = x , y = y , data = data , color = color, ci = None)
	return x

# Rating Plot 
def rating_plot (a):
    sns.set(style = 'whitegrid', font_scale = 1.8, rc={"figure.figsize": (12, 13), 'grid.color': '0.9'},)
    x = sns.countplot(y = 'rating_est', data = a , palette= "Blues_d",
                      order = a['rating_est'].value_counts().index)
    return x
    


def table_style (data):
    x = data.style.set_table_styles(
[{'selector': 'tr:nth-of-type(odd)',
  'props': [('background', '#eee')]}, 
 {'selector': 'tr:nth-of-type(even)',
  'props': [('background', 'white')]},
 {'selector': 'th',
  'props': [('background', '#606060'), 
            ('color', 'white'),
            ('font-family', 'verdana')]},
 {'selector': 'td',
  'props': [('font-family', 'verdana')]},
]
).hide_index()
    return x



# Creating an Estimate of Ratings 
def label_ratings (row):
    if row['rating'] in group1:
        return 1.0
    if row['rating'] in group2:
        return 1.5
    if row['rating'] in group3:
        return 2.0
    if row['rating'] in group4:
        return 2.5
    if row['rating'] in group5:
        return 3.0
    if row['rating'] in group6:
        return 3.5
    if row['rating'] in group7: 
        return 4.0
    if row ['rating'] in group8:
        return 4.5
    if row['rating'] in group9:
        return 5.0




