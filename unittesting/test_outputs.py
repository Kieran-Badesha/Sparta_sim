import pytest
from sparta_sim.app.classes import *


# Ensuring that queued trainees is a positive int value incl.0
# Error Handling via try/except blocks
def test_queued_trainees():
    try:
        assert Academy.get_queue() >= 0
    except ValueError:
        print('Negative number of queued trainees not possible')


# Ensuring that finished trainees is a positive int value incl.0
# Error Handling via try/except blocks
def test_finished_trainees():
    try:
        assert Academy.get_finished_trainees() >= 0
    except ValueError:
        print('Negative number of trainees finished not possible')


# Ensure the Conditions of Training hubs are met
# Error Handling via try/except blocks
def test_num_training_hub():
    try:
        assert TrainingHub.totalhubs() <= 3
    except ValueError:
        print('Total Training hubs cannot exceed 3 in any given month')

    try:
        assert TrainingHub.get_trainee_count() <= 100
    except ValueError:
        print('Total number of students per Hub cannot exceed 100')

    try:
        assert TrainingHub.capacity() == 100
    except ValueError:
        print('Expected Max capacity of Training Hub = 100')


# Ensure the Conditions of Bootcamps are met
# Error Handling via try/except blocks
def test_num_bootcamp():
    try:
        assert Bootcamp.totalcamps() <= 2
    except ValueError:
        print('Total Bootcamps cannot exceed 2')

    try:
        assert Bootcamp.get_trainee_count() <= 500
    except ValueError:
        print('Total number of students per Bootcamp cannot exceed 500')

    try:
        assert Bootcamp.capacity() == 500
    except ValueError:
        print('Expected Max capacity of Bootcamp = 500')


# Ensure the Conditions of Tech centres are met
# Error Handling via try/except blocks
def test_num_tech_centre():
    try:
        assert TechCentre.coursetypes() == 1
    except ValueError:
        print('Only 1 course type allowed')

    try:
        assert TechCentre.get_trainee_count() <= 200
    except ValueError:
        print('Total number of students per Tech Centre cannot exceed 200')

    try:
        assert TechCentre.capacity() == 200
    except ValueError:
        print('Expected Max capacity of Tech centre = 200')


# Ensure that number of trainees is within min and max values and that new trainees start with 0 months trained
# Error Handling via try/except blocks
def test_trainee_generator():
    try:
        assert trainee_generator(20, 30) <= 30
    except ValueError:
        print('Generated trainees cannot exceed the Max value per month')

    try:
        assert trainee_generator(20, 30) >= 20
    except ValueError:
        print('Generated trainees cannot be lower than the Min value per month')


def test_trainee_course_type():
    try:
        assert trainee_generator(20, 30)[0] == Java(4)
    except ValueError:
        print('Newly generated trainees must be assigned a course type')

    try:
        assert trainee_generator(20, 30)[1] == Data(4)
    except ValueError:
        print('Newly generated trainees must be assigned a course type')

    try:
        assert trainee_generator(20, 30)[2] == CSharp(4)
    except ValueError:
        print('Newly generated trainees must be assigned a course type')

    try:
        assert trainee_generator(20, 30)[3] == DevOps(4)
    except ValueError:
        print('Newly generated trainees must be assigned a course type')

    try:
        assert trainee_generator(20, 30)[4] == Business(4)
    except ValueError:
        print('Newly generated trainees must be assigned a course type')
