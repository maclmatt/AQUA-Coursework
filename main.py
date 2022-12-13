import sys
import datetime
from reporting import daily_average, daily_median, hourly_average, monthly_average, peak_hour_date, count_missing_data, fill_missing_data
from intelligence import find_red_pixels, find_cyan_pixels, detect_connected_components, detect_connected_components_sorted
from monitoring import day_graph, week_graph, month_graph, day_graph_pollutant, week_graph_pollutant, month_graph_pollutant, health_advice, yearly_reports, safest_place


def main_menu(): #DONE 2 marks
    """Gets and implements users choice from main menu
    Parameters: None
    Returns: None"""

    print("\nMenu:")
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

    print("\nPollution Reporting Menu:")
    print("DA - Daily Average\n" +
        "DM - Daily Median\n" +
        "HA - Hourly Average\n" +
        "MA - Monthly Average\n" +
        "PH - Peak Hour\n" + 
        "CM - Count Missing Data\n" + 
        "FM - Fill Missing Data\n")
    option = input("Please choose one of the above: ")

    if option == "DA":
        print("\nWhich monitoring station would you like the daily averages for?")
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
        print("\nWhich pollutant would you like the daily averages for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()

        print(daily_average(" ", sitecode, pollutant))

    elif option == "DM":
        print("\nWhich monitoring station would you like the daily medians for?")
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
        print("\nWhich pollutant would you like the daily medians for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()

        print(daily_median(" ", sitecode, pollutant))

    elif option == "HA":
        print("\nWhich monitoring station would you like the hourly averages for?")
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
        print("\nWhich pollutant would you like the hourly averages for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()

        print(hourly_average(" ", sitecode, pollutant))

    elif option == "MA":

        print("\nWhich monitoring station would you like the monthly averages for?")
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
        print("\nWhich pollutant would you like the monthly averages for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()

        print(monthly_average(" ", sitecode, pollutant))
    
    elif option == "PH":

        print("\nWhich monitoring station would you like the peak hour for?")
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
        print("\nWhich pollutant would you like the peak hour for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()
        date_input = input("\nWhich date would you like the peak hour for? (YYYY-MM-DD)")
        try:
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d')
        except:
            print("Incorrect data format, should be YYYY-MM-DD")
            reporting_menu()

        print(peak_hour_date(" ", date, sitecode, pollutant))

    elif option == "CM":

        print("\nWhich monitoring station would you like to count the missing data for?")
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
        print("\nWhich pollutant would you like to count the missing data for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()
        print("There are", count_missing_data(" ", sitecode, pollutant), "missing values")

    elif option == "FM":

        print("\nWhich monitoring station would you like to fill the missing values for?")
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
        print("\nWhich pollutant would you like to fill the missing values for?")
        print("no - Nitric oxide\n" +
            "pm10 - PM10 inhalable particulate matter\n" +
            "pm25 - PM2.5 inhalable particulate matter\n")
        pollutant = input("Please choose one of the above: ")
        if pollutant not in ["no", "pm10", "pm25"]:
            print("Invalid input, please enter 'no', 'pm10' or 'pm25'.")
            reporting_menu()
        new_value = input("\nPlease enter the value you would like to replace the missing values with: ")

        fill_missing_data(" ", new_value, sitecode, pollutant)

    main_menu()

def intelligence_menu(): #DONE 2 marks, not tested
    """Allows user to navigate image analysis options from the mobility intelligence module
    Parameters: None
    Returns: None"""

    print("\nMobility Intelligence Menu:")
    print("RP - Generate image representing all the red pixels from original map\n" +
        "CP - Generate image representing all the cyan pixels from original mapn\n" +
        "DC - Detect all connected pavement pixels\n" +
        "SDC - Sort all connected pavement regions\n")
    option = input("Please choose one of the above: ")

    if option == "RP":
        red_pixels = find_red_pixels("map.png")
        print("\nAn image of the map with only the red pixels represented has been generated and saved to the file: 'map-red-pixels.jpg'.")
    
    elif option == "CP":
        cyan_pixels = find_cyan_pixels("map.png")
        print("\nAn image of the map with only the red pixels represented has been generated and saved to the file: 'map-cyan-pixels.jpg'.")
    
    elif option == "DC":
        pavements = detect_connected_components(find_red_pixels("map.png"))
        print("\nA list of all the pavements and there size (in number of pixels) has been saved to the file: 'cc-output-2a.txt'")

    elif option == "SDC":
        MARK = detect_connected_components(find_red_pixels("map.png"))
        pavements = detect_connected_components_sorted(MARK)
        print("\nA list of all the pavements and there size (in number of pixels)\n" + 
            "in ascending order has been saved to the file: 'cc-output-2b.txt'")
        print("An image representing the two largest pavements has been saved to the file: 'cc-top-2.jpg'")

    main_menu()

def monitoring_menu(): #DONE 2 marks, more options could be added
    """Allows user to navigate live data analysis options from the real-time monitoring module
    Parameters: None
    Returns: None"""

    print("\nReal-time Monitoring Menu:")
    print("Would you like health advice or to see a graph for pollution levels?")
    print("G - Graph\nH - Health Advice")
    choice = input("Please choose one of the above: ")
    if choice == "G":

        print("\nWhich period of time would you like to see a graph for?")
        print("1 - Day\n" +
            "2 - Week\n" +
            "3 - Month\n")
        option = input("Please choose one of the above: ")
    
        if option == "1":
            print("\nWhich monitoring station would you like to see the graph for?")
            print("HRL - Harlington\n" + 
                "MY1 - Marylebone Road\n" +
                "KC1 - North Kensington\n"
                "Q - Go back to Real-time Monitoring Menu")
            sitecode = input("Please choose one of the above: ")
            if sitecode == "Q":
                monitoring_menu()
            elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
                print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
                monitoring_menu()
            one_or_more = input("Would you like to see a graph for all the pollutants? (Y/N) ")
            if one_or_more == "Y":
                day_graph(sitecode)
            elif one_or_more == "N":
                print("\nWhich pollutant would you like to see the graph for?")
                print("NO - Nitric oxide\n" +
                    "PM10 - PM10 inhalable particulate matter\n" +
                    "PM25 - PM2.5 inhalable particulate matter\n")
                pollutant = input("Please choose one of the above: ")
                if pollutant not in ["NO", "PM10", "PM25"]:
                    print("Invalid input, please enter 'NO', 'PM10' or 'PM25'.")
                    monitoring_menu()
                day_graph_pollutant(sitecode, pollutant)

        if option == "2":
            print("\nWhich monitoring station would you like to see the graph for?")
            print("HRL - Harlington\n" + 
                "MY1 - Marylebone Road\n" +
                "KC1 - North Kensington\n"
                "Q - Go back to Real-time Monitoring Menu")
            sitecode = input("Please choose one of the above: ")
            if sitecode == "Q":
                monitoring_menu()
            elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
                print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
                monitoring_menu()
            one_or_more = input("Would you like to see a graph for all the pollutants? (Y/N) ")
            if one_or_more == "Y":
                week_graph(sitecode)
            elif one_or_more == "N":
                print("\nWhich pollutant would you like to see the graph for?")
                print("NO - Nitric oxide\n" +
                    "PM10 - PM10 inhalable particulate matter\n" +
                    "PM25 - PM2.5 inhalable particulate matter\n")
                pollutant = input("Please choose one of the above: ")
                if pollutant not in ["NO", "PM10", "PM25"]:
                    print("Invalid input, please enter 'NO', 'PM10' or 'PM25'.")
                    monitoring_menu()
                week_graph_pollutant(sitecode, pollutant)

        if option == "3":
            print("\nWhich monitoring station would you like to see the graph for?")
            print("HRL - Harlington\n" + 
                "MY1 - Marylebone Road\n" +
                "KC1 - North Kensington\n"
                "Q - Go back to Real-time Monitoring Menu")
            sitecode = input("Please choose one of the above: ")
            if sitecode == "Q":
                monitoring_menu()
            elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
                print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
                monitoring_menu()
            one_or_more = input("Would you like to see a graph for all the pollutants? (Y/N) ")
            if one_or_more == "Y":
                month_graph(sitecode)
            elif one_or_more == "N":
                print("\nWhich pollutant would you like to see the graph for?")
                print("NO - Nitric oxide\n" +
                    "PM10 - PM10 inhalable particulate matter\n" +
                    "PM25 - PM2.5 inhalable particulate matter\n")
                pollutant = input("Please choose one of the above: ")
                if pollutant not in ["NO", "PM10", "PM25"]:
                    print("Invalid input, please enter 'NO', 'PM10' or 'PM25'.")
                    monitoring_menu()
                month_graph_pollutant(sitecode, pollutant)

    elif choice == "H":

        print("\nWhich monitoring station are you close to?")
        print("HRL - Harlington\n" + 
            "MY1 - Marylebone Road\n" +
            "KC1 - North Kensington\n"
            "Q - Go back to Real-time Monitoring Menu")
        sitecode = input("Please choose one of the above: ")
        if sitecode == "Q":
            monitoring_menu()
        elif sitecode not in ["HRL", "MY1", "KC1", "Q"]:
            print("Invalid input, please enter 'HRL', 'MY1', 'KC1' or 'Q'.")
            monitoring_menu()

        pop, health_Advice = health_advice(sitecode)
        for i in range(0, len(pop)):
            print("\n", pop[i], ":", health_Advice[i])

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