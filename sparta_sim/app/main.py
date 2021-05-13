from sparta_sim.app.config_input import *
from classes import *
from random import choice

academy_list = []
type_of_academy = ['hub', 'bootcamp', 'tech']
num_of_hub = 0
num_of_bootcamp = 0
trainee_type = ['Java', 'Csharp', 'DevOps', 'Data', 'Business']

for months in range(1, total_time + 1):
    if (months + 1) % 2 == 0:
        centre_open = choice(type_of_academy)
        if centre_open == 'hub' and num_of_hub < 3:
            academy_list.append(TrainingHub())
            num_of_hub += 1
        elif centre_open == 'bootcamp' and num_of_bootcamp < 2:
            academy_list.append(Bootcamp())
            num_of_bootcamp += 1
        elif centre_open == 'tech':
            trainees = choice(trainee_type)
            academy_list.append(TechCentre(trainees))

    trainee_list = trainee_generator(min_trainees, max_trainees)
    placed = choice(academy_list)
    placed.update_trainees(trainee_list, months)
    for academy in academy_list:
        academy.increment_trainees()
        print(academy.get_trainees())

