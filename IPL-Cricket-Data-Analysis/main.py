import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
matches = pd.read_csv("data/matches.csv")

# Display first 5 rows
print(matches.head())

# Count team wins
team_wins = matches['winner'].value_counts()

print(team_wins)

# Create bar chart
team_wins.plot(kind='bar')

plt.title("IPL Team Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.show()


# Toss winner analysis
toss_wins = matches['toss_winner'].value_counts()

print(toss_wins)

# Toss winner graph
toss_wins.plot(kind='bar')

plt.title("Toss Wins by Teams")
plt.xlabel("Teams")
plt.ylabel("Toss Wins")

plt.show()

# Top player of the match winners
top_players = matches['player_of_match'].value_counts().head(10)

print(top_players)

# Graph
top_players.plot(kind='bar')

plt.title("Top 10 Player of the Match Winners")
plt.xlabel("Players")
plt.ylabel("Awards")

plt.show()

# Top venues
venues = matches['venue'].value_counts().head(10)

print(venues)

venues.plot(kind='bar')

plt.title("Top IPL Venues")
plt.xlabel("Venue")
plt.ylabel("Matches")

plt.show()