import numpy
import csv

class League():
    def __init__(self):
        """ Initialises the league. Currently all of the players and their variables are hardcoded """
        self.player_1 = Player(name='Anthony', wins=6, losses=8, draws=0, points_for=11852, points_against=12030, scores=[765,801,821,901,832,817,797,828,893,809,896,814,970,908])
        self.player_2 = Player(name='Ben', wins=3, losses=11, draws=0, points_for=10664, points_against=11946, scores=[821,735,738,789,875,559,905,848,733,640,865,790,685,681])
        self.player_3 = Player(name='Daniel', wins=8, losses=6, draws=0, points_for=12779, points_against=11914, scores=[852,911,900,879,884,771,999,1086,798,1019,909,871,892,1008])
        self.player_4 = Player(name='Henry', wins=8, losses=6, draws=0, points_for=11755, points_against=11700, scores=[879,916,767,764,783,834,838,796,782,778,1020,996,829,773])
        self.player_5 = Player(name='Jacob', wins=10, losses=4, draws=0, points_for=11786, points_against=11275, scores=[928,836,743,820,857,870,878,942,833,838,813,901,702,825])
        self.player_6 = Player(name='Jarrod', wins=10, losses=4, draws=0, points_for=11988, points_against=10983, scores=[681,979,891,870,773,828,862,838,851,857,942,975,952,689])
        self.player_7 = Player(name='Joshua', wins=5, losses=9, draws=0, points_for=11723, points_against=11763, scores=[852,835,817,915,793,748,892,817,787,873,924,869,729,872])
        self.player_8 = Player(name='Jules', wins=4, losses=10, draws=0, points_for=10892, points_against=11863, scores=[523,747,822,547,823,752,784,713,864,715,904,867,983,848])
        self.player_9 = Player(name='Luke', wins=11, losses=3, draws=0, points_for=11992, points_against=11419, scores=[948,905,862,761,880,782,775,873,877,831,686,994,871,947])
        self.player_10 = Player(name='Matt', wins=6, losses=8, draws=0, points_for=11547, points_against=12062, scores=[865,865,875,855,816,776,824,816,870,828,784,758,781,834])
        self.player_11 = Player(name='Nathan', wins=6, losses=8, draws=0, points_for=11736, points_against=11724, scores=[830,800,786,977,821,775,870,688,905,877,854,847,820,886])
        self.player_12 = Player(name='Ned', wins=7, losses=7, draws=0, points_for=11996, points_against=11829, scores=[660,889,816,760,831,895,815,943,972,682,877,820,1003,1033])
        self.player_13 = Player(name='Nick', wins=5, losses=9, draws=0, points_for=11270, points_against=11901, scores=[872,865,746,675,785,865,848,785,825,804,827,851,842,680])
        self.player_14 = Player(name='Noah', wins=9, losses=5, draws=0, points_for=12374, points_against=11945, scores=[814,952,826,840,931,981,772,769,787,945,864,978,1043,872])

    def __repr__(self):
        output = ''
        for pos,player in self.ladder().items():
            output += str(pos).zfill(2) + ' ' + player.__repr__() + '\n'
        return output

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
        elif knockout == True:
            if player_1 > player_2:
                winner = player_1
                loser = player_2
            elif player_1 < player_2:
                winner = player_2
                loser = player_1
            else: # Draw with the exact same percentage. Should use points for as the next decider but raises an error for now
                raise Exception(player_1.name + ' and ' + player_2.name + ' could not be separated')
        else: # Draw
            return None, None
        return winner, loser

    def update_ladder(self, player_1, player_1_score, player_2, player_2_score):
        """ Updates the league ladder """
        player_1.points_for += player_1_score
        player_2.points_for += player_2_score
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

    def simulate_finals_week_1(self):
        # Finals Week 1
        ladder = self.ladder()
        winner_1, loser_1 = self.simulate_match(player_1=ladder[1], player_2=ladder[4], knockout=True)
        winner_2, loser_2 = self.simulate_match(player_1=ladder[2], player_2=ladder[3], knockout=True)
        winner_3, loser_3 = self.simulate_match(player_1=ladder[5], player_2=ladder[8], knockout=True)
        winner_4, loser_4 = self.simulate_match(player_1=ladder[6], player_2=ladder[7], knockout=True)
        return winner_1, winner_2, winner_3, winner_4, loser_1, loser_2, loser_3, loser_4

    def simulate_finals_week_2(self, winner_3, winner_4, loser_1, loser_2):
        # Finals Week 2
        winner_5, loser_5 = self.simulate_match(player_1=loser_1, player_2=winner_3, knockout=True)
        winner_6, loser_6 = self.simulate_match(player_1=loser_2, player_2=winner_4, knockout=True)
        return winner_5, winner_6, loser_5, loser_6

    def simulate_finals_week_3(self, winner_1, winner_2, winner_5, winner_6):
        # Finals Week 3
        winner_7, loser_7 = self.simulate_match(player_1=winner_1, player_2=winner_6, knockout=True)
        winner_8, loser_8 = self.simulate_match(player_1=winner_2, player_2=winner_5, knockout=True)
        return winner_7, winner_8, loser_7, loser_8

    def simulate_finals_week_4(self, winner_7, winner_8):
        # Grand Final
        winner, runner_up = self.simulate_match(player_1=winner_7, player_2=winner_8, knockout=True)
        return winner, runner_up

    def simulate_finals(self):
        """ Simulates all finals games and returns the winner and runner up """
        winner_1, winner_2, winner_3, winner_4, loser_1, loser_2, loser_3, loser_4 = self.simulate_finals_week_1()
        winner_5, winner_6, loser_5, loser_6 = self.simulate_finals_week_2(winner_3=winner_3, winner_4=winner_4, loser_1=loser_1, loser_2=loser_2)
        winner_7, winner_8, loser_7, loser_8 = self.simulate_finals_week_3(winner_1=winner_1, winner_2=winner_2, winner_5=winner_5, winner_6=winner_6)
        winner, runner_up = self.simulate_finals_week_4(winner_7=winner_7, winner_8=winner_8)
        return winner, runner_up

    def simulate_season(self):
        """ Simulates the remainder of the season """
        # self.simulate_round_12()
        # self.simulate_round_13()
        # self.simulate_round_14()
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
    def __init__(self, name, wins, losses, draws, points_for, points_against, scores):
        """ Initialises a player and all required variables """
        self.name = name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.points_for = points_for
        self.points_against = points_against
        self.scores = scores

        self.mean = sum(self.scores) / len(self.scores)
        self.standard_deviation = numpy.std(self.scores)

    def __repr__(self):
        return self.name.zfill(7) + ' - ' + str(self.ladder_points()).zfill(2) + ' ' + str(self.wins).zfill(2) + ' ' + str(self.draws).zfill(2) + ' ' + str(self.losses).zfill(2) + ' ' + str(round(self.percent(), 2)) + '%'

    def __gt__(self, other):
        """ Determines which player is higher on the ladder """
        points_1 = self.ladder_points()
        points_2 = other.ladder_points()
        if points_1 > points_2:
            return True
        elif points_1 < points_2:
            return False
        else:
            if self.percent() > other.percent():
                return True
            else:
                return False

    def ladder_points(self):
        """ Calculate a players ladder points """
        return 4 * self.wins + 2 * self.draws

    def sample(self):
        """ Generates a weekly score from a Normal Distribution using a players mean and standard deviation """
        sample = round(numpy.random.normal(loc=self.mean, scale=self.standard_deviation))
        return sample

    def percent(self):
        """ Calculates a players percentage """
        return 100 * self.points_for / self.points_against

def generate_probabilities(samples):
    league = League()
    players = league.players()
    for player in players:
        print(player.name.zfill(7), 'Mean:', round(player.mean, 2), 'SD:', round(player.standard_deviation,2))
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
