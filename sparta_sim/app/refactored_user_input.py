from sparta_sim.app.config_input import total_time

duration_of_sim = total_time


def return_user_input() -> [str]:
    user_name = input(f"What is your name?  ").capitalize()
    while not user_name.isalpha():
        user_name = input(f"Please use alphabetic letters to state your name  ").capitalize()

    return user_name


user = return_user_input()
