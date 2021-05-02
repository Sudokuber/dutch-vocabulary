from write_file import path_for_review, path_for_exercise, save_file_to_review, save_file_to_practice
import random

def question(wordlist, numbers_of_questions, file_loc, file_path):
    # make a copy of original dictionary
    wordlist_copy = wordlist.copy()
    count = 1
    correct = 0
    words_are_asked = {}
    guessed = {}
    not_guessed = {}
    dict_of_mistakes = {}
    while count <= int(numbers_of_questions):
        word = random.choice(list(wordlist_copy.items()))
        user_input = input(
            f'{count}. Please write down the Dutch word for {word[1]}: ')
        del wordlist_copy[word[0]]
        words_are_asked[word[0]] = word[1]
        if user_input.lower() == word[0].lower():
            guessed[word[0]] = word[1]
            count += 1
            correct += 1
            print('Correct!')
        elif user_input.lower() == 'q':
            break
        else:
            not_guessed[word[1]] = [word[0], user_input]
            dict_of_mistakes[word[0]] = word[1]
            count += 1
            print('Incorrect!')

    else:
        print(f'You answered {correct} / {numbers_of_questions} questions correct.')
        if len(not_guessed) != 0:
            # review incorrect answers
            review_not_guessed = input("would you like to review mistakes? (y/n)")
            if review_not_guessed.lower() == 'y':
                for key, values in not_guessed.items():
                    print(f'English: {key} - Dutch: {values[0]} - Your answer: {values[1]}')

            # save to file
            save_not_guessed_to_file = input('would you like to save your mistakes to a file? (y/n)')
            if save_not_guessed_to_file.lower() == 'y':
                exercise_path = path_for_exercise(file_path, file_loc)
                review_path = path_for_review(exercise_path)
                #file to review
                save_file_to_review(review_path, not_guessed)
                #file to practice
                save_file_to_practice(exercise_path, dict_of_mistakes)
                print('Saved!')
