import time
import pandas as pd
import numpy as np
#-----------------------------------------------------------

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

#-----------------------------------------------------------
# All my references are from Udacity class pages and geeksforgeeks website
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\n Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Asking the user and get the input, then check the spelling
    while True:
        city = str(input("Would you like to see data for Chicago, New York, or Washington?\n")).lower()
        if city == "chicago" or city == "new york" or city == "washington":
            break
        
        else: 
            print("Oops that's not a good typing...")

             
    while True:
        answer = str(input("Would you like to filter the data by month, day, or not at all?\n")).lower()
        if answer == "month" or answer == "day" or answer == "all":
            break
        
        else: 
            print("Oops that's not a good typing...")


    # TO DO: get user input for month (all, january, february, ... , june)
    # Asking the user and get the input, then check the spelling
    if answer == "month":
        
        day = "all"
        
        while True:
           month = str(input("Which month - January, February, March, April, May, or June?\n")).lower()
           if checkMonth(month):
              break
        
           else: 
                print("Oops that's not a good typing...")

        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Asking the user and get the input, then check the spelling
    elif answer == "day": 
        
        month = "all"
        
        while True:
           day = str(input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n")).lower()
           if checkDay(day):
              break
        
           else: 
                print("Oops that's not a good typing...")
    else:
        month, day = "all", "all"
                       
    print('-'*40)
    return city, month, day
#------------------My Functions ^_^ -----------------------------------------
# Months list to check user input
months = ["january", "february", "march", "april", "may", "june"]
def checkMonth(monthAnswer):
       for x in months:
            if monthAnswer == x:
                return True
       return False
# Days list to check user input
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def checkDay(dayAnswer):
     for x in days:
            if dayAnswer == x:
                return True
     return False
    
#-----------------------------------------------------------

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Loading data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        # months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filtering by day of week if applicable
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

#-----------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    print('Most common month --> ', common_month, "-", months[common_month-1])
    
    # TO DO: display the most common day of week
    print('Most common day of week --> ', df['day_of_week'].mode()[0])
    
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # Finding the most popular hour using mode function
    print('Most Popular Start Hour --> ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # Finding the most-common data using mode function
    print("Most commonly used start station -->", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    # Finding the most-common data using mode function
    print("Most commonly used end station --> ", df['End Station'].mode()[0])
    
    # TO DO: display most frequent combination of start station and end station trip
    # Finding the most-common station form start and end stations by making new coulmn and apllying the condition and using mode function
    df['start_end_station'] = np.where((df['Start Station'] == df['End Station']), df['Start Station'], np.nan)
    print("Most frequent combination of start station and end station trip -->", df['start_end_station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time 
    # Finding the total using sum function
    print("The total travel time is --> ",df["Trip Duration"].sum())

    # TO DO: display mean travel time 
    # Finding the average using mean function
    print("The mean travel time is --> ",df["Trip Duration"].mean())
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts for each user type:")
    print(df['User Type'].value_counts(), "\n")

    # TO DO: Display counts of gender
    # Check if the city is not Washington, because the gender and earliest, most recent, and most common year of birth are only available for NYC and Chicago
    if city != "washington":
        # Counting the Male and Female gender using value_counts fincrion
        print("Counts of gender:")
        print(df['Gender'].value_counts(), "\n")

        # TO DO: Display earliest, most recent, and most common year of birth
        # Finding the common year using mode function
        print("The common year --> ",int(df['Birth Year'].mode()[0]))

        # Finding the most recent year using max function
        print("The most recent year --> ",int(df['Birth Year'].max()))

        # Finding the most earliest year using min fuction
        print("The most earliest year --> ",int(df['Birth Year'].min()))
    else:
        print("Sorry the counts of gender and earliest, most recent, most common year of birth \n are only available for NYC and Chicago...")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#-----------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        # Printing 5 lines of raw data using head function after asking the user.
        answer_raw_data = input('\nDo you want to see some raw data? Enter yes or no.\n').lower()
        if answer_raw_data == 'yes':
            print(df.head()) 
        
            # Asking the user if he/she want to see more lines of raw data, if not the if condition will stop the while loop.
            rows_num = 5
            while True:
                
                raw_data = input('Do you want to see more 5 lines of raw data? Enter yes or no.\n')
                if raw_data.lower() != 'yes':
                    break
                else:
                    print(df.iloc[rows_num : rows_num + 5])
                    rows_num += 5
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
