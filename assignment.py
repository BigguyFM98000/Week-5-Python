# File Creation, Writing to the File, Reading, Appending, and Error Handling

def create_and_write_file():
    try:
        # Task 1: File Creation and Writing
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("This is line 2 with a number: 42.\n")
            file.write("Line 3: End of initial content.\n")
        print("File 'my_file.txt' created and initial content written.")
    except Exception as e:
        print(f"An error occurred while creating/writing the file: {e}")
    finally:
        print("File creation/writing process is complete.")


def read_file():
    try:
        # Task 2: Reading and Displaying File Contents
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nContent of 'my_file.txt':\n")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("File reading process is complete.")


def append_to_file():
    try:
        # Task 3: Appending to the File
        with open('my_file.txt', 'a') as file:
            file.write("Appended line 4: Additional content.\n")
            file.write("Appended line 5 with another number: 100.\n")
            file.write("Appended line 6: End of appended content.\n")
        print("Content appended to 'my_file.txt'.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File appending process is complete.")


# Task 4: Error Handling for All Operations
def main():
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()  # Reading again to show the appended content


if __name__ == "__main__":
    main()
