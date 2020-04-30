

def int_input(message):
    """
    Converts string input into 'int' type.
    """
    answer = input(message)
    return int(answer)


if __name__ == "__main__":
    desired_weight = int_input("Enter desired weight: ")
    bar_weight = int_input("Enter weight of bar: ") 
    desired_weight = (desired_weight-bar_weight)/2
    num_45 = 0
    num_25 = 0
    num_10 = 0
    num_5 = 0
    num_2_5 = 0
    while True:
        if desired_weight >= 45:
            desired_weight -= 45
            num_45 += 1
            continue
        elif desired_weight >= 25:
            desired_weight -= 25
            num_25 += 1
            continue
        elif desired_weight >= 10:
            desired_weight -= 10
            num_10 += 1
            continue
        elif desired_weight >= 5:
            desired_weight -= 5
            num_5 += 1
            continue
        elif desired_weight >= 2.5:
            desired_weight -= 2.5
            num_2_5 += 1
            continue
        break

print(f"You will need: \
    \n{num_45} 45lb plate(s) \
    \n{num_25} 25lb plate(s) \
    \n{num_10} 10lb plate(s) \
    \n{num_5} 5lb plate(s) \
    \n{num_2_5} 2.5lb plate(s) \
    \non each side of the bar.")