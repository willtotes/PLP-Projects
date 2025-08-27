def view_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        edited_content = content.upper()
        output_filename = f"modified_{filename}"

        with open(output_filename, 'w') as output_file:
            output_file.write(edited_content)

        print(f"Success, the file has been created as: {edited_content}")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    view_file()

