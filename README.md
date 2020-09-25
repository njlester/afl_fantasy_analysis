# AFL Fantasy Simulation

## What is AFL Fantasy
AFL Fantasy is a

## What the simulation does
Simulates the remainder of the 2020 AFL Fantasy season

## How it works
The remainder of the season has been coded in, i.e. who plays who each week as
well as finals matchups determined by ladder position
Each players observed weekly scores for the year are used to calculate a players
mean and standard deviation
As a players score is independent from their opponents score, each player was
assigned their own normal distribution with mean and standard deviation
calculated from their observed weekly scores.

Every game between two players were simulated by sampling each players score from
their normal distributions. The player with the highest score wins the game.


It works based off one assumption
