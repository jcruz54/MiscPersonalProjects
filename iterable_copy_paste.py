import pyperclip
import keyboard

def list_input(text_input, delimiter, strip_whitespace=False):
    """
    Converts string input into a list using a defined delimiter
    """
    text_input += delimiter
    if strip_whitespace:
        text_input = text_input.replace(" ", "")


    final_list = []
    list_item = ""

    for char in text_input:
        if char != delimiter:
            list_item += char
        else:
            final_list.append(list_item)
            list_item = ""

    return final_list


if __name__ == "__main__":
    test = input("Enter some text: ")
    test_list = list_input(test, " ")

    print(f"Paste Elements List: {test_list}")
    print("Ready to paste!")

    while True:
        for element in test_list:
            print(f"Current Paste Element: {element}")
            pyperclip.copy(element)
            keyboard.wait('ctrl + v')

        print("Cycle complete. Do you want to go through the list again? (Y/N)")
        restart_cycle = input().upper

        if restart_cycle == "N":
            break
    