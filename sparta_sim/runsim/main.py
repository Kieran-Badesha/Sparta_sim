from typing import Union
from runsim.config_input import total_time, min_trainees, max_trainees
from runsim.classes import TrainingHub, Bootcamp, TechCentre, trainee_generator
from random import choice


def main():
    academy_list = []
    type_of_academy = ['hub', 'bootcamp', 'tech']
    num_of_hub = 0
    num_of_bootcamp = 0
    trainee_type = ['Java', 'Csharp', 'DevOps', 'Data', 'Business']
    finished_trainees = {
                        'Java': 0,
                        'Data': 0,
                        'CSharp': 0,
                        'DevOps': 0,
                        'Business': 0
                        }
    queued_trainees = []

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

        generated_trainees = trainee_generator(min_trainees, max_trainees)
        
        trainee_list = generated_trainees + queued_trainees
        
        fill_academys(academy_list, months, trainee_list)

        finished_trainees, queued_trainees = increment_academys(academy_list,
                                                        finished_trainees, 
                                                        queued_trainees)
    
    print('List of Academies:\n')
    output_objects(academy_list)
    print('\nAmount of Finished Trainees:')
    print(finished_trainees)
    print('\nQueued Trainees: ')
    output_objects(queued_trainees)
        
        
def increment_academys(academy_list: list, finished_trainees: dict, 
            queued_trainees: list) -> list and dict:
    for academy in academy_list:
        academy.increment_trainees()
        finished_dict = academy.get_finished_trainees()
        queued_list = academy.get_queue()

        for group, count in finished_dict.items():
            finished_trainees[group] += count
        
        if queued_list:
            for group in queued_list:
                queued_trainees.append(group)
            
    return finished_trainees, queued_trainees


def fill_academys(academy_list: list, months: int, trainee_list: list) -> None:
    placed = choice(academy_list)
    placed.update_trainees(trainee_list, months)


def output_objects(item_list: list):
    for item in item_list:
        print(f'{item}')
