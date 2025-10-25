class NFLteam:
    def __init__ (self, team_name, list_of_players):
        self.team_name = team_name
        self.list_of_players = list_of_players

    def player_resume(self):
        print(f"Team: {self.team_name}")
        print("Players:")
        for player in self.list_of_players:
            print(f"Player: {player.player_name}\n", f"Position: {player.player_position}")

class Players:
    def __init__ (self, player_name, player_position):
        self.player_name = player_name
        self.player_position = player_position

joe_montana = Players("Joe Montana", "QuarterBack")
barry_sanders = Players("Barry Sanders", "Running Back")
jerry_rice = Players("Jerry Rice", "Wide Receiver")
graham_gano = Players("Graham Gano", "Kicker")

final_team = [joe_montana, barry_sanders, jerry_rice, graham_gano]
atlanta_inferno = NFLteam("Atlanta Inferno", final_team)

atlanta_inferno.player_resume()