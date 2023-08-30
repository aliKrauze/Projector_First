import pandas as pd

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"

df = pd.read_csv(url)

selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print(selected_columns)

num_teams = df['Team'].nunique()
print("Number of teams participated in Euro2012:", num_teams)

teams_with_more_than_6goals = df[df['Goals'] > 6]

print("Teams that scored more than 6 goals:")
print(teams_with_more_than_6goals[['Team', 'Goals']])