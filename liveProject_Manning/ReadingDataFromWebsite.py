import pandas as pd

url = 'https://en.wikipedia.org/wiki/NBA_All-Star_Game'
df = pd.read_html(url)[2]
df = df.head(40)
df.dropna(inplace=True)

westResults = []
eastResults = []

result = pd.DataFrame(columns=['Year','East','West','Host city'])
for value in df['Result']:
    winner = value.split(',')[0]
    loser = value.split(',')[1]
    if 'West' in winner:
        westResults.append(''.join(x if x.isdigit() else '' for x in winner))
        eastResults.append(''.join(x if x.isdigit() else '' for x in loser))
    elif 'East' in winner:
        eastResults.append(''.join(x if x.isdigit() else '' for x in winner))
        westResults.append(''.join(x if x.isdigit() else '' for x in loser))

result['Year'] = df.Year
result['East'] = eastResults
result['West'] = westResults
result['Host city'] = [x.split(',')[0] for x in df['Host city']]
result = result.set_index('Year')
result[['East','West']] = result[['East','West']].apply(pd.to_numeric)
result['diff'] = abs(result['East'] - result['West'])
groups = result.groupby('diff')
print('Prepared data')
print(result)
print('-'*30)
print('Group by point difference')
print(groups.get_group(5))
print('-'*30)
print('Host City')
hostCity = result.groupby('Host city').mean()
hostCity['Counts'] = (result['Host city'].value_counts(ascending=True).sort_index(axis=0))
print(hostCity)
print('-'*30)
print('Group by Host City')
groups = hostCity.groupby('Counts')
print(groups.filter(lambda x: x['Counts'].mean() >=2))


