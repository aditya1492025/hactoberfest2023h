import requests
from bs4 import BeautifulSoup

def get_live_score(match_url):
  """Gets the live score of a match from the Cricbuzz website.

  Args:
    match_url: The URL of the match page on the Cricbuzz website.

  Returns:
    A dictionary containing the live score data.
  """

  response = requests.get(match_url)
  soup = BeautifulSoup(response.content, "html.parser")

  scoreboard = soup.find("div", class_="scorecard-container")
  teams = scoreboard.find_all("div", class_="team-info")
  team_scores = []
  for team in teams:
    team_score = team.find("span", class_="score")
    team_scores.append(team_score.text)

  live_score = {
    "teams": team_scores,
  }

  return live_score

def main():
  """Prints the live score of the match to the console."""

  match_url = "https://www.cricbuzz.com/cricket-match/live-scores"
  live_score = get_live_score(match_url)

  print(f"Live score:")
  print(f"{live_score['teams'][0]} {live_score['teams'][1]}")

if __name__ == "__main__":
  main()
