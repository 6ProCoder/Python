import time

# Initialize an empty list
data = []

# Ask the user for input
print("Enter 'data' to input data, 'print' to print the data, or 'stop' to stop.")

while True:
    user_input = input("> ").lower()

    if user_input == "stop":
        break
    elif user_input == "data":
        # Get the type of data to input
        data_type = input("Enter 'number' for a number or 'text' for text: ").lower()

        if data_type == "number":
            # Convert the input to an integer
            data.append(int(input("Enter a number: ")))
        elif data_type == "text":
            data.append(input("Enter some text: "))
        else:
            print("Invalid data type. Please enter 'number' or 'text'.")
    elif user_input == "print":
        print(">>>", data, "<<<")
    else:
        print("Invalid command. Please enter 'data', 'print', or 'stop'.")

time.sleep(10)
