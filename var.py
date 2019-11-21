import pandas as pd

# Colors 

# Graphics 
g = '#37535e'

# Music 
m = '#3c758b'

# Education 
e = '#4095b6'

# Business 
b = '#53afc9'

# Video 

v = '#73c0c4'

# Photography 

p = '#94d1bf'

# Medical 

me = '#697b30'



mac_apps = pd.read_csv('macappstore.csv')
mac_apps = mac_apps.drop(['Unnamed: 0'], axis=1)

# Graphics, Education, Business, Music, Video, Photography, Medical 

# Large Apps by Sizes

large = mac_apps[mac_apps['size'].str.contains('GB')]
large_size = large[['category','name','size', 'price', 'total_languages']].sort_values(by='size', ascending = False)
large_size['size'] = large_size['size'].str.replace('GB', '')
large_size['size'] = large_size['size'].astype(float)

# Medium : MB

medium = mac_apps[mac_apps['size'].str.contains('MB')]
medium_size = medium[['category','name','size', 'price', 'total_languages']].sort_values(by='size', ascending = False)
medium_size['size'] = medium_size['size'].str.replace('MB', '')
medium_size['size'] = medium_size['size'].astype(float)

# Small: KB

small = mac_apps[mac_apps['size'].str.contains('KB')]
small_size = small[['category','name','size', 'price', 'total_languages']].sort_values(by='size', ascending = False)
small_size['size'] = small_size['size'].str.replace('KB', '')
small_size['size'] = small_size['size'].astype(float)

# LARGE SIZES (GB)

# Graphics:
graphicsl = large_size[large_size['category'].str.contains("Graphics & Design")].sort_values(by =  'size', ascending = False)
largest_graphics = graphicsl.head(10)

# Education : 
educationl = large_size[large_size['category'].str.contains("Education")].sort_values(by =  'size', ascending = False)
largest_education = educationl.head(10)

# Business

businl = large_size[large_size['category'].str.contains("Business")].sort_values(by =  'size', ascending = False)
largest_business = businl.head(10)

# Music 
musicl = large_size[large_size['category'].str.contains("Music")].sort_values(by =  'size', ascending = False)
largest_music = musicl.head(10)

# Video
videol = large_size[large_size['category'].str.contains("Video")].sort_values(by =  'size', ascending = False)
largest_video = videol.head(10)

# Photography
photol = large_size[large_size['category'].str.contains("Photography")].sort_values(by =  'size', ascending = False)
largest_photo = photol.head(10)

# Medical
medil = large_size[large_size['category'].str.contains("Medical")].sort_values(by =  'size', ascending = False)
largest_medical = medil.head(10)



# MEDIUM SIZE (MB)
# Graphics:
graphicsm = medium_size[medium_size['category'].str.contains("Graphics & Design")].sort_values(by =  'size', ascending = False)
medium_graphics = graphicsm.head(10)

# Education : 
educationm = medium_size[medium_size['category'].str.contains("Education")].sort_values(by =  'size', ascending = False)
medium_education = educationm.head(10)

# Business

businm = medium_size[medium_size['category'].str.contains("Business")].sort_values(by =  'size', ascending = False)
medium_business = businm.head(10)

# Music 
musicm = medium_size[medium_size['category'].str.contains("Music")].sort_values(by =  'size', ascending = False)
medium_music = musicm.head(10)

# Video
videom = medium_size[medium_size['category'].str.contains("Video")].sort_values(by =  'size', ascending = False)
medium_video = videom.head(10)

# Photography
photom = medium_size[medium_size['category'].str.contains("Photography")].sort_values(by =  'size', ascending = False)
medium_photo = photom.head(10)

# Medical
medim = medium_size[medium_size['category'].str.contains("Medical")].sort_values(by =  'size', ascending = False)
medium_medical = medim.head(10)



# SMALL SIZE (KB)

# Utilities: 
#utilitys = small_size[small_size['category'].str.contains("Utilities")].sort_values(by =  'size', ascending = False)
#small_utility =  utilitys.head(10)

# Graphics
graphicss = small_size[small_size['category'].str.contains("Graphics & Design")].sort_values(by =  'size', ascending = False)
small_graphics =  graphicss.head(10)

# Education : 
educations = small_size[small_size['category'].str.contains("Education")].sort_values(by =  'size', ascending = False)
small_education = educations.head(10)

# Business

busins = small_size[small_size['category'].str.contains("Business")].sort_values(by =  'size', ascending = False)
small_business = busins.head(10)

# Music 
musics = small_size[small_size['category'].str.contains("Music")].sort_values(by =  'size', ascending = False)
small_music = musics.head(10)

# Video
videos = small_size[small_size['category'].str.contains("Video")].sort_values(by =  'size', ascending = False)
small_video = videos.head(10)

# Photography
photos = small_size[small_size['category'].str.contains("Photography")].sort_values(by =  'size', ascending = False)
small_photo = photos.head(10)

# Medical
medis = small_size[small_size['category'].str.contains("Medical")].sort_values(by =  'size', ascending = False)
small_medical = medis.head(10)


# Price 
price_c = mac_apps['price_category'].value_counts().reset_index()
price_c.rename(columns={'index':'price_category', 'price_category':'count'}, inplace=True)

paid = mac_apps.query('price_category == 1')
free = mac_apps.query('price_category == 0')

# Graphics Price
graph = paid[paid['category'].str.contains('Graphics & Design')].sort_values(by ='price', ascending = False)
paid_graph =  graph.head(10)

# Ratings

filtered_rating = mac_apps.query('rating > 0.0')

# Grouping ratings 

group1 = [1.0,1.1, 1.2, 1.3, 1.4] # 1.0
group2 = [1.5] # 1.5
group3 = [1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4] #2.0
group4 = [2.5] # 2.5
group5 = [2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4] # 3.0
group6 = [3.5] # 3.5
group7 = [3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4] # 4.0
group8 = [4.5] # 4.5
group9 = [4.6, 4.7, 4.8, 4.9, 5.0] # 5.0

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

filtered_rating['rating_est'] = filtered_rating.apply(lambda row: label_ratings(row), axis=1)



education_rate = filtered_rating[filtered_rating['category'].str.contains('Education')].sort_values(by ='rating_est', ascending = False)
medicine_rate = filtered_rating[filtered_rating['category'].str.contains('Medical')].sort_values(by ='rating_est', ascending = False)
entertain_rate = filtered_rating[filtered_rating['category'].str.contains('Entertainment')].sort_values(by ='rating_est', ascending = False)
photo_rate = filtered_rating[filtered_rating['category'].str.contains('Photography')].sort_values(by ='rating_est', ascending = False)
video_rate = filtered_rating[filtered_rating['category'].str.contains('Video')].sort_values(by ='rating_est', ascending = False)
graphics_rate = filtered_rating[filtered_rating['category'].str.contains('Graphics & Design')].sort_values(by ='rating_est', ascending = False)
business_rate = filtered_rating[filtered_rating['category'].str.contains('Business')].sort_values(by ='rating_est', ascending = False)


# Do not sort these
education_rate1 = filtered_rating[filtered_rating['category'].str.contains('Education')]
medicine_rate1 = filtered_rating[filtered_rating['category'].str.contains('Medical')]
entertain_rate1 =filtered_rating[filtered_rating['category'].str.contains('Entertainment')]
photo_rate1 = filtered_rating[filtered_rating['category'].str.contains('Photography')]
video_rate1 = filtered_rating[filtered_rating['category'].str.contains('Video')]
graphics_rate1 = filtered_rating[filtered_rating['category'].str.contains('Graphics & Design')]
business_rate1 = filtered_rating[filtered_rating['category'].str.contains('Business')]





# Music Ratings 
music_rate = filtered_rating[filtered_rating['category'].str.contains('Music')].sort_values(by ='rating_est', ascending = False)
music_rates1 = music_rate.head(10)
# Ratings greater than 5.0
highest_music = music_rate.query('rating >= 5.0')
highest_music = highest_music.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category', 'rating_est'], axis = 1)
#highest_music = highest_music.drop(['rating_est'], axis = 1)
highest_music1 = highest_music.head(10)
highest_music1.columns = ['Compatibility', 'Name']

# Renaming columns for table

#highest_music1.columns = ['Compatibility', 'Name']
highest_music.columns = ['Compatibility', 'Name']

# Ratings less than 5.0 but greater than 3.0

medium_music_rate = music_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_music_rate = medium_music_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_music_rate1 = medium_music_rate.head(10)
# Renaming columns 
medium_music_rate.columns = ['Compatibility', 'Name','Rating']
medium_music_rate1.columns = ['Compatibility', 'Name','Rating']

#Ratings : >= 5.0
highest_education_rate = education_rate.query('rating >= 5.0')
highest_education_rate = highest_education_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category', 'rating_est'], axis = 1)
highest_education_rate.columns = ['Compatibility', 'Name']
highest_education_rate1 = highest_education_rate.head(10)


# Medicine
highest_med = medicine_rate.query('rating >= 5.0')
highest_med = highest_med.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category', 'rating_est'], axis = 1)
highest_med.columns = ['Compatibility', 'Name']
highest_med1 = highest_med.head(10)

# Entertainment 
highest_entertain = entertain_rate.query('rating >= 5.0')
highest_entertain = highest_entertain.drop(['category', 'price', 'rating', 'size', 'total_languages', 'price_category', 'rating_est'], axis = 1)
highest_entertain.columns = ['Compatibility', 'Name']
highest_entertain1 = highest_entertain.head(10)

# Photography 
highest_photo = photo_rate.query('rating >= 5.0')
highest_photo = highest_photo.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category', 'rating_est'], axis = 1)
highest_photo.columns = ['Compatibility', 'Name']
highest_photo1 = highest_photo.head(10)

# Video
highest_video = video_rate.query('rating >= 5.0')
highest_video = highest_video.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category', 'rating_est'], axis = 1)
highest_video.columns = ['Compatibility', 'Name']
highest_video1 = highest_video.head(10)

# Graphics
highest_graph = graphics_rate.query('rating >= 5.0')
highest_graph = highest_graph.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category', 'rating_est'], axis = 1)
highest_graph.columns = ['Compatibility', 'Name']
highest_graph1 = highest_graph.head(10)

# Business
highest_business = business_rate.query('rating >= 5.0')
highest_business = highest_business.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category', 'rating_est'], axis = 1)
highest_business.columns = ['Compatibility', 'Name']
highest_business1 = highest_business.head(10)



# Ratings < 5.0
medium_education_rate = education_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_education_rate = medium_education_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_education_rate.columns = ['Compatibility', 'Name', 'Rating']
medium_education_rate1 = medium_education_rate.head(10)


# Music
medium_music_rate = music_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_music_rate = medium_music_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_music_rate.columns = ['Compatibility', 'Name', 'Rating']
medium_music_rate1 = medium_music_rate.head(10)

# Medicine
medium_med_rate = medicine_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_med_rate = medium_med_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_med_rate.columns = ['Compatibility', 'Name', 'Rating']
medium_med_rate1 = medium_med_rate.head(10)

# Entertainment 
medium_entertain_rate = entertain_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_entertain_rate = medium_entertain_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_entertain_rate.columns = ['Compatibility', 'Name', 'Rating']
medium_entertain_rate1 = medium_entertain_rate.head(10)

# Photography 
medium_photo_rate = photo_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_photo_rate = medium_photo_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_photo_rate.columns = ['Compatibility', 'Name', 'Rating']
medium_photo_rate1 = medium_photo_rate.head(10)

# Video
medium_video_rate = video_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_video_rate = medium_video_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_video_rate.columns = ['Compatibility', 'Name', 'Rating']
medium_video_rate1 = medium_video_rate.head(10)

# Graphics
medium_graph_rate = graphics_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_graph_rate = medium_graph_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_graph_rate.columns = ['Compatibility', 'Name', 'Rating']
medium_graph_rate1 = medium_graph_rate.head(10)

# Business
medium_business_rate = business_rate.query('rating_est >= 3.0 & rating_est < 5.0')
medium_business_rate = medium_business_rate.drop([ 'category', 'price', 'rating', 'size', 'total_languages', 'price_category'], axis = 1)
medium_business_rate.columns = ['Compatibility', 'Name', 'Rating']
medium_business_rate1 = medium_business_rate.head(10)

















