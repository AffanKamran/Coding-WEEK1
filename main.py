#*************************************************************************************
#******************* AICP CODING INTERNSHIP Task Week 1 ******************************
#*************************************************************************************

def validate_weight(weight):
    try:
        weight = float(weight)
        if weight <= 15 or weight >= 200:  # weight range (15-200)
            return False
        else:
            return True
    except ValueError:
        return False


def input_weights_and_names(num_pupils):
    names = []
    weights = []
    for i in range(num_pupils):
        name = input("Enter name of pupil {}: ".format(i + 1))
        while True:
            weight = input("Enter weight of {} on the first day of term: ".format(name))
            if validate_weight(weight):
                weights.append(float(weight))
                names.append(name)
                break
            else:
                print("Invalid weight. Please enter a valid weight.")

    return names, weights


def input_last_day_weights(num_pupils):
    last_day_weights = []
    for i in range(num_pupils):
        while True:
            weight = input("Enter weight of pupil {} on the last day of term: ".format(i + 1))
            if validate_weight(weight):
                last_day_weights.append(float(weight))
                break
            else:
                print("Invalid weight. Please enter a valid weight.")

    return last_day_weights


def calculate_weight_differences(weights_first_day, weights_last_day):
    differences = [last - first for first, last in zip(weights_first_day, weights_last_day)]
    return differences


def output_names_and_weights(names, weights):
    print("\nPupil Names and Weights:")
    for name, weight in zip(names, weights):
        print("Name: {}, Weight: {} kg".format(name, weight))


def output_names_and_weight_differences(names, weight_differences):
    print("\nPupil Names and Weight Differences:")
    for name, difference in zip(names, weight_differences):
        print("Name: {}, Weight Difference: {} kg".format(name, difference))


def output_names_and_weight_differences2(names, weight_differences):
    print("\nPupil Names and Weight Differences:")
    for name, difference in zip(names, weight_differences):
        print("Name: {}, Weight Difference: {} kg".format(name, difference))
        if abs(difference) > 2.5:
            if difference > 0:
                print("{}'s weight has risen by {} kg.".format(name, abs(difference)))
            else:
                print("{}'s weight has fallen by {} kg.".format(name, abs(difference)))


def execute_task():
    print("***** Choose a task to execute: **********")
    print("1. Record weights on the first day of term.")
    print("2. Record weights on the last day of term and calculate differences.")
    print("3. Output weight differences and identify whether weight rises/falls.")
    print()
    task_choice = input("Enter the task number (1, 2, or 3): ")

    if task_choice == '1':
        num_pupils = 30
        names, weights = input_weights_and_names(num_pupils)
        output_names_and_weights(names, weights)
    elif task_choice == '2':
        num_pupils = 30
        names, weights_first_day = input_weights_and_names(num_pupils)
        weights_last_day = input_last_day_weights(num_pupils)
        weight_differences = calculate_weight_differences(weights_first_day, weights_last_day)
        output_names_and_weight_differences(names, weight_differences)
    elif task_choice == '3':
        num_pupils = 30
        names, weights_first_day = input_weights_and_names(num_pupils)
        weights_last_day = input_last_day_weights(num_pupils)
        weight_differences = calculate_weight_differences(weights_first_day, weights_last_day)
        output_names_and_weight_differences2(names, weight_differences)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    execute_task()


if __name__ == "__main__":
    main()
