def main():
    percentage = float(input('Enter your score:')) # get score number
    print(determine_grade_status(percentage)) #output the score status

def determine_grade_status(percentange):
    #determine the grade status
    if percentange < 0 or percentange > 100:
        return 'invalid score'
    elif percentange >= 90:
        return 'HD'
    elif percentange >= 75:
        return 'D'
    elif percentange >= 60:
        return 'C'
    else:
        return 'Bad'




main()