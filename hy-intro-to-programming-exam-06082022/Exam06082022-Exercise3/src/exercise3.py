# Write your solution to exercise 3 here
def points(stats: str):
   # statistics in the format: [team]:[wins]-[losses]-[ties]
   name_and_numbers = stats.split(":")
   wins_losses_ties = name_and_numbers[1].split("-")

   # if wins, losses or ties are not readable integers, raise ValueError.
   try:
      wins = int(wins_losses_ties[0])
      losses = int(wins_losses_ties[1])
      ties = int(wins_losses_ties[2])
      # win = 3 points
      # loss = 0 point
      # tie = 1 point
      points = wins * 3 + losses * 0 + ties * 1
   except:
      raise ValueError ("Something wrong with the stats")
   
   return points

# if __name__ == "__main__":
#    print(points("Sleepers:0-0-0"))
