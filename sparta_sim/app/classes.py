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

class Trainee:
    def __init__(self, min_trainees=20, max_trainees=30):
        self.min_trainees = min_trainees
        self.max_trainees = max_trainees


class Java(Trainee):
    def __init__(self):
        super().__init__()


class Data(Trainee):
    def __init__(self):
        super().__init__()


class CSharp(Trainee):
    def __init__(self):
        super().__init__()


class DevOps(Trainee):
    def __init__(self):
        super().__init__()


class Business(Trainee):
    def __init__(self):
        super().__init__()
