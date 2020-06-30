

import random


for i in range(10):
    print(random.random())


for i in range(10):
    print(random.uniform(3,7))


for i in range(10):
    print(random.randint(1,6))


outcomes = ["rock", "paper", "scissors"]


for i in range(5):
    print(random.choice(outcomes))
