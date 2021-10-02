import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

print (CITY_DATA.keys())
cities=['chicago','new york','washington','los angeles']
meses=['january', 'february', 'march', 'april', 'may', 'june','jul','aug']
days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
#     cities = ('chicago', 'new york', 'washington')
#     while True:
#          city = raw_input('Which of these cities do you want to explore : Chicago, New York or Washington? \n> ').lower()
#          #city = raw_input('user input for city (chicago, new york city, washington)    \n>  ').lower()
#          if city in cities :
#             break
    
    while True:
        city = input('Which of these cities do you want to explore : Chicago, New York or Washington?  \n> {} \n> '.format(cities))

        if city.casefold() in cities:
            break
        else:
            print('City is not permited')

       
    if city==cities['washington']:
        print("Looks like you want to hear about washington! if this is not true. Restart the program now!")
        while True:            
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
                        
           
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month=input('Input for month (all, january, february, ... , june\n> {}  \n>'.format(meses))
        if month.casefold() in meses:
            break
        else:
            print('Month is not permited')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    
    while True:
        day=input('Input for day of week (all, monday, tuesday, ... sunday): \n>  {}  \n >'.format(days))
        if day.casefold() in days:
            break
        else:
            print('Day is not permited')


    print('-'*40)
    return city, month, day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city.casefold()])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name.str.lower()
    df['hour'] = df['Start Time'].dt.hour                                
    #print(df['month'].mode().values )
    #print(df['day_of_week'].mode().values )
    # the function mode generate the common value of month, day
#     if month != 'all':
#         month =  meses.index(month) + 1
#         df= df[df['month'] == month]
    
                                    
#     if day != 'all':
        
#         # filter by day of week to create the new dataframe
#         df = df[ df['day_of_week'] ==day ]
    #print(df.shape)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    # TO DO:display the most common month
    #df['Start Time']= pd.to_datetime(df['Start Time'])
    #df['month'] = df['Start Time'].dt.month
    #df['month']=df['month'].mode()[0]
    #commonmonth = df['month'].mode().reset_index()
    print('The most common month is : ', df['month'].mode().values[0])

    # TO DO: display the most common day of week
    #df['day'] = df['Start Time'].dt.day
    #commonday = df['day_of_week'].mode().reset_index()
    print('The most common day is : ', df['day_of_week'].mode().values[0] )


    # TO DO: display the most common start hour
    #commonhour = df['hour'].mode().reset_index()
    print('The most common start hour is : ', df['hour'].mode().values[0] )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #df['Start Station'] = df['Start Station'].mode()[0]
    print('The most commonly used start station: ', df['Start Station'].mode())
    
    # TO DO: display most commonly used end station
    #df['End Station'] = df['End Station'].mode()[0]
    print('The most commonly used end station: ', df['End Station'].mode())
    
    # TO DO: display most frequent combination of start station and end station trip
    
    combine=df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1)
    print('The most frequent combination of start station and end station trip: \n', combine)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    hours = df['Trip Duration'] // 60
    minutes = df['Trip Duration']  - (hours * 60)
    #df['Trip Duration']=df['Trip Duration'].sum()
    print('total travel time in hours : ', hours.sum())
    print('total travel time in minutes : ', minutes.sum())
    # TO DO: display mean travel time
    print('mean travel time in hours: ', hours.mean())
    print('mean travel time in minutes: ', minutes.mean())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df['User Type'].value_counts()
    #len(user_types)
    print('counts of user types: \n>', user_types)
    # TO DO: Display counts of gender
    try: 
        gender = df['Gender'].value_counts()
        minbirth = df['Birth Year'].min()
        maxbirth = df['Birth Year'].max()
        modebirth = df['Birth Year'].mode()
        print(gender.reset_index())
        print('Display earliest, most recent, and most common year of birth :',minbirth)
        print('Display earliest, most recent, and most common year of birth :',maxbirth)
        print('Display earliest, most recent, and most common year of birth :',modebirth)    
        
    except:
        print('Column gender not available') # o Gender not available
        print('Column Bith Year not available') # o Gender not available
        
    # TO DO: Display earliest, most recent, and most common year of birth
    #df['Birth Year']=df['Birth Year'].min()
    #print('most earlisest of birth: ', df['Birth Year'].min())
    #mostrecent_year=df['Birth Year'].max()
    
    
        
    #df['Birth Year'] = df['Birth Year'].min()
        
    
    #print('most recent of birth: ', df['Birth Year'].max())
    #common=df['Birth Year'].mode()[0]
    #print('most common year of birth: ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 5
    rows=df.shape[0]
    while  start_loc<rows:
        print(df.iloc[start_loc-5:start_loc])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display!='yes':
            break
        
            
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)    
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
        
          
if __name__ == "__main__":
	main()
