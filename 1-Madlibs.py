# 1-Madlibs project: String concatenation
# We want to create a string that says "subscribe to ____"

# Create a variable for the string
# youtuber = "Auron"

# A few ways to create the string "subscribe to "
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adjective = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adjective}! It makes me so excited all the " \
         f"because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}."

print(madlib)