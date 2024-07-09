def main():
    # Ask for first name
    first_name = input("Enter your first name: ")
    
    # Ask for last name
    last_name = input("Enter your last name: ")
    
    # Validate lengths
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name should be at least 2 characters long.")
    else:
        print("Thank you! Input validation successful.")

main()
