import simpy
import random
import statistics

# months = int(input('enter the number of months:'))
# centres_open=months//2

trainees = []



# Generates trainees in the range of 20-30 every month
def generate_trainees(months):
    for m in range(0, months):
        trainees_per_month = random.randint(20, 30)
        trainees.append(trainees_per_month)
    return trainees

'''
print(generate_trainees())
t = sum(generate_trainees())
print(f'The total number of trainees: {t}')
'''

# Generate training centres every two months
def generate_training_centres(months):
    centres_open = months // 2
    centres = []
    for c in range(1, centres_open + 1):
        centres.append(c)
    return centres_open


print(generate_training_centres())
print(f'The number of training centres open: {centres_open}')



def generate_full_centres():
    fc = []
    for i in trainees:
        sum= sum +i
        if sum<=100:
            fc.append(sum)



waiting_list = []


def waiting_trainees():
    return sum(waiting_list)
