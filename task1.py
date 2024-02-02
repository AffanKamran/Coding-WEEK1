# **************** AICP CODING INTERNSHIP Task Week 1 ********************************
#************************** Task 1 ***************************************************
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

def input_names_and_weights(num_pupils):
    names = []
    weights = []
    for i in range(num_pupils):
        name = input("Enter name of pupil {}: ".format(i+1))
        while True:
            weight = input("Enter weight of {}: ".format(name))
            if validate_weight(weight):
                weights.append(float(weight))
                names.append(name)
                break
            else:
                print("Invalid weight. Please enter a valid weight.")

    return names, weights

def output_names_and_weights(names, weights):
    print("\nPupil Names and Weights:")
    for name, weight in zip(names, weights):
        print("Name: {}, Weight: {} kg".format(name, weight))

def main():
    num_pupils = 30
    names, weights = input_names_and_weights(num_pupils)
    output_names_and_weights(names, weights)

if __name__ == "__main__":
    main()
