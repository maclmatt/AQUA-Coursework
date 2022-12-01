import sys
from reporting import daily_average, daily_median, hourly_average, monthly_average, peak_hour_date 

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
        print("Which monitoring station would you like the daily averages for?")
        print("H - Harlington\n" + 
            "M - Marylebone Road\n" +
            "N - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        option = input("Please choose one of the above: ")
        if option == "H":
            monitoring_station = "Pollution-London Harlington.csv"
        elif option == "M":
            monitoring_station = "Pollution-London Marylebone Road.csv"
        elif option == "N":
            monitoring_station = "Pollution-London N Kensington.csv"
        elif option == "Q":
            reporting_menu()
        else:
            print("Invalid input, please enter 'H', 'M', 'N' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like the daily averages for?")
        print("NO - Nitric oxide\n" +
            "PM10 - PM10 inhalable particulate matter\n" +
            "PM2.5 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["NO", "PM10", "PM2.5"]:
            print("Invalid input, please enter 'NO', 'PM10' or 'PM2.5'.")
            reporting_menu()

        print(daily_average("data/", monitoring_station, pollutant))

    elif option == "DM":
        print("Which monitoring station would you like the daily medians for?")
        print("H - Harlington\n" + 
            "M - Marylebone Road\n" +
            "N - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        option = input("Please choose one of the above: ")
        if option == "H":
            monitoring_station = "Pollution-London Harlington.csv"
        elif option == "M":
            monitoring_station = "Pollution-London Marylebone Road.csv"
        elif option == "N":
            monitoring_station = "Pollution-London N Kensington.csv"
        elif option == "Q":
            reporting_menu()
        else:
            print("Invalid input, please enter 'H', 'M', 'N' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like the daily medians for?")
        print("NO - Nitric oxide\n" +
            "PM10 - PM10 inhalable particulate matter\n" +
            "PM2.5 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["NO", "PM10", "PM2.5"]:
            print("Invalid input, please enter 'NO', 'PM10' or 'PM2.5'.")
            reporting_menu()

        print(daily_median("data/", monitoring_station, pollutant))
        
    elif option == "HA":
        print(" ")
    elif option == "MA":
        print(" ")
    elif option == "PH":
        print(" ")

    #should complete while doing 4.1.1 coding tasks (i.e., reporting.py)

    main_menu()



def monitoring_menu():
    
    main_menu()


def intelligence_menu():
    """Your documentation goes here"""
    
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