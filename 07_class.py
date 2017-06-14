# class

# define a class: Car()
class Car():
    def __init__(self):
        self.color = "black"
        self.make = "honda"
        self.model = "accord"

black_honda_accord = Car()

print(black_honda_accord.color)

# define a class: Team()
class Team():
    def __init__(self,name):
        self.name = name
giants = Team('New York Giants')


# Count the team winner number
import csv
class Team():
    
    def __init__(self, name): 
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
jaguars = Team('Jacksonville Jaguars')
jaguars_wins = jaguars.count_total_wins()
