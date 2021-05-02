import csv
from datetime import date
from pathlib import Path
import os

#do you want to save?
file_path = "D:/Inburgering examen/Welkom in Nederland/vocabulary exercise/wordlists/"
file_loc = "D:/Inburgering examen/Welkom in Nederland/vocabulary exercise/wordlists/chapter2.ods"

#check if the file name is already taken
def check_repeat_file_name(new_filename, file_path):
    name_exist = True
    while name_exist:
        if os.path.isfile(f'{file_path}{new_filename}.csv'):
            print('Name is taken, enter a new file name:')
            new_filename = input('file exits,'
                                 'please enter a new name (without suffix): ')
        else:
            new_path = f'{file_path}{new_filename}.csv'
            name_exist = False
            return new_path

def path_for_exercise(file_path, file_loc):
    # default name
    wordlist_name = Path(file_loc)
    default_name = f'mistakes {wordlist_name.stem} {date.today()}.csv'

    # rename file
    change_file = input(f'Default file name is "{default_name}", '
                        f'would you like to rename it? (y/n).')
    if change_file.lower() == 'y':
        new_filename = input('please enter a file name (without suffix): ')
        return check_repeat_file_name(new_filename, file_path)
    else:
        default_path = f'{file_path}{default_name}'
        return default_path


def path_for_review(path_for_exercise):
    defult_path = "D:/Inburgering examen/Welkom in Nederland/vocabulary exercise/"
    file_name = Path(path_for_exercise).name
    full_path = defult_path + file_name
    return full_path

# to review:
# save_file(path_review, not_guessed)
def save_file_to_review(path, dict):
    with open(path, 'w', newline='') as f:
        csv_writer = csv.writer(f, delimiter='\t')
        csv_writer.writerow(['Engels - Dutch, Your Answer'])
        for item in dict.items():
            csv_writer.writerow(item)

# to practice:
# save_file(path_exercise, dict_of_mistakes)
def save_file_to_practice(path, dict):
    with open(path, 'w', newline='') as f:
        csv_writer = csv.writer(f, delimiter='\t')
        csv_writer.writerow(['Nederlands', 'Engels'])
        for item in dict.items():
            csv_writer.writerow(item)
