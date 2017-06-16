
# Functions and Function Design 

def readable_timedelta(days):
    """Print the number of weeks and days in a number of days."""
    #to get the number of weeks we use integer division
    weeks = days // 7
    #to get the number of days that remain we use %, the modulus operator
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def welcome_message(name):
#Prints out a personalised welcome message
    return "Welcome to this Python script, " + name + "!"

#Call the welcome message function with the input "Udacity Student" 
#and print the output
print(welcome_message("Luka"))



def which_prize(points):
    
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"

print(which_prize(77))
# Out: Oh dear, no prize this time.

def which_prize2(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 150 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."


# Case Study: Scores To Rating Function Design

        
def convert_to_numeric(score):
    """
    Convert the score to a float.
    """
    converted_score = float(score)
    return converted_score

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    max_score = max(score1,score2,score3,score4,score5)
    min_score = min(score1,score2,score3,score4,score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum


def score_to_rating_string(av_score):
    """
    Convert the average score, which should be between 0 and 5, 
    into a rating.
    """
    if av_score < 1:
        rating = "Terrible"
    elif av_score < 2:
        rating = "Bad"
    elif av_score < 3:
        rating = "OK"
    elif av_score < 4:
        rating = "Good"
    else:          #Using else at the end, every possible case gets caught
        rating = "Excellent"
    return rating

# Trick: Mutable default Arguments

def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list
todo_list('check the mail')
# Out: ['wake up','check the mail']
todo_list('running')
# Out: ['wake up','check the mail','running']
# Lists are mutable objects. This list object is used everytime the function is called, it isn't redefined each time.





