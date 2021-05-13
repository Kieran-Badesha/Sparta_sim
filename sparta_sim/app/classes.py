from numpy.random import binomial


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

    def update_trainees(self, trainee_list: list, month: int):
        self.queued_trainees = None
        trainee_list_total = sum(count.get_trainee_count()
                                for count in trainee_list
                                )
        spaces = self.__capacity - self.__total_trainees

        if trainee_list_total > spaces:
            self.__trainees[f'group_{month}'] = []

            used_group = []

            for trainee in range(0, len(trainee_list)):

                if (spaces - trainee_list[trainee].get_trainee_count()) >= 0:
                    self.__trainees[f'group_{month}'].append(
                                                        trainee_list[trainee])

                    spaces -= trainee_list[trainee].get_trainee_count()
                    used_group.append(trainee)
            
                       
            self.queued_trainees = [trainee 
                                    for i, trainee in enumerate(trainee_list) 
                                    if i not in used_group]

        else:
            self.__trainees[f'group_{month}'] = trainee_list
        
        self.__update_trainee_count()

    def increment_trainees(self):
        for group in self.__trainees.keys():
            
            for trainees in range(len(self.__trainees[group])):

                if self.__trainees[group][trainees].get_trained_months() == 11:
                    name = self.__trainees[group][trainees].__class__.__name__
                    self.__finished_trainees[name] += (
                        self.__trainees[group][trainees].get_trainee_count())

                    self.__trainees[group][trainees].increment_training()
                
                elif self.__trainees[group][trainees].get_trained_months() < 11:
                    self.__trainees[group][trainees].increment_training()
                
        self.__update_trainee_count()
          
    def get_finished_trainees(self):
        return self.__finished_trainees
    
    def get_trainees(self):
        return self.__trainees

    def __update_trainee_count(self):
        self.__total_trainees = 0
        for group in self.__trainees.keys():

            for trainees in range(len(self.__trainees[group])):

                if self.__trainees[group][trainees].get_trained_months() != 12: 
                    self.__total_trainees += (
                        self.__trainees[group][trainees].get_trainee_count()) 

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
   
    def update_trainees(self, trainee_list: list, month: int):
        trainee_list = [group 
                        for group in trainee_list 
                        if trainee_list[group].__class__.__name__ == self.__trainee_type]

        self.queued_trainees = None
        trainee_list_total = sum(count.get_trainee_count()
                                for count in trainee_list
                                )
        spaces = self.__capacity - self.__total_trainees

        if trainee_list_total > spaces:
            self.__trainees[f'group_{month}'] = []

            used_group = []

            for trainee in range(len(trainee_list)):

                if (spaces - trainee_list[trainee].get_trainee_count()) >= 0:
                    self.__trainees[f'group_{month}'].append(
                                                        trainee_list[trainee])

                    spaces -= trainee_list[trainee].get_trainee_count()
                    used_group.append(trainee)
            
                       
            self.queued_trainees = [trainee 
                                    for i, trainee in enumerate(trainee_list) 
                                    if i not in used_group]

        else:
            self.__trainees[f'group_{month}'] = trainee_list


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

    trainees = []

    for course, prob in course_probabilities.items():
            x = binomial(num_of_trainees, prob)

            while x == 0:
                x = binomial(num_of_trainees, prob)

            num_of_trainees -= x

            if course == 'Java':
                trainees.append(Java(x))
            elif course == 'Data':
                trainees.append(Data(x))
            elif course == 'CSharp':
                trainees.append(CSharp(x))
            elif course == 'DevOps':
                trainees.append(DevOps(x))
            elif course == 'Business':
                trainees.append(Business(x))   

    return trainees


class Trainee:
    def __init__(self, number_of_trainees) -> None:
        self.__trained_months = 0
        self.__trainee_count = number_of_trainees

    def increment_training(self):
        self.__trained_months += 1
        
    def get_trainee_count(self):
        return self.__trainee_count
    
    def update_trainee_count(self, amount):
        self.__trainee_count += amount
    
    def get_trained_months(self):
        return self.__trained_months

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}, {self.get_trainee_count()}, '
                f'{self.get_trained_months()} months;')


class Java(Trainee):
    def __init__(self, number_of_trainees) -> None:
        super().__init__(number_of_trainees)


class DevOps(Trainee):
    def __init__(self, number_of_trainees) -> None:
        super().__init__(number_of_trainees)


class CSharp(Trainee):
    def __init__(self, number_of_trainees) -> None:
        super().__init__(number_of_trainees)


class Data(Trainee):
    def __init__(self, number_of_trainees) -> None:
        super().__init__(number_of_trainees)


class Business(Trainee):
    def __init__(self, number_of_trainees) -> None:
        super().__init__(number_of_trainees)

