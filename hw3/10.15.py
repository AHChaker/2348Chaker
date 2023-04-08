#Hamid Chaker 2060843
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

if __name__ == "__main__":
    student_team = Team()

    teamname = input()
    teamwins = int(input())
    team_losses = int(input())

    student_team.team_name = teamname
    student_team.team_wins = teamwins
    student_team.team_losses = team_losses

    if student_team.get_win_percentage() < 0.5:
        print(f'Team {student_team.team_name} has a losing average.')
    else:
        print(f"Congratulations, Team {student_team.team_name} has a winning average!")
