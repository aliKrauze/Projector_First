import random
import csv


def simulate_rounds(total_rounds):
    players_names = {'Nicole': 0, 'Andrew': 0,
                    'Antony': 0, 'Ann': 0, 'Svetla': 0}
    for i in range(1, total_rounds+1):
        for player in players_names:
            round_score = random.randint(0, 1000)
            players_names[player] = round_score

    return players_names


def save_to_file(players_names, user_score_file):
    with open(user_score_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Player name', 'Score'])
        for player, score in players_names.items():
            writer.writerow([player, score])


if __name__ == "__main__":
    total_rounds = 100
    player_score = simulate_rounds(total_rounds)
    save_to_file(player_score, 'user_score_file.csv')
