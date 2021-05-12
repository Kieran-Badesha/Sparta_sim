from numpy.random import binomial
# Sim Class

class Simulation:
    pass

# Academy Classes


class Academy:
    def __init__(self):
        pass


class TrainingHub(Academy):

    def __init__(self):
        super().__init__()


class Bootcamp(Academy):

    def __init__(self):
        super().__init__()


class TechCentre(Academy):

    def __init__(self):
        super().__init__()


# Trainee Classes
def trainee_generator(min_trainees, max_trainees):

    course_probabilities = {
                            'Java': 0.2,
                            'Data': 0.25,
                            'CSharp': 1/3,
                            'DevOps': 0.5,
                            'Business': 1
                            }

    trainee_range = max_trainees - min_trainees
    trainees_per_month = int(binomial(n=trainee_range, p=0.5, size=1))
    num_of_trainees = min_trainees + trainees_per_month

    if num_of_trainees > max_trainees:
        num_of_trainees = max_trainees

    trainees = {}

    for course, prob in course_probabilities.items():
        x = binomial(num_of_trainees, prob)

        num_of_trainees -= x

        trainees[course] = {'Count': x,
                            'Months Trained': 0}

    return trainees




print(trainee_generator())
