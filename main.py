import sys


def main_menu(): #DONE 2 marks
    """Gets and implements users choice from main menu
    Parameters: None
    Returns: None"""

    print("Menu:")
    print("R - Access the Pollution Reporting module\n" + 
        "I - Access the Mobility Intelligence module\n" + 
        "M - Access the Real-time Monitoring module\n" + 
        "A - Print the About text\n" +
        "Q - Quit the application")
    option = input("Please choose one of the above: ")

    if option == "R":
        reporting_menu()
    elif option == "I":
        intelligence_menu()
    elif option == "M":
        monitoring_menu()
    elif option == "A":
        about()
    elif option == "Q":
        quit()
    else:
        print("Your choice is not valid, please enter 'R', 'I', 'M', 'A' or 'Q'.")
        main_menu()

def reporting_menu():
    """Allows user to navigate data analysis options from the pollution reporting module
    Parameters: None
    Returns: None"""

    print("Pollution Reporting Menu:")
    print("DA - Daily Average\n" +
        "DM - Daily Median\n" +
        "HA - Hourly Average\n" +
        "MA - Monthly Average\n" +
        "PH - Peak Hour\n")
    option = input("Please choose one of the above: ")

    if option == "DA":
        print(" ")
    elif option == "DM":
        print(" ")
    elif option == "HA":
        print(" ")
    elif option == "MA":
        print(" ")
    elif option == "PH":
        print(" ")

    #should complete while doing 4.1.1 coding tasks (i.e., reporting.py)

    main_menu()



def monitoring_menu():
    """Your documentation goes here"""
    # Your code goes here
    main_menu()


def intelligence_menu():
    """Your documentation goes here"""
    # Your code goes here
    main_menu()

def about(): #DONE 1 mark
    """Prints module code and 6-digit candidate number, then returns to main menu
    Parameters: None
    Returns: None"""
    print("ECM1400")
    print("257111")

def quit(): #DONE 1 mark
    """Quits program, with goodbye message
    Parameters: None
    Results: None"""
    print("Thank you for using the AQUA platform.")
    sys.exit()

if __name__ == '__main__':
    main_menu()