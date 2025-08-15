import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('netflix_data_cleaned.xlsx')
#               Comparision Of Movies and TV Shows Released On Netflix 
type_count= df['Type'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(type_count.index,type_count.values,color=['green','orange'])
plt.title('Number if Movies And TV Shows Comparision')
plt.xlabel('Type')
plt.ylabel('Number of Movies and TV shows')
plt.tight_layout()
plt.savefig('Type_Count_Netflix.png')
plt.show()
#               For Rating Distribution with Percentage in PieChart
Rating=df['Rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(Rating,labels=Rating.index,autopct='%1.1f%%',startangle=40)
plt.title('Rating Distribution With PieChart')
plt.tight_layout()
plt.savefig('Rating_Netflix.png')
plt.show()  


#               For Finding Duration of Movies


Movie_df=df[df['Type']=='Movie'].copy()
Movie_df['Duration_int']=Movie_df['Duration'].str.replace('min','').astype(int)

plt.figure(figsize=(10,6))

plt.hist(Movie_df['Duration_int'],bins=50,color='orange',edgecolor='black',label='Duration Of Movies')
plt.legend()
plt.title('Movie Duration Histogram')
plt.xlabel('Number Of Movies')
plt.ylabel('Duration Of Movies')
plt.savefig('Movie_Duration')
plt.tight_layout()
plt.savefig('Movie_Duration.png')
plt.show()


#                For Finding Duration of Movies

tv_df = df[df['Type'] == 'TV Show'].copy()
tv_df['Duration_int'] = (
    tv_df['Duration']
    .str.replace('Seasons', '', regex=False)
    .str.replace('Season', '', regex=False)
    .str.strip()
    .astype(int)
)
plt.figure(figsize=(10, 6))
plt.hist(tv_df['Duration_int'], bins=15, color='orange', edgecolor='black', label='Duration of TV Shows')
plt.legend()
plt.title('TV Shows Duration Histogram')
plt.xlabel('Number of Seasons')
plt.ylabel('Count of TV Shows')
plt.tight_layout()
plt.savefig('Count of TV Shows.png')
plt.show()


#           Content Released PerYear
release_year=df['Release Year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_year.index,release_year.values,color='blue')
plt.title('Release Year Vs Number of Content')
plt.xlabel('Release Year')
plt.ylabel('Number of Content')
plt.tight_layout()
plt.savefig('Release_year Content.png')
plt.show()



#           Content Producing Countries
Country_count=df['Country'].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.barh(Country_count.index,Country_count.values,color='Purple')
plt.title('Top 10 Countries Content')
plt.xlabel('Number of Content Released')
plt.ylabel('Countries that provide content')
plt.tight_layout()
plt.savefig('Content Provide Country.png')
plt.show()



#           Compairing 2Plots Of Movies and TV Show Side by Side



Content_with_year=df.groupby(['Release Year','Type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(12,8))

ax[0].plot(Content_with_year.index,Content_with_year['Movie'],color='blue')
ax[0].set_title('Movie Content With Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('No of Movies')


ax[1].plot(Content_with_year.index,Content_with_year['TV Show'],color='orange')
ax[1].set_title('TV Shows Content With Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('No of TV Shows')

plt.suptitle('Comparision Between Movies and TV Shows')
plt.tight_layout()
plt.savefig('Released Movie+Shows Comparision')
plt.show()