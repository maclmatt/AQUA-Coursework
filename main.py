import sys
import datetime
from reporting import daily_average, daily_median, hourly_average, monthly_average, peak_hour_date, count_missing_data, fill_missing_data
from intelligence import find_red_pixels, find_cyan_pixels, detect_connected_components, detect_connected_components_sorted

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

def reporting_menu(): #DONE 2 marks
    """Allows user to navigate data analysis options from the pollution reporting module
    Parameters: None
    Returns: None"""

    print("Pollution Reporting Menu:")
    print("DA - Daily Average\n" +
        "DM - Daily Median\n" +
        "HA - Hourly Average\n" +
        "MA - Monthly Average\n" +
        "PH - Peak Hour\n" + 
        "CM - Count Missing Data\n" + 
        "FM - Fill Missing Data\n")
    option = input("Please choose one of the above: ")

    if option == "DA":
        print("Which monitoring station would you like the daily averages for?")
        print("HRL - Harlington\n" + 
            "MY1 - Marylebone Road\n" +
            "KC1 - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        sitecode = input("Please choose one of the above: ")
        if sitecode == "Q":
            reporting_menu()
        elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
            print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like the daily averages for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()

        print(daily_average(" ", sitecode, pollutant))

    elif option == "DM":
        print("Which monitoring station would you like the daily medians for?")
        print("HRL - Harlington\n" + 
            "MY1 - Marylebone Road\n" +
            "KC1 - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        sitecode = input("Please choose one of the above: ")
        if sitecode == "Q":
            reporting_menu()
        elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
            print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like the daily medians for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()

        print(daily_median(" ", sitecode, pollutant))

    elif option == "HA":
        print("Which monitoring station would you like the hourly averages for?")
        print("HRL - Harlington\n" + 
            "MY1 - Marylebone Road\n" +
            "KC1 - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        sitecode = input("Please choose one of the above: ")
        if sitecode == "Q":
            reporting_menu()
        elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
            print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like the hourly averages for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()

        print(hourly_average(" ", sitecode, pollutant))

    elif option == "MA":

        print("Which monitoring station would you like the monthly averages for?")
        print("HRL - Harlington\n" + 
            "MY1 - Marylebone Road\n" +
            "KC1 - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        sitecode = input("Please choose one of the above: ")
        if sitecode == "Q":
            reporting_menu()
        elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
            print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like the monthly averages for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()

        print(monthly_average(" ", sitecode, pollutant))
    
    elif option == "PH":

        print("Which monitoring station would you like the peak hour for?")
        print("HRL - Harlington\n" + 
            "MY1 - Marylebone Road\n" +
            "KC1 - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        sitecode = input("Please choose one of the above: ")
        if sitecode == "Q":
            reporting_menu()
        elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
            print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like the peak hour for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()
        date_input = input("Which date would you like the peak hour for? (YYYY-MM-DD)")
        try:
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d')
        except:
            print("Incorrect data format, should be YYYY-MM-DD")
            reporting_menu()

        print(peak_hour_date(" ", date, sitecode, pollutant))

    elif option == "CM":

        print("Which monitoring station would you like to count the missing data for?")
        print("HRL - Harlington\n" + 
            "MY1 - Marylebone Road\n" +
            "KC1 - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        sitecode = input("Please choose one of the above: ")
        if sitecode == "Q":
            reporting_menu()
        elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
            print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like to count the missing data for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()
        print("There are", count_missing_data(" ", sitecode, pollutant), "missing values")

    elif option == "FM":

        print("Which monitoring station would you like to fill the missing values for?")
        print("HRL - Harlington\n" + 
            "MY1 - Marylebone Road\n" +
            "KC1 - North Kensington\n"
            "Q - Go back to Pollution Reporting Menu")
        sitecode = input("Please choose one of the above: ")
        if sitecode == "Q":
            reporting_menu()
        elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
            print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
            reporting_menu()
        print("Which pollutant would you like to fill the missing values for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()
        new_value = input("Please enter the value you would like to replace the missing values with: ")

        fill_missing_data(" ", new_value, sitecode, pollutant)

    main_menu()

def monitoring_menu(): #DONE 2 marks
    """Allows user to navigate image analysis options from the mobility intelligence module
    Parameters: None
    Returns: None"""

    print("Mobility Intelligence Menu:")
    print("RP - Generate image representing all the red pixels from original map\n" +
        "CP - Generate image representing all the cyan pixels from original mapn\n" +
        "DC - Detect all connected pavement pixels\n" +
        "SDC - Sort all connected pavement regions\n")
    option = input("Please choose one of the above: ")

    if option == "RP":
        red_pixels = find_red_pixels("map.png")
        print("An image of the map with only the red pixels represented has been generated and saved to the file: 'map-red-pixels.jpg'.")
    
    elif option == "CP":
        cyan_pixels = find_cyan_pixels("map.png")
        print("An image of the map with only the red pixels represented has been generated and saved to the file: 'map-cyan-pixels.jpg'.")
    
    elif option == "DC":
        pavements = detect_connected_components(find_red_pixels("map.png"))
        print("A list of all the pavements and there size (in number of pixels) has been saved to the file: 'cc-output-2a.txt'")

    elif option == "SDC":
        pavements = detect_connected_components(find_red_pixels("map.png"))
        print("A list of all the pavements and there size (in number of pixels)\n" + 
            "in ascending order has been saved to the file: 'cc-output-2b.txt'")
        print("An image representing the two largest pavements has been saved to the file: 'cc-top-2.jpg'")

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