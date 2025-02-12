def get_multiple_of_six():
    """Forces the user to enter a multiple of 6
    :return: The valid integer input that is a multiple of 6
    """
    while True:
        try:
            num = int(input("Enter a multiple of 6: ")) #convernts input to interger
            if num % 6 == 0: #if the residual of dividing by 6 is 0
                print("great!", num, "this is a multiple of 6")
                return num
            else:
                print("Error: The number is not a multiple of 6. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

get_multiple_of_six()