import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    global city
    global CITY_DATA
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = {"a":"chicago", "b":"new york city", "c":"washington"}
    while True:
        try:
            city_selection = input('To view the available bikeshare data, kindly type: \n\n The letter (a) for Chicago\n The letter (b) for New York\n the letter (c) for Washington\n  ').lower()
            if city_selection in cities.keys():
                city = cities[city_selection]
                break
        except KeyboardInterrupt:
                print('NO Input Taken')
        else:
                print('Invalid city choice!!')

    # get user filter by months of days or both

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        try:
            month = input('\n\nTo filter {}\'s data by a particular month, please type the month name as bellow or type: "all" for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:'.format(city.title())).lower()
            if month in months:
                break
        except KeyboardInterrupt:
            print('NO Input Taken')
        else:
            print("That's invalid choice, please type a valid month name or all. \nnote: you can only choose from the first 6 months of the year")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        try:
            day = input('\n\nTo filter {}\'s data filterd by {} month(s) by a day, please type the day name as bellow or type: "all" for not filtering by day: \n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n-All\n\n:'.format(city.title(),month.title())).lower()
            if day in days:
                break
        except KeyboardInterrupt:
            print('NO Input Taken')
        else:
            print("That's invalid choice, please type a valid day name or all.")


    print('-'*40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month: ', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week:', common_day)
    # display the most common start hour

    common_start_hour = df['start_hour'].mode()[0]
    print('The most common start hour is: ', common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station: ', common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: ', common_end_station)

    # display most frequent combination of start station and end station trip

    df['Start End Station'] = df[['Start Station', 'End Station']].agg('  to  '.join, axis=1)
    most_frequent_combination = df['Start End Station'].mode()[0]
    print('most frequent combination of start station and end station trip: ', most_frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration = "Trip Duration"
    column_sum = df[trip_duration].sum()
    print('total travel time= ', column_sum)

    # display mean travel time

    column_mean = df[trip_duration].mean()
    print('mean travel time=', column_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('Counts of user types:\n', user_types)

    # Display counts of gender

    while city != 'washington':
        counts_of_gender = df['Gender'].value_counts()
        print('\ncounts of gender is:\n', counts_of_gender)
        break
    else:
        print('\nyou choose to see Washington data and there is no gender data for it')


    # Display earliest, most recent, and most common year of birth

    while city != 'washington':
        earliest_yofb = df['Birth Year'].min()
        most_recent_yofb = df['Birth Year'].max()
        most_common_yofb = df['Birth Year'].mode()[0]
        print('\nthe earliest year of birth= ', earliest_yofb, '\nthe most recent year of birth= ', most_recent_yofb, '\nthe most common year of birth= ', most_common_yofb)
        break
    else:
        print('\nyou choose to see ashington data and there is no year of birth data for it')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Ask user to see 5 rows from the data
def display_raw_data(city):

    display_raw = input('May you want to have a look on five raw data? Type yes or no.\n')

    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
                print(chunk)
                display_raw = input('May you want to have a look on another five raw data? Type yes or no.\n')
                if display_raw != 'yes':
                    break
        except KeyboardInterrupt:
            print('NO Input Taken')
        else:
            print('Thank You')





    print('-'*40)
    return city, display_raw



# repeating the question


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
