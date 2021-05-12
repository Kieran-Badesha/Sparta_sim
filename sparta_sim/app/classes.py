from numpy.random import binomial

# Sim Class
class Simulation:
    pass
# Academy Classes

class Academy:
    def __init__(self):
        self.__trainees = {}
        self.__finished_trainees = {
                                    'Java': 0,
                                    'Data': 0,
                                    'CSharp': 0,
                                    'DevOps': 0,
                                    'Business': 0
                                    }
        self.__total_trainees = 0
        self.__capacity = 100

    def update_trainees(self, trainee_dict: dict, month: int):
        self.queued_trainees = None
        trainee_dict_total = sum(count['Count'] 
                                for count in trainee_dict.values()
                                )
        spaces = self.__capacity - self.__total_trainees

        if trainee_dict_total > spaces:
            self.__trainees[f'group_{month}'] = {}

            used_group = []

            for trainee in trainee_dict:

                if (spaces - trainee_dict[trainee]['Count']) >= 0:
                    self.__trainees[f'group_{month}'][trainee] = (
                                                        trainee_dict[trainee])

                    spaces -= trainee_dict[trainee]['Count']
                    used_group.append(trainee)
            
            for group in used_group:
                trainee_dict.pop(group)
            
            self.queued_trainees = trainee_dict

        else:
            self.__trainees[f'group_{month}'] = trainee_dict
    
    def increment_trainees(self):
        for group in self.__trainees.keys():
            
            for trainees in self.__trainees[group].keys():

                if self.__trainees[group][trainees]['Months Trained'] == 11:
                    self.__finished_trainees[trainees] += (
                                    self.__trainees[group][trainees]['Count'])

                    self.__trainees[group][trainees]['Months Trained'] += 1
                
                elif self.__trainees[group][trainees]['Months Trained'] < 11:
                    self.__trainees[group][trainees]['Months Trained'] += 1
                
        self.__update_trainee_count()
        
            
    def get_finished_trainees(self):
        return sum(self.__finished_trainees.values())
    
    def get_trainees(self):
        return self.__trainees
    
    def __update_trainee_count(self):
        self.__total_trainees = 0
        for group in self.__trainees.keys():

            for trainees in self.__trainees[group].keys():

                if self.__trainees[group][trainees]['Months Trained'] != 12: 
                    self.__total_trainees += (
                                    self.__trainees[group][trainees]['Count']) 

    def get_trainee_count(self):
        self.__update_trainee_count()
        return self.__total_trainees
    
    def get_queue(self):
        return self.queued_trainees

class TrainingHub(Academy):
    def __init__(self):
        super().__init__()

class Bootcamp(Academy):
    def __init__(self):
        super().__init__()
        self.__capacity = 500

class TechCentre(Academy):
    def __init__(self, trainee_type):
        super().__init__()
        self.__capacity = 200
        self.__trainee_type = trainee_type


# Trainee Generator
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

        while x == 0:
            x = binomial(num_of_trainees, prob)

        num_of_trainees -= x

        trainees[course] = {'Count': x,
                            'Months Trained': 0}

    return trainees
