class Team:
    def __init__(self):
        self.teamname = 'none'
        self.teamwins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        team_score = self.teamwins / (self.teamwins + self.team_losses)
        return team_score


if __name__ == "__main__":

    student_team = Team()

    teamname = input()
    teamwins = int(input())
    team_losses = int(input())

    student_team.teamname = teamname
    student_team.teamwins = teamwins
    student_team.team_losses = team_losses

    win_percent = student_team.get_win_percentage()

    if win_percent < 0.5:
        print(f'Team {student_team.teamname} has a losing average.')
    elif win_percent >= 0.5:
        print(f"Congratulations, Team {student_team.teamname} has a winning average!")
