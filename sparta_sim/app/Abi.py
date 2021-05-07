import simpy
import random
import statistics

months = int(input('enter the number of months:'))
centres_open = months // 2

trainees = []
centres = []


# Generates trainees in the range of 20-30 every month
def generate_trainees():
    for m in range(0, months):
        trainees_per_month = random.randint(20, 30)
        trainees.append(trainees_per_month)
    return trainees



t = sum(generate_trainees())
print(f'The total number of trainees: {t}')


# Generate training centres every two months
def generate_training_centres():
    for c in range(1, centres_open + 1):
        centres.append(c)
    return centres


print(generate_training_centres())
print(f'The number of training centres open: {centres_open}')
item = []


def generate_full_centres():
    sums=0
    for value in trainees:

        if sums <= 100:
            sums = sums + value

        elif sums > 100:
            item.append(100)
            sums = sums - 100

    return item


fc=generate_full_centres()
print(f'The number of full centres are :{fc}')

waiting_list = []


def waiting_trainees():
    return sum(waiting_list)
