""" Write a Python program that receives from the user the length of a movie in
minutes and prints how many hours and how many minutes
The movie continues. For example:
- If the length of the recorded film is - 70, then the answer will be 1 hour and 10 minutes
- If the length of the recorded film is - 160, then the answer will be 2 hours and 40 minutes
- If the length of the recorded film is - 180, then the answer will be 3 hours and 0 minutes
- etc."""

lmin: int = int(input("Please enter the duration of the movie in minutes: "))

hours = lmin // 60
minutes = lmin % 60

print(f'The movie is {hours} hours and {minutes} minutes long!')