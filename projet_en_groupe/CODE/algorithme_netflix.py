# ALL the imports
import pandas as pd
from tabulate import tabulate
import os
import csv
from fuzzywuzzy import process

#display(data_2)


"""file_path_1 = "/content/drive/MyDrive/Coding_project_2023/netflix_titles-2.csv"""
file_path_1 = "/Users/adrien/vscodeworkspace/coding-project/projet_en_groupe/data_cp_2023/netflix_titles-2.csv"
data_1 = pd.read_csv(file_path_1)

"""file_path_2 = "/content/drive/MyDrive/Coding_project_2023/ratings.csv"""
file_path_2 ="/Users/adrien/vscodeworkspace/coding-project/projet_en_groupe/data_cp_2023/ratings.csv"
data_2 = pd.read_csv(file_path_2)



# Show the catalog
def catalog(data_1):
    # display the head of catalog for more you can export it in a csv file
    subset_data = data_1.head(50)
    table_data = [list(row) for row in subset_data.itertuples(index=False)]
    headers = list(subset_data.columns)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    save_to_csv(data_1)

    return


def movies(data_1):
    # display the head of films for more you can export it in a csv file
    films = data_1[data_1['type'] == 'Movie']
    subset_data = films.head(50)
    table_data = [list(row) for row in subset_data.itertuples(index=False)]
    headers = list(subset_data.columns)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    save_to_csv(films)

    return


def series(data_1):
    # display the head of series for more you can export it in a csv file
    series = data_1[data_1['type'] == 'TV Show']
    subset_data = series.head(50)
    table_data = [list(row) for row in subset_data.itertuples(index=False)]
    headers = list(subset_data.columns)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    save_to_csv(series)

    return


def by_year(data_1):  # this function is used to display the data (movies, series or both) by ascending or descending the release year
    filtered_data = filter_media_type(data_1)
    sort_order = get_sort_order()
    sorted_data = sort_data_by_year(filtered_data, sort_order)

    table_data = [list(row) for row in sorted_data.head(50).itertuples(index=False)]
    headers = list(sorted_data.columns)

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    save_to_csv(sorted_data) # ask if the user want to save the data just shown

    return


def by_country(data_1) :
    filtered_data = filter_media_type(data_1)

    country_list = []
    for countries in filtered_data['country'].dropna().str.split(',') :
        for country in countries:
            cleaned_country = country.strip()  # Remove leading and trailing spaces
            if cleaned_country and cleaned_country not in country_list :
                country_list.append(cleaned_country)

    country_list.sort()
    print("List of all available countries:")
    print(tabulate(enumerate(country_list, start=1), headers=['No.', 'Country'], tablefmt='pretty'))


    while True :
        country_input = input("Enter the name of the country to display movies and/or series: ")

        # Use FuzzyWuzzy to find the closest match
        matches = process.extractOne(country_input, country_list)

        if matches[1] >= 80 :  # 80 is the threshold to compare the fuzzywuzzy used in precedent line
            country_input = matches[0] # give the name of the country
            break
        else :
            closest_match = matches[0] # give the closest match of the value entered (wich is a country)
            print(f"Invalid country name. The closest match is: {closest_match}")

    if country_input in country_list : # Check if the entered country is correct
        print(f"You selected: {country_input}")
    else :
        print(f"You entered: {country_input}, which is not in the list.")

    country_data = filtered_data[filtered_data['country'].str.lower().str.contains(country_input.lower(), case=False, na=False)] # view all the data ( of movies, series or both) for a coutnry given

    if not country_data.empty :
        print(tabulate(country_data.head(50), headers='keys', tablefmt='pretty'))
        save_to_csv(country_data)
    else :
        print(f"No movies or series found for the country {country_input}.")

    return


def genre(data_1):
    filtered_data = filter_media_type(data_1)

    genre_list = []
    for genres in data_1['listed_in'].dropna().str.split(', '):
        for genre in genres:
            if genre not in genre_list and genre != '' :
                genre_list.append(genre)

    genre_list.sort()
    print("List of all possible genres:")
    print(tabulate(enumerate(genre_list, start=1), headers=['No.', 'Genre'], tablefmt='pretty'))

    while True :
        type_input = input("Enter the type (romantic, action, drama, etc.) to display movies and/or series: ")

        matches = process.extractOne(type_input, genre_list) # Use FuzzyWuzzy to find the closest match

        if matches[1] >= 80 :  # 80 is the threshold to compare the fuzzywuzzy used in precedent line
            type_input = matches[0]
            break
        else :
            closest_match = matches[0] # give the closest match of the value entered (wich is a type of movie/series)
            print(f"Invalid genre. The closest match is: {closest_match}")

    # Check if the entered genre is correct
    if type_input in genre_list :
        print(f"You selected: {type_input}")
    else :
        print(f"You entered: {type_input}, which is not in the list.")

    type_data = filtered_data[filtered_data['listed_in'].str.lower().str.contains(type_input.lower(), case=False, na=False)] # used to filter the type in listed_in and display the data

    if not type_data.empty :
        print(tabulate(type_data.head(50), headers='keys', tablefmt='pretty'))
        save_to_csv(type_data)
    else :
        print(f"No movies or series found for the type {type_input}.")

    return


def duration(data_1):
    filtered_data = filter_media_type(data_1) # filter by media type (movies, series or both)

    genre_list = [] # Get list of all possible genres
    for genres in data_1['listed_in'].dropna().str.split(', ') :
        for genre in genres:
            if genre not in genre_list and genre != '' :
                genre_list.append(genre)

    genre_list.sort()
    print("List of all possible genres:")
    print(tabulate(enumerate(genre_list, start=1), headers=['No.', 'Genre'], tablefmt='pretty'))

    while True : # loop until the user enter a right type
        type_input = input("Enter the type (romantic, action, drama, etc.) to display movies and/or series: ") # Ask user to enter gender

        matches = process.extractOne(type_input, genre_list) # Use FuzzyWuzzy to find the closest match

        if matches[1] >= 80 :
            type_input = matches[0]
            break
        else :
            closest_match = matches[0]
            print(f"Invalid genre. The closest match is: {closest_match}")

    if type_input in genre_list : # Check if the type entered is correct
        print(f"You selected: {type_input}")
    else :
        print(f"You entered: {type_input}, which is not in the list.")

    sort_order = get_sort_order()

    type_data = filtered_data[filtered_data['listed_in'].str.lower().str.contains(type_input.lower(), case=False, na=False)].copy()

    if not type_data.empty :
        print(f"\nDisplaying data for {type_input} sorted in {'ascending' if sort_order == '1' else 'descending'} order:")

        type_data['duration'] = type_data['duration'].str.extract('(\\d+)').astype(float) # Extract numeric values ​​from the 'duration' column

        type_data_sorted = type_data.sort_values(by=['type', 'duration'], ascending=[True, sort_order == '1']) # Sort data based on type and duration

        type_data_sorted['duration'] = type_data_sorted.apply(
            lambda row: f"{int(row['duration'])} min" if row['type'].lower() == 'movie' else f"{int(row['duration'])} Season",
            axis=1
        ) # Convert duration values ​​to formatted text

        print(tabulate(type_data_sorted.head(50), headers='keys', tablefmt='pretty'))
        save_to_csv(type_data_sorted)
    else :
        print(f"No movies or series found for the type {type_input}.")

    return



def director(data_1) :
    filtered_data = filter_media_type(data_1)

    director_list = [] # get all the director possible
    for dirs in data_1['director'].dropna().str.split(', ') :
        for director_name in dirs :
            if director_name not in director_list and director_name != '' :
                director_list.append(director_name)

    print("List of all possible directors: ") # Sort the director_list in alphabetical order
    director_list = sorted(director_list) # not displayed with tabulate because the number of director is too big
    print(', '.join(director_list))

    while True :
        director_input = input("Enter the name of the director to display movies and/or series: ")

        matches = process.extractOne(director_input, director_list) # Use FuzzyWuzzy to find the closest match

        if matches[1] >= 80 : # comparison with the line fuzzyWuzzy before
            director_input = matches[0]
            break
        else :
            closest_match = matches[0]
            print(f"Invalid director name. The closest match is: {closest_match}")

    if director_input in director_list : # Check if the entered director is correct
        print(f"You selected: {director_input}")
    else :
        print(f"You entered: {director_input}, which is not in the list.")

    sort_order = get_sort_order()

    order_text = 'ascending' if sort_order == '1' else 'descending'

    director_data = filtered_data[filtered_data['director'].str.lower().str.contains(director_input.lower(), case=False, na=False)]

    if not director_data.empty :
        print(f"\nDisplaying data for movies and/or series directed by {director_input} sorted by release year in {order_text} order:")

        director_data_sorted = sort_data_by_year(director_data, sort_order)
        print(tabulate(director_data_sorted.head(50), headers='keys', tablefmt='pretty'))
        save_to_csv(director_data_sorted)
    else :
        print(f"No person found with the name {director_input}.")

    return


def actor(data_1):
    filtered_data = filter_media_type(data_1)

    actor_list = []
    for actors in data_1['cast'].dropna().str.split(', ') :
        for actor_name in actors:
            if actor_name not in actor_list and actor_name != '' :
                actor_list.append(actor_name)

    actor_list = sorted(actor_list)
    print("List of all possible actors: ") # not displayed with tabulate because the number of actor is too big
    print(', '.join(actor_list))

    while True :
        actor_input = input("Enter the name of the actor to display movies and/or series: ")

        matches = process.extractOne(actor_input, actor_list) # Use FuzzyWuzzy to find the closest match

        if matches[1] >= 80:
            actor_input = matches[0]
            break
        else :
            closest_match = matches[0]
            print(f"Invalid actor name. The closest match is: {closest_match}")

    if actor_input in actor_list : # Check if the entered actor is correct
        print(f"You selected: {actor_input}")
    else :
        print(f"You entered: {actor_input}, which is not in the list.")

    sort_order = get_sort_order()

    order_text = 'ascending' if sort_order == '1' else 'descending'

    actor_data = filtered_data[filtered_data['cast'].str.lower().str.contains(actor_input.lower(), case=False, na=False)]

    if not actor_data.empty :
        print(f"\nDisplaying data for movies and/or series featuring {actor_input} sorted by release year in {order_text} order:")

        actor_data_sorted = sort_data_by_year(actor_data, sort_order)
        print(tabulate(actor_data_sorted.head(50), headers='keys', tablefmt='pretty'))
        save_to_csv(actor_data_sorted)
    else :
        print(f"No actor found with the name {actor_input}.")

    return



def specific_genre_director(data_1) :
    filtered_data = filter_media_type(data_1)

    director_list = [] # get all the director possible
    for dirs in data_1['director'].dropna().str.split(', ') :
        for director_name in dirs :
            if director_name not in director_list and director_name != '' :
                director_list.append(director_name)

    director_list = sorted(director_list)
    print("List of all available directors:") # not displayed with tabulate because number too big
    print(', '.join(director_list))

    while True :
        director_input = input("Enter the name of the director to display movies and/or series: ")

        director_matches = process.extractOne(director_input, director_list) # Use FuzzyWuzzy to find the closest match

        if director_matches[1] >= 80 :
            director_input = director_matches[0]
            break
        else :
            closest_match = director_matches[0]
            print(f"Invalid director name. The closest match is: {closest_match}")

    if director_input in director_list : # Check if the entered director is correct
        print(f"You selected: {director_input}")
    else :
        print(f"You entered: {director_input}, which is not in the list.")

    unique_types = filtered_data['listed_in'].str.split(', ').explode().unique() # Get a list of all available types without duplicates

    unique_types = sorted(unique_types) # Sort the unique_types in alphabetical order

    print("\nList of all available types:") # display with tabulate
    print(tabulate(enumerate(unique_types, start=1), headers=['No.', 'Genre'], tablefmt='pretty'))

    while True :
        type_input = input("Enter the type (romantic, action, drama, etc.): ").capitalize()

        type_matches = process.extractOne(type_input, unique_types) # Use FuzzyWuzzy to find the closest match

        if type_matches[1] >= 80 :
            type_input = type_matches[0]
            break
        else :
            closest_match = type_matches[0]
            print(f"Invalid type. The closest match is: {closest_match}")

    if type_input in unique_types : # Check if the entered type is correct
        print(f"You selected: {type_input}")
    else :
        print(f"You entered: {type_input}, which is not in the list.")

    director_type_data = filtered_data[
        (filtered_data['director'].str.lower().str.contains(director_input.lower(), case=False, na=False)) &
        (filtered_data['listed_in'].str.lower().str.contains(type_input.lower(), case=False, na=False))
    ]

    if not director_type_data.empty :

        count = len(director_type_data) # Display the count
        print(f"The director {director_input} has directed {count} movie(s) or series of type {type_input}.")
        print(tabulate(director_type_data.head(50), headers='keys', tablefmt='pretty'))
        save_to_csv(director_type_data)

    else:
        print(f"No movies or series found for the director {director_input} and type {type_input}.")

    return


def specific_genre_actor(data_1) :
    filtered_data = filter_media_type(data_1)

    unique_actors = filtered_data['cast'].str.split(', ').explode().unique() # Get a list of unique actors
    unique_actors = [str(actor) for actor in unique_actors]

    unique_actors = sorted(unique_actors) # Sort the unique_actors in alphabetical order

    print("List of all available actors:")
    print(', '.join(unique_actors))

    while True : # Input actor name with fuzzy matching
        actor_input = input("Enter the name of the actor to display movies and/or series: ")
        actor_matches = process.extractOne(actor_input, unique_actors)

        if actor_matches[1] >= 80 : # verify the fuzzy matching
            actor_input = actor_matches[0]
            break
        else :
            closest_match = actor_matches[0]
            print(f"Invalid actor name. The closest match is: {closest_match}")

    if actor_input in unique_actors :
        print(f"You selected: {actor_input}")
    else :
        print(f"You entered: {actor_input}, which is not in the list.")

    unique_types = filtered_data['listed_in'].str.split(', ').explode().unique() # Get a list of all available types without duplicates

    unique_types = sorted(unique_types) # Sort the unique_types in alphabetical order

    print("\nList of all available types:")
    print(', '.join(unique_types))

    while True : # Input type with fuzzy matching
        type_input = input("Enter the type (romantic, action, drama, etc.): ")
        type_matches = process.extractOne(type_input, unique_types)

        if type_matches[1] >= 80 :
            type_input = type_matches[0]
            break
        else :
            closest_match = type_matches[0]
            print(f"Invalid type. The closest match is: {closest_match}")

    if type_input in unique_types :
        print(f"You selected: {type_input}")
    else :
        print(f"You entered: {type_input}, which is not in the list.")

    actor_type_data = filtered_data[
        (filtered_data['cast'].str.lower().str.contains(actor_input.lower(), case=False, na=False)) &
        (filtered_data['listed_in'].str.lower().str.contains(type_input.lower(), case=False, na=False))
    ] # Filter the data based on actor and type

    if not actor_type_data.empty :
        count = len(actor_type_data)
        print(f"The actor {actor_input} has acted in {count} movie(s) or series of type {type_input}.")
        print(tabulate(actor_type_data.head(50), headers='keys', tablefmt='pretty'))
        save_to_csv(actor_type_data)
    else :
        print(f"No movies or series found for the actor {actor_input} and type {type_input}.")

    return


# RATING FUNCTIONS

# these are variables that needs to be registered in general not in a local function
data_2['appreciation (%)'] = 0
notes = data_2.drop('show_id', axis=1)
sum_vals = notes.sum(axis=1)
data_2['appreciation (%)'] = round((sum_vals / notes.shape[1]) * 100, 2)

def most_rated(data_1, data_2) :

    filtered_data = filter_media_type(data_1)
    link_between =  pd.merge(filtered_data,data_2, on='show_id')
    link_between_sorted = link_between.sort_values(by='appreciation (%)', ascending=False)

    table_headers = ['show_id', 'title', 'type', 'appreciation (%)']
    table_data = link_between_sorted[table_headers]

    print("Films et séries les mieux notés :")
    print(tabulate(table_data.head(50), headers='keys', tablefmt='pretty'))
    save_to_csv(link_between_sorted)
    return


def most_rated_year(data_1, data_2): # Display all available unique release years
    available_years = sorted(data_1['release_year'].unique())
    print("Available years: ", available_years)

    while True: # Input year with validation
        year_input = input("Enter a release year: ")

        try:
            year = int(year_input)

            if year in available_years:
                break
            else:
                print("Please enter a valid year from the available options.")

        except ValueError:
            print("Please enter a valid year.") # Filter the data based on the release year

    filtered_data = filter_media_type(data_1[data_1['release_year'] == year])
    link_between = pd.merge(filtered_data, data_2, on='show_id')  # Merge the dataframes on the 'show_id' key
    link_between_sorted = link_between.sort_values(by='appreciation (%)', ascending=False)

    table_headers = ['show_id', 'title', 'type', 'release_year', 'appreciation (%)'] # Define headers for the tabulated table

    table_data = link_between_sorted[table_headers] # Extract relevant data for tabulation

    print(f"Top-rated shows for the year {year}:") # Print the top-rated shows for the year in a tabular format
    print(tabulate(table_data.head(50), headers='keys', tablefmt='pretty'))

    save_to_csv(link_between_sorted)  # Save the sorted data to CSV

    return


def most_rated_recent(data_1, data_2) : # we chose to display the 20 newest and highest rated movies
    merged_data = pd.merge(data_1, data_2, on='show_id') # merge the dataframes on the 'show_id' key
    sorted_data = merged_data.sort_values(by=['release_year', 'appreciation (%)'], ascending=[False, False]) # Sort the DataFrame by the 'appreciation' column (in descending order) and 'release_year' (in descending order)
    top_50_data = sorted_data.head(50) # Display the most rated and recent shows

    table_headers = ['show_id', 'title', 'type', 'release_year', 'appreciation (%)']
    table_data = top_50_data[table_headers]

    print("Top 50 most rated and recent shows:")
    print(tabulate(table_data, headers='keys', tablefmt='pretty'))

    save_to_csv(top_50_data)
    return



# PARENTAL CODE FUNCTION
def parental_code(data_1) :
    valid_codes = set(['PG-13', 'TV-MA', 'PG', 'TV-14', 'TV-PG', 'TV-Y', 'TV-Y7', 'R', 'TV-G', 'G', 'NC-17', 'NR', 'TV-Y7-FV', 'UR'])
    # there is an issue in the csv (values ​​which should not be there) more explanation with the next lines. So we sorted cause we are not allowed to modify the csv files.

    filtered_data = data_1[data_1['rating'].isin(valid_codes)] # Filter out entries that are not valid parental codes
    # the data needed to be filtered because there is a bug in the csv file with the comma. There were minutes values in the parental codes


    print("Valid parental codes:")
    print(tabulate(enumerate(valid_codes, start=1), headers=['No.', 'Parental Code'], tablefmt='pretty'))

    while True:
        selected_code = input("Enter a parental code to display movies and/or series: ")  # Ask the user to enter a parental code

        if selected_code in valid_codes:  # Filter the data based on the selected parental code
            result_data = filtered_data[filtered_data['rating'].str.contains(selected_code, case=False, na=False)]
            if not result_data.empty:
                print(tabulate(result_data.head(50), headers='keys', tablefmt='pretty'))
                save_to_csv(result_data)
            else:
                print(f"No movies or series found for the parental code {selected_code}.")
            break
        else:
            print("Invalid parental code entered. Please enter a valid code.")

    return


def directors_nationality(data_1) :

    directors_nationality_dict = {}  # Extract unique directors and their respective nationalities
    country_nationalities_set = set()

    for index, row in data_1.iterrows():
        directors = str(row['director']).split(', ') if pd.notna(row['director']) else []
        nationality = str(row['country']).split(',')

        unique_nationalities = set(filter(lambda x: pd.notna(x) and x.lower() != 'nan', map(str.strip, nationality)))  # Add unique nationalities from 'country' column to the set, excluding 'nan'
        country_nationalities_set.update(unique_nationalities)

        for director in directors :
            director = director.strip()
            if director in directors_nationality_dict :
                directors_nationality_dict[director]['nationalities'].update(unique_nationalities) # Add unique nationalities only if they are not already present
                directors_nationality_dict[director]['number of movies or series'] += 1
            else :
                directors_nationality_dict[director] = {'nationalities': set(unique_nationalities), 'number of movies or series': 1}

    sorted_directors = sorted(directors_nationality_dict.items(), key=lambda x: x[1]['number of movies or series'], reverse=True)  # sort the directors by the number of movies and series produced

    columns = ['director', 'nationalities', 'number of movies or series'] # Create a DataFrame with pandas to "SHOW" the output to the user.
    directors_df = pd.DataFrame([[director, ', '.join(info['nationalities']), info['number of movies or series']] for director, info in sorted_directors], columns=columns)

    columns = ['Director', 'Nationalities', 'Number of Movies or Series']
    directors_df = pd.DataFrame([[str(director) if pd.notna(director) else 'Unknown',
                                  ', '.join(str(n) for n in info['nationalities']),
                                  info['number of movies or series']] for director, info in sorted_directors],
                                columns=columns)

    print("Directors and their nationalities, sorted by the number of movies and series produced:")
    print(tabulate(directors_df.head(25), headers='keys', tablefmt='grid')) # Display using tabulate

    save_to_csv(directors_df) # Save to CSV using the pandas DataFrame

    return directors_df

# Allow to filter if the user want movie, tv show or both
def filter_media_type(data) :
    while True:
        print("Select the type of media:")
        print("1. Movie")
        print("2. TV Show")
        print("3. Both")

        media_choice = input("Enter the corresponding number : ")

        if media_choice in ['1', '2', '3']:
            if media_choice == '1':
                return data[data['type'].str.lower() == 'movie']
            elif media_choice == '2':
                return data[data['type'].str.lower() == 'tv show']
            else:
                return data
        else:
            print("Invalid choice. Please enter a valid number.")

# Used to sort by ascending or descending (depending on the preference of the user)
def get_sort_order() :
    while True :
        print("1. Ascending")
        print("2. Descending")
        sort_type = input("Enter the number of sort order : ")

        if sort_type in ['1', '2'] :
            return sort_type
        else:
            print("Invalid choice. Please enter 1 for ascending or 2 for descending.")

def sort_data_by_year(data, sort_order) :
    sorted_data = data.sort_values(by='release_year', ascending=(sort_order == '1'))
    return sorted_data

# STATISTICS
def basic_statistics(data_1):

    if 'type' not in data_1.columns or 'country' not in data_1.columns:
        print("The dataset does not contain the necessary columns.")
        return

    movies_count = len(data_1[data_1['type'] == 'Movie'])
    series_count = len(data_1[data_1['type'] == 'TV Show'])

    print(f"Number of movies in the catalog: {movies_count}")
    print(f"Number of series in the catalog: {series_count}")

    if movies_count > series_count:
        print("There are more movies than series in the catalog.")
    elif movies_count < series_count:
        print("There are more series than movies in the catalog.")
    else:
        print("The catalog has an equal number of movies and series.")

    country_counts = data_1['country'].str.split(', ').explode().value_counts()
    country_table = tabulate(country_counts.reset_index().head(50), headers=['Country', 'Count'], tablefmt='grid')

    print("\nCountries that produced movies/series, sorted from most to least productive:")
    print(country_table)

    return



# Allow to register a CSV file each time there was a 'show' as instruction
def save_to_csv(data, default_filename='output.csv'):
    while True:

        save_choice = input("Do you want to save the data to a CSV file? (YES/NO): ").upper()

        if save_choice == 'YES':

            file_name = input("Enter the file name (DO NOT include .csv extension, or press Enter for the default): ")  # Prompt for a file name
            file_name = file_name + ".csv"
            if not file_name:
                file_name = default_filename

            if os.path.exists(file_name):  # Check if the file already exists
                while True:
                    overwrite_choice = input(f"The file '{file_name}' already exists. Do you want to overwrite it? (YES/NO): ").upper() # Ask if the user wants to overwrite or create a new file

                    if overwrite_choice == 'YES':
                        data.to_csv(file_name, index=False) # Overwrite the existing file
                        print(f"Data saved to {file_name}")
                        break

                    elif overwrite_choice == 'NO': # Prompt for a new file name
                        new_filename = input("Enter a new file name (DO NOT include .csv extension): ")
                        new_filename = new_filename + ".csv"
                        data.to_csv(new_filename, index=False)
                        print(f"Data saved to {new_filename}")
                        break
                    else:
                        print("Invalid choice. Please enter either 'YES' or 'NO'.")

            else:
                data.to_csv(file_name, index=False)  # Save to a new file .csv
                print(f"Data saved to {file_name}")
                break

        elif save_choice == 'NO':
            print("Data not saved.")
            break

        else:
            print("Invalid choice. Please enter either 'YES' or 'NO.'")


# ALGO RECOMMENDATION
categories = [] # categories are defined on a global level


def read_movie_series_info(file_path):
    catalog = {}
    with open(file_path, 'r', encoding='utf-8') as info_file:
        info_reader = csv.reader(info_file)
        next(info_reader)  # Skip header row.
        for row in info_reader:
            show_id, show_type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description = row
            catalog[show_id] = [title, listed_in.split(', ')]
    return catalog

def read_user_ratings(file_path):
    ratings = {}
    with open(file_path, 'r', encoding='utf-8') as ratings_file:
        ratings_reader = csv.reader(ratings_file)
        header = next(ratings_reader)  # Skip header row
        user_ids = list(map(int, header[1:]))

        for row in ratings_reader:
            show_id = row[0]
            user_ratings = list(map(int, row[1:]))
            ratings[show_id] = dict(zip(user_ids, user_ratings))

    return ratings

def create_category_matrix(catalog, categories, output_file_path):
    category_matrix = [[0 for _ in range(len(categories))] for _ in range(len(categories))] # create the matrix category without the names

    for show_id, movie_categories in catalog.items(): # fill up the matrix
        for i in range(len(categories)):
            if categories[i] in movie_categories[1]:
                for j in range(len(categories)):
                    if categories[j] in movie_categories[1]: # verify if index is correct
                        if i < len(category_matrix) and j < len(category_matrix[i]):
                            category_matrix[i][j] += 1

    category_matrix_with_names = [[category] + row for category, row in zip(categories, category_matrix)] # ADD names of categories
    df = pd.DataFrame(category_matrix_with_names, columns=[''] + categories)

    df.to_excel(output_file_path, index=False) # register the dataframe in an excel because it's more readable than a matrix

    return category_matrix



def recommend_movies(user_id, catalog, user_ratings, category_matrix, threshold=0.9999): # Give recommended movies according to a threshold of similarity.
    # The threshold is very high to be very restrictive because all the users have shown loads of series and movies. allows us to be stricter on the recommendations
    global categories  # Declare categories as a global variable
    categories = list(set(category for _, movie_info in catalog.items() for category in movie_info[1]))  # allows you to update the global categories variable at the local level

    user_id = int(user_id)  # Convertir user_id en entier

    suggestions = {}
    category_index = {}

    category_index = {category: i for i, category in enumerate(categories)} # Create the dictionary to store category indices

    user_categories = categories # Added missing assignment

    for show_id, categories in catalog.items(): # Check if the user has rated the movie of series

        if show_id in user_ratings and user_id in user_ratings[show_id] and user_ratings[show_id][user_id] == 0: # verify the ratings given by the user
           # List of categories common between the film/series and the films/series rated by the user
            common_categories = [category for category in categories[1] if category in user_categories]

            if common_categories:
               # Calculate the similarity between the movie/series and the movies/series rated by the user
                similarity = sum(
                    min(category_matrix[category_index[category]][category_index[user_category]] for user_category in common_categories)
                    for category in categories[1]
                )

                # Only recommend movies/series whose similarity exceeds the specified threshold
                if similarity > threshold:
                    suggestions[show_id] = {'title': catalog[show_id][0], 'similarity': similarity}

    # Sort suggestions by decreasing similarity
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1]['similarity'], reverse=True)

    return sorted_suggestions[:5] # choosen 5 based on the instructions given

def recommandation_algorithm() :

    # Replace file_path_1 and file_path_2 with the actual file paths
    file_path_1 = "/content/drive/MyDrive/Coding_project_netflix_2023/netflix_titles-2.csv"
    file_path_2 = "/content/drive/MyDrive/Coding_project_netflix_2023/ratings.csv"

    while True :
        user_id = input("Quel est ton user ? ")

        try:
            user_id = int(user_id)
            if 1 <= user_id <= 100 :  # Check if user_id is between 1 and 100
                break  # break if user id is valid
            else:
                print("L'identifiant de l'utilisateur doit être compris entre 1 et 100.")
        except ValueError as e :
            print(f"Veuillez entrer un identifiant d'utilisateur valide. Erreur: {e}")

    # Read data from CSV files
    catalog = read_movie_series_info(file_path_1) # call the function read_movie_series_info
    ratings = read_user_ratings(file_path_2)  # call the function read_user_ratings

    # Create category matrix
    categories = list(set(category for _, movie_info in catalog.items() for category in movie_info[1]))
    output_file_path = "matrice_categories.xlsx"
    category_matrix = create_category_matrix(catalog, categories, output_file_path)


    # Display movies already viewed by the user
    print("Films déjà vus par l'utilisateur:")
    for show_id, user_rating in ratings.items():
        if user_id in user_rating and user_rating[user_id] > 0:
            print(f"- {catalog[show_id][0]}")

    # Recommend movies that the user hasn't seen yet
    recommended_movies = recommend_movies(user_id, catalog, ratings, category_matrix, threshold=0.5)

    # Display top 5 recommendations
    print("\nTop 5 recommandations:")
    for show_id, info in recommended_movies:
        print(f"Title: {info['title']}, Similarity: {info['similarity']}")


#  Menu
def action():
    print("Here are the different options available:")
    options = [
        "View the entire catalog",
        "View all movies in the catalog",
        "View all series in the catalog",
        "View all series, movies or both by year",
        "View all series, movies or both by country",
        "View all series, movies or both by type",
        "View all series, movies or both by type sorted by duration",
        "View series, movies or both directed by a specific director and sorted by year",
        "View series, movies or both featuring a specific actor and sorted by year",
        "View how many series, movies or both and series directed by a director in a specific genre",
        "View how many series, movies or both an actor has played in",
        "Display the highest-rated series, movies or both",
        "Display the highest-rated series, movies or both for a specific year",
        "Display recent highest-rated series, movies or both",
        "Display movies and series based on parental control code",
        "Display the nationalities of directors and sort the list based on the number of movies and series directed",
        "Display basic statistics",
        "Get Personalized Recommendations",
        "STOP to stop"
    ]

    # Create a list of lists for tabulate
    table = [[i + 1, option] for i, option in enumerate(options)]

    # Print the tabulated menu
    print(tabulate(table, headers=["Options", "Descriptions"], tablefmt="grid", colalign=("center", "left")))

    command = input("Enter the number of what you want to do: ")

    if command == "1" :
      catalog(data_1)
    elif command == "2" :
      movies(data_1)
    elif command == "3" :
      series(data_1)
    elif command == "4" :
      by_year(data_1)
    elif command == "5" :
      by_country(data_1)
    elif command == "6" :
      genre(data_1)
    elif command == "7" :
      duration(data_1)
    elif command == "8" :
      director(data_1)
    elif command == "9" :
      actor(data_1)
    elif command == "10" :
      specific_genre_director(data_1)
    elif command == "11" :
      specific_genre_actor(data_1)
    elif command == "12" :
      most_rated(data_1, data_2)
    elif command == "13" :
      most_rated_year(data_1, data_2)
    elif command == "14" :
      most_rated_recent(data_1, data_2)
    elif command == "15" :
      parental_code(data_1)
    elif command == "16" :
      directors_nationality(data_1)
    elif command == "17" :
      basic_statistics(data_1)
    elif command == "18" :
      recommandation_algorithm()
    elif command.upper() == "STOP" or "19" :
      return False


menu = []

while True:
    response = action()
    if response is False:
        break
    else:
        if response == True:
            menu = []
        else:
            menu.append(response)