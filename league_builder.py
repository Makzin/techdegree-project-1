import csv
from random import shuffle


def write_to_teams_file(teamname, team):
    with open("teams.txt", "a") as file:
        file.write(("{}".format(teamname))+"\n")
        for player in team:
            file.write("{}, {}, {}".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]) + "\n")
        file.write("\n")

def read_from_input_file():
    with open("soccer_players.csv") as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=",")
        players = list(player_reader)

        #Shuffling ensures randomization, so players don't get assigned to teams in order of having signed up for the league.
        # This also makes sure teams are unique each time the script is re-run.
        shuffle(players)
        return players

def sort_experienced_and_noobs(player_list):
    experienced_players = []
    noobs = []
    for player in player_list:
        if player["Soccer Experience"] == "YES":
            experienced_players.append(player)
        else:
            noobs.append(player)
    return experienced_players, noobs

def sort_players_in_teams(experienced_players, noobs):
    raptors = []
    sharks = []
    dragons = []

    #Possible ideas for future improvement:
    # - if dealing with more than 18 players:
    #   Ask for input to create a new team name and assign players to 4 or more teams instead.
    #   This might require some logic to calculate optimal team balance

    for player in experienced_players:
        if len(raptors) < 3:
            raptors.append(player)
        elif len(sharks) < 3:
            sharks.append(player)
        else:
            dragons.append(player)

    for player in noobs:
        if len(raptors) < 6:
            raptors.append(player)
        elif len(sharks) < 6:
            sharks.append(player)
        else:
            dragons.append(player)

    team_roster = [{
        "Name": "Raptors",
        "Team": raptors
    },{
        "Name": "Sharks",
        "Team": sharks
    }, {
        "Name": "Dragons",
        "Team": dragons
    }]

    return team_roster

def create_guardians_letter(team, player):
    copy = "Dear {}, ".format(player["Guardian Name(s)"]) + "\n" \
    "\n" \
    "I'm happy to welcome {} to Awesometown's Youth Soccer League!".format(player["Name"]) + "\n" \
    "This letter is to inform you that {} has been assigned to Team {}".format(player["Name"], team["Name"]) + "\n" \
    "The first practice will take place on Saturday, January 20 2018 at 9AM." + "\n" \
    "Hope to see you there!" + "\n" \
    "\n" \
    "Kind Regards, " + "\n" \
    "Max Van Lyl"

    player_name = player['Name'].lower()
    formatted_player_name = player_name.replace(" ", "_")
    with open("{}.txt".format(formatted_player_name), "a") as file:
        file.write("{}".format(copy))

def main():
    player_list = read_from_input_file()
    experienced_players, noobs = sort_experienced_and_noobs(player_list)
    team_roster = sort_players_in_teams(experienced_players, noobs)
    for team in team_roster:
        write_to_teams_file(team["Name"], team["Team"])
        for player in team["Team"]:
            create_guardians_letter(team, player)

if __name__ == "__main__":
    main()






