import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
#What did you see on line 1?
#What was the smallest number you could have seen, what was the largest?
#I see number and the smallest is 8 and biggest is 20

#What did you see on line 2?
#What was the smallest number you could have seen, what was the largest?
#Could line 2 have produced a 4?
# The number always in range of 2. The smallest is 3 and biggest 9. It will not produce a 4. It will only produce 3,5,7,9

#What did you see on line 3?
#What was the smallest number you could have seen, what was the largest?
# I see a float. the smallest number is 3.477464325785493. largest is 4.7999026124251625

#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,101))