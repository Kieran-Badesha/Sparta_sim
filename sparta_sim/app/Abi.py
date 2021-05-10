import random

months = int(input('enter the number of months:'))
centres_open = months // 2

trainees = []
centres = []


# Generates trainees in the range of 20-30 every month
def generate_trainees():
    for m in range(0, months):
        trainees_per_month = random.randint(20, 30)
        trainees.append(trainees_per_month)
    print(trainees)
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

fc = []


# Generate the number of full centres
def generate_full_centres():
    sum_of_trainees = 0
    # this for loop is to generate the batches of 100 trainees
    for i in trainees:
        sum_of_trainees += i

        if sum_of_trainees <= 100:
            pass

        # this appends 100 to the fc list everytime the sum_of_trainees exceeds a 100
        else:
            fc.append(100)
            sum_of_trainees -= 100

    # compares the number of batches to the centres open
    if len(fc) <= centres_open:
        return len(fc)

    else:
        return centres_open


gfc = generate_full_centres()
print(f'The number of centres full are :{gfc}')

# to generate the number of trainees in the waiting list

waiting_list = []


def waiting_trainees():
    return sum(waiting_list)


# surplus trainees added to the waiting list
if t > centres_open * 100:
    surplus_trainees = t - (centres_open * 100)
    waiting_list.append(surplus_trainees)
# this is just a placeholder for the code
else:
    pass
print(waiting_list)
