import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Required lists
cities= ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

def get_filters():
    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
# TO DO: get user input for city
    while True:
        try:
            city = str(input("Would you like to see data for Chicago, New York City or Washington?\n ").lower())
            if city in cities:
                print(f"{city} is a nice city")
                break
        except KeyboardInterrupt:
            print("You can only choose between Chicago, New York City or Washington")
            break
        else:
            print("You can only choose between Chicago, New York City or Washington")

# TO DO: get user input for month
    while True:
        try:
            month = str(input("Pls choose a month: January, February, March, April, May, June ? Or type all.\n ").lower())
            if month in months:
                print("Good option")
                break
        except KeyboardInterrupt:
            print("missing input")
            break
        else:
            print("You need to select one month")

# TO DO: get user input for day of the week
    while True:
        try:
            day = str(input("Pls choose a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Or type all\n ").lower())
            if day in days:
                print("Nice!")
                break
        except KeyboardInterrupt:
            print("missing input")
            break
        else:
            print("You need to select one day")

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
# To load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])

    # To convert start time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # To extract month from Start Time to create new column

    df['month'] = df['Start Time'].dt.month

    # To extract day of week from Start Time to create new column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # To extract hour from Start Time to create new column
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

    # filter by month to create the new dataframe.
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("\nThe most common month is: {}".format(months[common_month].title()))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nThe most common day of week is: {}".format(common_day.title()))

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("\nThe most common start hour is: {}".format(str(common_start_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station is: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost frequent start and end station are: ', frequent_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    return df


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time in seconds is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    return df


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    ask_user = input(
        "Would you like to see raw data?[y/n]\nInput 'y' for yes or 'n' for no: ").lower()
    if ask_user.lower() != 'y':
        print("Good choice")
    if ask_user.lower() == 'y':
        print(df.head())
        view_more_data = input(
            "Would you like to see raw data?[y/n]\nInput 'y' for yes or 'n' for no: ").lower()
        m = 0
        m = m + 5
        pd.set_option('display.max_columns', 400)
        if view_more_data.lower() == 'y':
            print(df.iloc[m: m + 5])
            while True:
                try:
                    view_more_data = input(
                        "Would you like to see raw data?[y/n]\nInput 'y' for yes or 'n' for no: ").lower()
                    if view_more_data.lower() == 'y':
                        print(df.iloc[m: m + 10])

                    if view_more_data.lower() != 'y':
                        break

                except KeyboardInterrupt:
                    print('\nMissing input')
                    break

                except:
                    print("\nMissing input")

    return df


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
        main()