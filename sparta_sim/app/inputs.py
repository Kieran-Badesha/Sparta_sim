# '''
# - Ask who the user is
# - How long the simulation (in months)
# - Remind the user that this value that was inputted is in months
# - Ask them if they want to rewrite the inputted value (y/n loop)
# '''
# Boolean prompts
# name_prompt = True
# Lists of yes or no vairations
yes_words = ["Y", "y", "Yes", "YES", "yes"]
no_words = ["N", "n", "No", "NO", "no"]
# while name_prompt:
#     user_name = input(f"What is your name?  ").capitalize()
#     if user_name.isalpha():
#         name_prompt = False
#     else:
#         print("Please use alphabetic letters to state your name")


def return_duration_sim(name: str) -> int:
    duration_of_sim = True
    input_duration_of_sim = input(f"How long would you like to run the simulation for in months?  ")

    while duration_of_sim:
        if input_duration_of_sim.isdigit():
            duration_of_sim = False

        else:
            input_duration_of_sim = input(
                f"{name}, Please input digits to represent the desired length of the Sparta simulation  ")

    input_duration_of_sim = int(input_duration_of_sim)

    return input_duration_of_sim


def return_user_input() -> [str, int]:
    name_prompt = True
    input_duration_of_sim = True

    while name_prompt:
        user_name = input(f"What is your name?  ").capitalize()

        if user_name.isalpha():
            name_prompt = False
            input_duration_of_sim = return_duration_sim(user_name)

        else:
            print("Please use alphabetic letters to state your name")

    return user_name, input_duration_of_sim


user, input_duration = return_user_input()


def confirm_duration(input_duration_1: int, user: str) -> bool:
    simulation_confirmation = input(f" you would like to simulate {input_duration_1} months. Is this correct?")

    while simulation_confirmation in yes_words or simulation_confirmation in no_words:
        if simulation_confirmation in no_words:
            simulation_confirmation = input(f"{user}, would you like change your simulation length? (Y/N) ").upper()

            if simulation_confirmation in no_words:
                return False

            else:
                global input_duration
                input_duration = return_duration_sim(user)

        else:
            print(f"You have confirmed to run the simulation for {input_duration} months")

            return True


print(confirm_duration(input_duration, user))
# yes or no statements can be lower or uppercase
