import tkinter as tk
import random

teams = {
    "Arsenal FC": 0,
    "Manchester City FC": 0,
    "Manchester United FC": 0,
    "Newcastle United": 0,
    "Liverpool FC": 0,
    "Brighton and Hove Albion": 0,
    "Chelsea FC": 0,
    "Tottenham Hotspur FC": 0,
    "Aston Villa FC": 0,
    "West Ham United": 0,
    "Leicester City FC": 0,
    "Everton FC": 0,
    "Nottingham Forest": 0,
    "Crystal Palace FC": 0,
    "Wolverhampton Wanderers": 0,
    "AFC Bournemouth": 0,
    "Southampton FC": 0,
    "Leeds United FC": 0,
    "Fulham FC": 0,
    "Brentford FC": 0
}

# Define the probabilities that a team will score a goal
probabilities = {
    "Arsenal FC": 0.7,
    "Manchester City FC": 1.65,
    "Manchester United FC": 0.8,
    "Newcastle United": 0.55,
    "Liverpool FC": 0.6,
    "Brighton and Hove Albion": 0.45,
    "Chelsea FC": 0.4,
    "Tottenham Hotspur FC": 0.35,
    "Aston Villa FC": 0.3,
    "West Ham United": 0.25,
    "Leicester City FC": 0.2,
    "Everton FC": 0.15,
    "Nottingham Forest": 0.1,
    "Crystal Palace FC": 0.23,
    "Wolverhampton Wanderers": 0.34,
    "AFC Bournemouth": 0.2,
    "Southampton FC": 0.1,
    "Leeds United FC": 0.2,
    "Fulham FC": 0.2,
    "Brentford FC": 0.1
}

# Define the maximum number of goals that can be scored in a match
MAX_GOALS = 4

def update_table(home_team, home_score, away_team, away_score, teams):
    # Update the points for the home and away teams
    if home_score > away_score:
        teams[home_team] += 3
    elif home_score == away_score:
        teams[home_team] += 1
        teams[away_team] += 1
    else:
        teams[away_team] += 3

def generate_scores(home_team, away_team):
    # Generate the home team's score based on their probability
    home_score = random.choices(range(0, MAX_GOALS+1), weights=[(1 - probabilities[home_team]) * 5] + [probabilities[home_team] * 5] * MAX_GOALS)[0]

    # Generate the away team's score based on their probability
    away_score = random.choices(range(0, MAX_GOALS+1), weights=[(1 - probabilities[away_team]) * 5] + [probabilities[away_team] * 5] * MAX_GOALS)[0]

    return home_score, away_score

def enter_scores(home_team, away_team, teams):
    # Generate the scores for the match
    home_score, away_score = generate_scores(home_team, away_team)

    # Print the scores for the match
    print(f"{home_team} {home_score} - {away_score} {away_team}")
   
    # Update the league table based on the match scores
    update_table(home_team, home_score, away_team, away_score, teams)



def display_table(teams):
    # Create a new tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("English Premier League")

    # Create a tkinter Label for each team and their points
    for i, (team, points) in enumerate(sorted(teams.items(), key=lambda x: x[1], reverse=True)):
        label = tk.Label(window, text=f"{i+1}. {team}: {points} points")
        label.pack()

    # Start the tkinter main loop
    window.mainloop()

# Generate scores for each match
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f'{home_team} vs {away_team}')
            enter_scores(home_team, away_team, teams)

# Display the league table
display_table(teams)

