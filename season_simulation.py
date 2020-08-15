import numpy
import csv

class League():
    def __init__(self):
        """ Initialises the league. Currently all of the players and their variables are hardcoded """
        self.player_1 = Player(name='Anthony', wins=4, losses=7, draws=0, scores=[765,801,821,901,832,817,797,828,893,809,896], points_against=9417)
        self.player_2 = Player(name='Ben', wins=3, losses=8, draws=0, scores=[821,735,738,789,875,559,905,848,733,640,865], points_against=9455)
        self.player_3 = Player(name='Daniel', wins=6, losses=5, draws=0, scores=[852,911,900,879,884,771,999,1086,798,1019,909], points_against=9403)
        self.player_4 = Player(name='Henry', wins=5, losses=6, draws=0, scores=[879,916,767,764,783,834,838,796,782,778,1020], points_against=9423)
        self.player_5 = Player(name='Jacob', wins=9, losses=2, draws=0, scores=[928,836,743,820,857,870,878,942,833,838,813], points_against=8691)
        self.player_6 = Player(name='Jarrod', wins=8, losses=3, draws=0, scores=[681,979,891,870,773,828,862,838,851,857,942], points_against=8483)
        self.player_7 = Player(name='Joshua', wins=5, losses=6, draws=0, scores=[852,835,817,915,793,748,892,817,787,873,924], points_against=9032)
        self.player_8 = Player(name='Jules', wins=2, losses=9, draws=0, scores=[523,747,822,547,823,752,784,713,864,715,904], points_against=9208)
        self.player_9 = Player(name='Luke', wins=8, losses=3, draws=0, scores=[948,905,862,761,880,782,775,873,877,831,686], points_against=9185)
        self.player_10 = Player(name='Matt', wins=6, losses=5, draws=0, scores=[865,865,875,855,816,776,824,816,870,828,784], points_against=9288)
        self.player_11 = Player(name='Nathan', wins=5, losses=6, draws=0, scores=[830,800,786,977,821,775,870,688,905,877,854], points_against=9059)
        self.player_12 = Player(name='Ned', wins=6, losses=5, draws=0, scores=[660,889,816,760,831,895,815,943,972,682,877], points_against=8999)
        self.player_13 = Player(name='Nick', wins=4, losses=7, draws=0, scores=[872,865,746,675,785,865,848,785,825,804,827], points_against=9156)
        self.player_14 = Player(name='Noah', wins=6, losses=5, draws=0, scores=[814,952,826,840,931,981,772,769,787,945,864], points_against=9266)

    def simulate_match(self, player_1, player_2, knockout=False):
        """ Simulates a match between two players. Returns the winner followed by the loser """
        player_1_score = player_1.sample()
        player_2_score = player_2.sample()

        if knockout == False:
            self.update_ladder(player_1=player_1, player_1_score=player_1_score, player_2=player_2, player_2_score=player_2_score)

        if player_1_score > player_2_score:
            winner = player_1
            loser = player_2
        elif player_1_score < player_2_score:
            winner = player_2
            loser = player_1
        else: # Draw
            if player_1 > player_2:
                winner = player_1
                loser = player_2
            elif player_1 < player_2:
                winner = player_2
                loser = player_1
            else: # Draw with the exact same percentage. Should use points for as the next decider but raises an error for now
                raise Exception(player_1 + ' and ' + player_2 + ' could not be separated')
        return winner, loser

    def update_ladder(self, player_1, player_1_score, player_2, player_2_score):
        """ Updates the league ladder """
        player_1.scores.append(player_1_score)
        player_2.scores.append(player_2_score)
        player_1.points_against += player_2_score
        player_2.points_against += player_1_score
        if player_1_score > player_2_score:
            player_1.wins += 1
            player_2.losses += 1
        elif player_1_score < player_2_score:
            player_1.losses += 1
            player_2.wins += 1
        else:
            player_1.draws += 1
            player_2.draws += 1

    def simulate_round_12(self):
        """ Simulates round 12 matches """
        self.simulate_match(player_1=self.player_3, player_2=self.player_6)
        self.simulate_match(player_1=self.player_12, player_2=self.player_5)
        self.simulate_match(player_1=self.player_1, player_2=self.player_10)
        self.simulate_match(player_1=self.player_13, player_2=self.player_14)
        self.simulate_match(player_1=self.player_4, player_2=self.player_8)
        self.simulate_match(player_1=self.player_2, player_2=self.player_11)
        self.simulate_match(player_1=self.player_9, player_2=self.player_7)

    def simulate_round_13(self):
        """ Simulates round 13 matches """
        self.simulate_match(player_1=self.player_3, player_2=self.player_5)
        self.simulate_match(player_1=self.player_6, player_2=self.player_10)
        self.simulate_match(player_1=self.player_12, player_2=self.player_14)
        self.simulate_match(player_1=self.player_1, player_2=self.player_8)
        self.simulate_match(player_1=self.player_13, player_2=self.player_11)
        self.simulate_match(player_1=self.player_4, player_2=self.player_7)
        self.simulate_match(player_1=self.player_2, player_2=self.player_9)

    def simulate_round_14(self):
        """ Simulates round 14 matches """
        self.simulate_match(player_1=self.player_3, player_2=self.player_10)
        self.simulate_match(player_1=self.player_5, player_2=self.player_14)
        self.simulate_match(player_1=self.player_6, player_2=self.player_8)
        self.simulate_match(player_1=self.player_12, player_2=self.player_11)
        self.simulate_match(player_1=self.player_1, player_2=self.player_7)
        self.simulate_match(player_1=self.player_13, player_2=self.player_9)
        self.simulate_match(player_1=self.player_4, player_2=self.player_2)

    def simulate_finals(self):
        """ Simulates all finals games and returns the winner and runner up """
        # Finals Week 1
        ladder = self.ladder()
        winner_1, loser_1 = self.simulate_match(player_1=ladder[1], player_2=ladder[4], knockout=True)
        winner_2, loser_2 = self.simulate_match(player_1=ladder[2], player_2=ladder[3], knockout=True)
        winner_3, loser_3 = self.simulate_match(player_1=ladder[5], player_2=ladder[8], knockout=True)
        winner_4, loser_4 = self.simulate_match(player_1=ladder[6], player_2=ladder[7], knockout=True)

        # Finals Week 2
        winner_5, loser_5 = self.simulate_match(player_1=loser_1, player_2=winner_4, knockout=True)
        winner_6, loser_6 = self.simulate_match(player_1=loser_2, player_2=winner_3, knockout=True)

        # Finals Week 3
        winner_7, loser_7 = self.simulate_match(player_1=winner_1, player_2=winner_6, knockout=True)
        winner_8, loser_8 = self.simulate_match(player_1=winner_2, player_2=winner_5, knockout=True)

        # Grand Final
        winner, runner_up = self.simulate_match(player_1=winner_7, player_2=winner_8, knockout=True)
        return winner, runner_up

    def simulate_season(self):
        """ Simulates the remainder of the season """
        self.simulate_round_12()
        self.simulate_round_13()
        self.simulate_round_14()
        winner, runner_up = self.simulate_finals()
        return winner, runner_up

    def ladder(self):
        """ Returns a dictionary mapping each ladder position to a player """
        players = sorted(self.players(), reverse=True)
        return {n + 1: players[n] for n in range(14)}

    def players(self):
        """ Returns a list of players """
        players = list()
        for n in range(14):
            player = getattr(self, 'player_' + str(n + 1))
            players.append(player)
        return players

class Player():
    def __init__(self, name, wins, losses, draws, scores, points_against):
        """ Initialises a player and all required variables """
        self.name = name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.scores = scores
        self.points_against = points_against

        self.mean = sum(self.scores) / sum([self.wins, self.losses, self.draws])
        self.standard_deviation = numpy.std(self.scores)

    def __repr__(self):
        return self.name + ' - ' + str(self.wins) + ' Wins ' + str(self.draws) + ' Draws ' + str(self.losses) + ' Losses ' + str(self.percent()) + '%'

    def __gt__(self, other):
        """ Determines which player is higher on the ladder """
        points_1 = 4 * self.wins + 2 * self.draws
        points_2 = 4 * other.wins + 2 * other.draws
        if points_1 > points_2:
            return True
        elif points_1 < points_2:
            return False
        else:
            if self.percent() > other.percent():
                return True
            else:
                return False

    def sample(self):
        """ Generates a weekly score from a Normal Distribution using a players mean and standard deviation """
        sample = round(numpy.random.normal(loc=self.mean, scale=self.standard_deviation))
        return sample

    def percent(self):
        """ Calculates a players percentage """
        return sum(self.scores) / self.points_against

def generate_probabilities(samples):
    league = League()
    players = league.players()
    ladder_positions = {player.name: {n + 1: 0 for n in range(14)} for player in players}
    winners = {player.name: 0 for player in players}
    runner_ups = {player.name: 0 for player in players}
    for i in range(samples):
        league = League()
        winner, runner_up = league.simulate_season()
        winners[winner.name] += 1
        runner_ups[runner_up.name] += 1
        ladder = league.ladder()
        for player in ladder_positions.keys():
            for pos,p in ladder.items():
                if player == p.name:
                    ladder_positions[player][pos] = ladder_positions[player].get(pos, 0) + 1
                    break

    with open('ladder_positions.csv', 'w', encoding='UTF-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Name'] + [n + 1 for n in range(14)])
        for player,results in ladder_positions.items():
            results = {pos: 100 * n / samples for pos,n in results.items()}
            writer.writerow([player] + list(results.values()))

    with open('grand_final_results.csv', 'w', encoding='UTF-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Name', '1st', '2nd'])
        for player in winners.keys():
            first_percent = 100 * winners[player] / samples
            second_percent = 100 * runner_ups[player] / samples
            writer.writerow([player, first_percent, second_percent])

if __name__ == '__main__':
    generate_probabilities(samples=10000)
