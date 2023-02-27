import math
import tkinter as tk
import random
import numpy as np
from tkinter import ttk


teams = {
    'Arsenal FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Manchester City FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Manchester United FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Brighton and Hove Albion': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Newcastle United': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Liverpool FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Chelsea FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Tottenham Hotspur': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Aston Villa FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'West Ham United': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Leicester City FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Nottingham Forest': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Everton FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Crystal Palace FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Wolverhampton Wanderers': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Leeds United FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'AFC Bournemouth': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Southampton FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Fulham FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0},
    'Brentford FC': {'points': 0, 'games_played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'goal_difference': 0}
    }

probabilities = {
    "Arsenal FC": (0.7, 0.7),
    "Manchester City FC": (1.65, 1.65),
    "Manchester United FC": (0.8, 0.8),
    "Brighton and Hove Albion": (0.45, 0.45),
    "Newcastle United": (0.55, 0.55),
    "Liverpool FC": (0.6, 0.6),
    "Chelsea FC": (0.4, 0.4),
    "Tottenham Hotspur": (0.35, 0.35),
    "Aston Villa FC": (0.3, 0.3),
    "West Ham United": (0.25, 0.25),
    "Leicester City FC": (0.2, 0.2),
    "Nottingham Forest": (0.1, 0.1),
    "Everton FC": (0.15, 0.15),
    "Crystal Palace FC": (0.23, 0.23),
    "Wolverhampton Wanderers": (0.34, 0.34),
    "Leeds United FC": (0.2, 0.2),
    "AFC Bournemouth": (0.2, 0.2),
    "Southampton FC": (0.1, 0.1),
    "Fulham FC": (0.2, 0.2),
    "Brentford FC": (0.1, 0.1)
    }


def enter_scores(home_team, away_team, probabilities, teams):
    home_attack, home_defense = probabilities[home_team]
    away_attack, away_defense = probabilities[away_team]

    # Calculate expected goals for each team
    home_expected_goals = expected_goals(home_attack, away_defense)
    away_expected_goals = expected_goals(away_attack, home_defense)

    # Generate random scores using Poisson distribution
    home_goals = np.random.poisson(home_expected_goals)
    away_goals = np.random.poisson(away_expected_goals)

    # Update team statistics based on game outcome
    teams[home_team]['goals_for'] += home_goals
    teams[away_team]['goals_for'] += away_goals
    teams[home_team]['goals_against'] += away_goals
    teams[away_team]['goals_against'] += home_goals
    teams[home_team]['games_played'] += 1
    teams[away_team]['games_played'] += 1
    teams[home_team]['goal_difference'] = teams[home_team]['goals_for'] - teams[home_team]['goals_against']
    teams[away_team]['goal_difference'] = teams[away_team]['goals_for'] - teams[away_team]['goals_against']
	
    if home_goals > away_goals:
        teams[home_team]['points'] += 3
        teams[home_team]['wins'] += 1
        teams[away_team]['losses'] += 1
    elif home_goals < away_goals:
        teams[away_team]['points'] += 3
        teams[away_team]['wins'] += 1
        teams[home_team]['losses'] += 1
    else:
        teams[home_team]['points'] += 1
        teams[away_team]['points'] += 1
        teams[home_team]['draws'] += 1
        teams[away_team]['draws'] += 1

    print(f"{home_team} {home_goals} : {away_goals} {away_team}")

def expected_goals(attack_strength, defense_strength):
    return math.exp(attack_strength + defense_strength) / (1 + math.exp(attack_strength + defense_strength))

def simulate_matches(teams, probabilities):
    # Generate all possible matchups
    matchups = [(home_team, away_team) for home_team in teams.keys() for away_team in teams.keys() if home_team != away_team]
    
    
    # Shuffle the matchups to randomize the order of games played
    #random.shuffle(matchups)


    for home_team, away_team in matchups:
        enter_scores(home_team, away_team, probabilities, teams)



    # Sort teams by points, then by goal difference, then by goals scored
    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]['points'], -x[1]['goals_for'] + x[1]['goals_against'], -x[1]['goals_for']))

    # Return the sorted teams
    return sorted_teams
   
    
# Simulate matches and get sorted teams
sorted_teams = simulate_matches(teams, probabilities)


def display_league_table():
    # Create the Tkinter window
    window = tk.Tk()
    window.title("Premier League Table")

    # Create the Treeview widget
    table = ttk.Treeview(window)

    # Define the columns of the table
    table['columns'] = ('points', 'games_played', 'wins', 'draws', 'losses', 'goals_for', 'goals_against', 'goal_difference')

    # Format the columns
    table.column('#0', width=300)
    table.column('points', width=100)
    table.column('games_played', width=100)
    table.column('wins', width=100)
    table.column('draws', width=100)
    table.column('losses', width=100)
    table.column('goals_for', width=100)
    table.column('goals_against', width=120)
    table.column('goal_difference', width=100)

    # Create the headings for the columns
    table.heading('#0', text='Teams')
    table.heading('points', text='Points')
    table.heading('games_played', text='GP')
    table.heading('wins', text='W')
    table.heading('draws', text='D')
    table.heading('losses', text='L')
    table.heading('goals_for', text='GF')
    table.heading('goals_against', text='GA')
    table.heading('goal_difference', text='GD')
    # Insert the data into the table
    for team, stats in sorted_teams:
        table.insert('', 'end', text=team, values=(stats['points'], stats['games_played'], stats['wins'], stats['draws'], stats['losses'], stats['goals_for'], stats['goals_against'], stats['goal_difference']))

    # Pack the table and run the window
    table.pack()
    window.mainloop()

sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]['points'], -x[1]['goals_for'] + x[1]['goals_against'], -x[1]['goals_for']))

# Show the league table
display_league_table()

