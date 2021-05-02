from write_dutch import question
from os import listdir
import read_files

def main():
    # file path is dir (without file name)
    # file loc is accurate file location
    file_path = read_files.file_path()
    print(f'wordlist path: {file_path}')
    continue_practice = True
    while continue_practice:
        show_files = [print(f) for f in listdir(file_path) if
                      f.endswith(('.ods', '.csv'))]
        file_loc = read_files.pick_file(file_path)
        wordlist = read_files.convert_file(file_loc)
        print(f'There are {len(wordlist)} words in the list', end='\n')
        # ask about number of questions
        numbers_of_questions = input('how many words do you want to practice? ')
        not_number = True
        while not_number:
            if numbers_of_questions.isnumeric():
                not_number = False
            else:
                numbers_of_questions = input('please fill in a valid number: ')
        # option to quit exercise
        print('You can quit anytime during the exercise by enter "q" ')
        # main
        question(wordlist, numbers_of_questions, file_loc, file_path)
        # option to practice again
        if input('Do you want to practice again? (y/n)') == 'y'.lower():
            continue_practice = True
        else:
            print("well done! See you next time!")
            continue_practice = False

if __name__ == '__main__':
    main()