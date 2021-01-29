import plotly
import plotly.express as px
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd

###THE SCRIPTS BELOW CREATED ALL THE VISUALS IN THE WEB APP. THERE ARE FOUR OF THEM.
###ALSO SHOWS THE CLEANING AND WRANGLING OF DATA

### script below is for the histogram. It writes the figure to a file, then I add that figure file to the project
raw = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_all = raw.fillna(0)
df_all['Odds_Mean'] = df_all['Odds'].mean()
df_all['trackCondition'].replace(to_replace='Muddy', value='Sloppy', inplace=True)

X = df_all['Odds']
Y = df_all['Odds']

fig_histogram = px.histogram(df_all, x=X, color='trackCondition',
                 title='Odds Distribution with Track Conditions'
                 )

fig_histogram.write_html('D:/Personal/WGU/Capstone_Docs/visual_histogram_oddsDist.html', include_plotlyjs='cdn')



### script below is for the scatter matrix. It writes the figure to a file, then I add that figure file to the project
raw = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_all = raw.fillna(0)

df_all = df_all[['Odds', 'lowTemp', 'highTemp', 'precipitation', 'final_place', 'PP']]

# below creates 2 new new columns
df_all['averageTemp'] = df_all['lowTemp'] + df_all['highTemp']
df_all['averageTemp'] = df_all['averageTemp'] / 2
df_all['top_3'] = df_all['final_place'] < 4

# removes 2 columns
df_all = df_all.drop(['lowTemp','highTemp'], axis=1)

fig3 = px.scatter_matrix(df_all,
                         dimensions=['Odds', 'averageTemp', 'precipitation', 'PP'],
                         color='final_place',
                         labels={'averageTemp':'AvgTemp', 'precipitation':'Rain',
                                 'final_place':'Final Place', 'trackCondition':'Track Condition',
                                 'top_3':'Top 3 Finish', 'weather':'Weather Description',
                                 'attendance':'Attendance', 'PP':'P.Position', 'Odds':'Odds'},
                         opacity=0.4,
                         title='Data Features Scatter Matrix',
                         height=800)

fig3.write_html('D:/Personal/WGU/Capstone_Docs/predict_visual3.html', include_plotlyjs='cdn')



### script below is for the PCA. It writes the figure to a file, then I add that figure file to the project
raw = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_all = raw.fillna(0)

df_all = df_all[['Odds', 'lowTemp', 'highTemp', 'precipitation', 'final_place', 'PP']]
# below creates 2 new new columns
df_all['averageTemp'] = df_all['lowTemp'] + df_all['highTemp']
df_all['averageTemp'] = df_all['averageTemp'] / 2

# removes 2 columns
df_all = df_all.drop(['lowTemp','highTemp'], axis=1)

pca = PCA()
components = pca.fit_transform(df_all)
labels = {
    str(i): f"PC {i + 1} ({var:.1f}%)"
    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
}

fig_pca = px.scatter_matrix(components,
                         dimensions=range(4),
                         color=df_all['final_place'],
                         labels=labels,
                         opacity=0.7,
                         title='PCA Scatter Matrix',
                         height=800
                            )
fig_pca.update_traces(diagonal_visible=False)

fig_pca.write_html('D:/Personal/WGU/Capstone_Docs/PCA_scatter.html', include_plotlyjs='cdn')



### script below is for the multi-linear regression model. It writes the figure to a file, then I
### add that figure file to the project
raw = pd.read_csv('data/Merged_RaceData_AllYears.csv')
df_all = raw.fillna(0)

df_all = df_all[['Odds', 'lowTemp', 'highTemp', 'precipitation', 'final_place',
                 'PP', 'trackCondition', 'weather']]
# below creates new averageTemp feature or column
df_all['averageTemp'] = df_all['lowTemp'] + df_all['highTemp']
df_all['averageTemp'] = df_all['averageTemp'] / 2
# below replaces sloppy and muddy with other
df_all['trackCondition'].replace(to_replace='Muddy', value='Sloppy', inplace=True)
df_all['weather'].replace(to_replace='Showery', value='Rainy', inplace=True)
df_all['weather'].replace(to_replace='Foggy', value='Cloudy', inplace=True)

fig = px.scatter(df_all,
                 x='final_place',
                 y='Odds',
                 facet_col='trackCondition',
                 color='weather',
                 trendline='ols')

fig.write_html('D:/Personal/WGU/Capstone_Docs/multiLinear.html', include_plotlyjs='cdn')