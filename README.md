# AFL Fantasy Simulation

## What is AFL Fantasy
AFL Fantasy is an online game where participants assemble an imaginary team of real life AFL players.
Each AFL player scores points based on their actual statistical performance on the field of play throughout the AFL season.
Participants in a league are pitched against each other each week, with the winner determined by the highest scoring team.

## How the simulation works
Participant matchups for the remainder of the regular season have been coded in, as well as keeping track of the league ladder allowing finals matchups to be determined by ladder position.
Each participants observed weekly scores for the year is used to calculate their mean and standard deviation.
As a participants score is independent from their opponents score, each player was assigned their own normal distribution using their own mean and standard deviation.
Every game for the remainder of the season can then be simulated by sampling two opposing participants scores from their normal distributions. The participant with the highest score wins the game.
Points for, points against, wins, draws and losses are also accounted for to allow an accurate finals series simulation.

## Output
The simulation outputs two CSV files:
1. The probability of each player finishing the regular season in each ladder position
2. The probability of each player winning the grand final or being the runner-up

## Assumptions
The simulation is based off one assumption; a players weekly score is normally distributed!
