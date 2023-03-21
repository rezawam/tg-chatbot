import random

replicas_love = [
    # some data here
    "Ты лучший в мире парень, закинешь мне на карту 300 рублей?"
]

replicas_horny = [
    # some data here
    "Я бы приехала к тебе, но у меня нет денег на такси..."
]

def random_love():
    return random.choice(replicas_love)

def random_horny():
    return random.choice(replicas_horny)
