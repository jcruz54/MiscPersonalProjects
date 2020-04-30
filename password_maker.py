import random 

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*"
three_char_words = ["shy","pop","hog","pig","cap","dog","cat","act","owl","lot"]
four_char_words = ["book","bone","fish","dark","moon","ship","wild","wood","chef","duke"]
five_char_words = ["ariel","bacon","camel","campy","comfy","shoes","rupee", "mango","phone","pizza"]
weak_word_lists = [three_char_words, four_char_words, five_char_words]

def int_input(message):
    """
    Converts string input into 'int' type.
    """
    answer = input(message)
    return int(answer)

def bool_input(question, option_1, option_2):
    """
    Returns True or False based on user-response to a two-answer question.
    
    The response being equal to the first option will return True, the 
    second option will return false.

    If the user enters a response that is neither one of the options,
    a ValueError is raised.

    --- EXAMPLE ---
    A "Yes/No" question is a two-option question. "Yes"
    could be set to option_1 and "No" could be set to option_2. If
    the user were to enter "Yes" in response to the question, this
    function would return "True" while it would return "False" if
    the user entered "No" to the question.
    ---------------
    """
    answer = input(question)
    if answer.upper() == option_1:
        return True
    elif answer.upper() == option_2:
        return False
    else:
        raise ValueError(f'Invalid input. Please enter either {option_1} or {option_2}.')

def create_password(is_strong, has_numbers, has_special_chars):
    """
    Creates a customized password based on provided parameters.
    """
    password = ""
    features = [lowercase, uppercase]
    if has_numbers:
            features.append(numbers)
    if has_special_chars:
        features.append(special_characters)

    if is_strong:
        print("For a strong password, your password will be a minimum of 8 characters in length.")
        length = int_input("How many total characters do you want in you password?")
        if length < 8:
            raise ValueError(f'Invalid input. Please enter a greater than or equal to 8.')
        for x in range(0, length):
            current_char = random.choice(random.choice(features))
            password += current_char
    else:
        print("For a weak password, your password will contain a word 3-5 characters in length.")
        length = int_input("How many characters do you want in your password's word?")
        
        if length >= 3 or length <=5:
            word_list = weak_word_lists[length-3]
            password += random.choice(word_list)
        else:
            raise ValueError(f'Invalid input. Please enter a value betweem 3 and 5 inclusive.')
        
        for feature in features:
            password += random.choice(feature)

    return password

if __name__ == "__main__":
    is_strong = bool_input("Do you want a strong or weak password? (STRONG/WEAK)", option_1="STRONG", option_2="WEAK")
    has_numbers = bool_input("Would you like numbers in your password? (Y/N)", option_1="Y", option_2="N")
    has_special_chars = bool_input("Would you like special characters in your password? (Y/N)", option_1="Y", option_2="N")

    new_password = create_password(is_strong, has_numbers, has_special_chars)
    print(new_password)