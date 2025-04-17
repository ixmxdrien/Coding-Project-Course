import random
import pandas as pd
import os
import statistics
import re
from IPython.display import display
from tabulate import tabulate
from fuzzywuzzy import process

all_course_BAC1 = ("Anglais 1", "Fondements du droit public", "Fondements du droit de l'entreprise", "Economie", "Espagnol 1", "Comptabilité", "Informatique de gestion", "Mathématiques de gestion 1", "Statistiques et probabilités", "Pilosophie", "Psychologie", "Sociologie", "Séminaire de travail universitaire en gestion")

all_course_BAC2 = ("Anglais 2", "Droit de l'entreprise", "Macroéconomie", "Microéconomie", "Espagnol 2", "Marketing", "Production", "Informatique et algorithmique", "Finance", "Inférences statistiques", "Mathématiques de gestion 2", "Technologies industrielles")

all_course_BAC3 = ("Anglais 3", "Economie industrielle", "Espagnol 3", "Séminaire : organisations et transformation digitale", "Management humain", "Projet entrepreneurial", "Comptabilité et contrôle de gestion", "Gestion de données", "Coding project", "Econométrie", "Recherche opérationnelle", "Optimization", "Séminaire : organisation et mutations sociales", "Questions de sciences religieuses")

all_course_MA1 = ("Advanced English 1", "Español avanzado 1", "Data analytics", "Projet quantitatif et gestion de projet", "Data Mining", "Nouvelles technologies et pratiques émergentes", "Web mining", "Machine learning", "Quantitative Decision Making", "Recommender Systems", "Pilotage stratégique de l'entreprise", "Séminaire on Current Managerial Issues")

all_course_MA2 = ("Advanced English 2", "Español avanzado 1", "Responsabilité sociétale de l'entreprise","Integrated Information Systems", "Mémoire", "Séminaire d'accompagnement du mémoire")



file_path = '/Users/adrien/vscodeworkspace/coding-project/Data_Base.xlsx'
data = pd.read_excel(file_path)

menu = []

name_pattern = re.compile(r'^[A-Za-zéèêëàâäôöûüçÉÈÊËÀÂÄÔÖÛÜÇ][A-Za-zéèêëàâäôöûüçÉÈÊËÀÂÄÔÖÛÜÇ\'\-]*$')
date_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$')
place_of_birth_pattern = re.compile(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$')
address_pattern = re.compile(r'^[A-Za-z\s]+ \d+, [A-Za-z\s]+$')
telephone_pattern = re.compile(r'^\d{4}/\d{2}\.\d{2}\.\d{2}$')
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@student\.uclouvain\.be$')
gender_pattern = re.compile(r'^[MFO]$')
academic_year_pattern = re.compile(r'^(BAC[123]|MA[12])$')
campus_pattern = re.compile(r'^(Louvain-la-Neuve|Mons)$', re.IGNORECASE)
curriculum_pattern = re.compile(r'^(INGM1BA|INGM2M)$', re.IGNORECASE)



# function to reload data each time something is modified
def reload_data(file_path):
    return pd.read_excel(file_path)


# function to REGISTER a new student in the data base
def register_student(data):
    while True:
        user_input = input("Enter 'q' to quit or any other key to continue: ") # manage issue if you have entered the wrong number
        if user_input.lower() == 'q':
            print("Operation canceled.")
            return

        while True: # loop to verify if errors
            Firstname = input("What is the student's firstname? ")
            if name_pattern.match(Firstname):  # Check if the name matches the specified format
                print(f"The firstname is valid : {Firstname}")
                break  # Exit the loop if the name is valid
            else:
                print("The firstname is not valid. Make sure to follow the specified format.")

        while True:  # loop to verify if errors
            Lastname = input("What is the student's lastname? ")  # Ask the user for the surname
            if name_pattern.match(Lastname):
                print(f"The lastname is valid : {Lastname}")
                break  # Exit the loop if the surname is valid
            else:
                print("The lastname is not valid. Make sure to follow the specified format.")

        while True:  # loop to verify if errors
            Date_of_birth = input("Please enter a date in the format dd/mm/yyyy: ") # Ask the user for the birthdate
            if date_pattern.match(Date_of_birth): # check if the format is respected
                print(f"The date is valid : {Date_of_birth}")
                break  # Exit the loop if the date is valid
            else:
                print("The date is not valid. Make sure to follow the format dd/mm/yyyy.")

        while True:  # loop to verify if errors
            Place_of_birth = input("What is the city of birth? ")
            if place_of_birth_pattern.match(Place_of_birth):
                print(f"The place of birth is valid : {Place_of_birth}")
                break  # Exit the loop if the city of birth is valid
            else:
                print("The city of birth is not valid. Make sure to use only letters and spaces.")

        while True:  # loop to verify if errors
            Address = input("Please enter an address in the format 'street number, city': ")
            if address_pattern.match(Address):
                print(f"The address is valid : {Address}")
                break  # Exit the loop if the address is valid
            else:
                print("The address is not valid. Make sure to follow the format 'street number, city'.")

        while True:  # loop to verify if errors
            Telephone = input("What is the telephone number? (in the format 0000/00.00.00) ")
            if telephone_pattern.match(Telephone):
                print(f"The telephone number is valid : {Telephone}")
                break  # Exit the loop if the telephone number is valid
            else:
                print("The telephone number is not valid. Make sure to follow the requested format.")

        print("The email address was completed automatically. If it is not suitable you can modify it later : ")
        email_of_student = f"{Firstname}{'.'}{Lastname}{'@student.uclouvain.be'}" # this is automaticaly attributed based on the firstname and lastname
        Email = email_of_student.lower()
        print(Email)

        while True:  # loop to verify if errors
            Gender = input("What is your gender? (For Male enter M, for Female enter F, and for another type enter O): ")
            if gender_pattern.match(Gender):
                print(f"The gender is valid : {Gender}")
                break  # Exit the loop if the gender is valid
            else:
                print("The gender is not valid. Make sure to follow the requested format.")

        while True:  # loop to verify if errors
            Academic_year = input("What is your academic year? (BAC1/BAC2/BAC3/MA1/MA2): ")
            if academic_year_pattern.match(Academic_year):
                print(f"The academic year is valid : {Academic_year}")
                break  # Exit the loop if the academic year is valid
            else:
                print("The academic year is not valid. Make sure to follow the requested format.")

        if Academic_year in ['BAC1', 'BAC2', 'BAC3'] : # Curriculum is automatically attributed depeding on the academic year.
            Curriculum = "INGM1BA"
        else :
            Curriculum = "INGM2M"

        Courses_and_grade = {}
        if Academic_year == 'MA2':
            for course in all_course_BAC1 + all_course_BAC2 + all_course_BAC3 + all_course_MA1 + all_course_MA2: # for  instance, if you are in MA2 you need to enter every gardes of each courses.
                grade = input(f"What is the grade for {course}? ")
                while not grade.isdigit() or int(grade) not in range(0, 21):
                    print("The grade must be an integer between 0 and 20.")
                    grade = input(f"What is the grade for {course}? ")
                Courses_and_grade[course] = int(grade)

        elif Academic_year == 'MA1':
            for course in all_course_BAC1 + all_course_BAC2 + all_course_BAC3 + all_course_MA1: # same as before every course unless MA2 because you are not in yet.
                grade = input(f"What is the grade for {course}? ")
                while not grade.isdigit() or int(grade) not in range(0, 21):
                    print("The grade must be an integer between 0 and 20.")
                    grade = input(f"What is the grade for {course}? ")
                Courses_and_grade[course] = int(grade)

        elif Academic_year == 'BAC3':
            for course in all_course_BAC1 + all_course_BAC2 + all_course_BAC3:
                grade = input(f"What is the grade for {course}? ")
                while not grade.isdigit() or int(grade) not in range(0, 21):
                    print("The grade must be an integer between 0 and 20.")
                    grade = input(f"What is the grade for {course}? ")
                Courses_and_grade[course] = int(grade)

        elif Academic_year == 'BAC2':
            for course in all_course_BAC1 + all_course_BAC2:
                grade = input(f"What is the grade for {course}? ")
                while not grade.isdigit() or int(grade) not in range(0, 21):
                    print("The grade must be an integer between 0 and 20.")
                    grade = input(f"What is the grade for {course}? ")
                Courses_and_grade[course] = int(grade)

        elif Academic_year == 'BAC1':
            for course in all_course_BAC1:
                grade = input(f"What is the grade for {course}? ")
                while not grade.isdigit() or int(grade) not in range(0, 21):
                    print("The grade must be an integer between 0 and 20.")
                    grade = input(f"What is the grade for {course}? ")
                Courses_and_grade[course] = int(grade)

        while True:
            Campus = input("Enter 'Louvain-la-Neuve' or 'Mons' depending on the campus: ") # Only 2 campus possible but it must respect the pattern of the campus
            if campus_pattern.match(Campus):
                print("The campus choice is valid.")
                break  # Exit the loop if the campus choice is valid
            else:
                print("The campus choice is not valid. Make sure to follow the requested format.")

        matricule = generate_matricule(Firstname, Lastname, Date_of_birth) # call the function matricule to generate a matricule

        register(data, Firstname, Lastname, Curriculum, Date_of_birth, Place_of_birth, Address, Telephone, Email, Gender, Academic_year, Courses_and_grade, Campus, matricule) # Call the function register to register a student with these informations

        # Display the entered information by the user.
        print("\nEntered Information:")
        print(f"Firstname: {Firstname}")
        print(f"Lastname: {Lastname}")
        print(f"Date of Birth: {Date_of_birth}")
        print(f"Place of Birth: {Place_of_birth}")
        print(f"Address: {Address}")
        print(f"Telephone: {Telephone}")
        print(f"Email: {Email}")
        print(f"Gender: {Gender}")
        print(f"Academic Year: {Academic_year}")
        print(f"Curriculum: {Curriculum}")
        print(f"Courses and Grades: {Courses_and_grade}")
        print(f"Campus: {Campus}")
        print(f"Matricule: {matricule}")

        while True:
            # Ask the user if they want to modify any information before registration because mistakes are always possible
            modify_info = input("Do you want to modify any information before registration? (YES/NO): ").upper()
            if modify_info == "YES":
                data = reload_data(file_path)
                modify(data)  # Call the modify function to update information (which may be false or incorrectly entered)
                break  # Exit the loop after modification
            elif modify_info == "NO":
                break  # Exit the loop if no modification is needed.
            else:
                print("Invalid input. Please enter either 'YES' or 'NO'.")

        return



# the function is used to register the data in the file and to reload the file.
def register(data, firstname, lastname, Curriculum, date_of_birth, place_of_birth, address, telephone, email, gender, academic_year, courses_and_grade, campus, matricule):

    student = {
        "Firstname": firstname,
        "Lastname": lastname,
        "Curriculum":Curriculum,
        "Date of Birth": date_of_birth,
        "Place of Birth": place_of_birth,
        "Address": address,
        "Telephone": telephone,
        "Email": email,
        "Gender": gender,
        "Academic Year": academic_year,
        "Campus": campus,
        "Matricule": matricule
    }

    for course, grade in courses_and_grade.items():
        student[course] = grade

    student_df = pd.DataFrame([student])
    data = pd.concat([data, student_df], ignore_index=True)

    data.to_excel(file_path, index=False)

    data = reload_data(file_path)

    print('The person has been registered.\n')

    return data

# Used to generate the matricule of the student.
def generate_matricule(firstname, lastname, date_of_birth):
    consonant_of_firstname = ''.join([c for c in firstname if c.lower() not in 'aeiou'])[:3]
    consonant_of_lastname = ''.join([c for c in lastname if c.lower() not in 'aeiou'])[:2]
    last_consonant_of_lastname = ''.join([c for c in lastname if c.lower() not in 'aeiou']).lower()[-1]
    year_of_birth_string = str(date_of_birth)[-4:]
    random_integer = random.randint(0, 10)
    matricule = f"{consonant_of_lastname }{consonant_of_firstname}{last_consonant_of_lastname}{year_of_birth_string}{random_integer}"
    matricule = matricule.lower()

    return matricule

# MODIFYING THE DATA OF A STUDENT
def modify(data):
    while True:
        matricule_to_modify = input("Enter the matricule of the student you want to modify (or 'q' to quit): ") # matricule is unique, that's why I based my function modify on it
        if matricule_to_modify.lower() == 'q': # back to the menu if you entered the wrong number.
            print("Operation canceled.")
            break

        student_row = data[data['Matricule'] == matricule_to_modify.lower()]

        if student_row.empty:
            print("No student found with the specified matricule.") # the matricule encoded can be False. I didn't used the fuzzywuzzy because I wanted the matricule to be written correctly to modify information.
            return

        print("\nDetails of the student before modification:")
        print(student_row[['Matricule', 'Firstname', 'Lastname']]) # Better to give important information about the student before modifying it, to be sure it is him or her.

        confirmation = input("Do you really want to modify this student? (YES/NO) ").upper() # to make sure it's the right student
        if confirmation == "YES":
            student_index = student_row.index[0]

            print("\nDetails of the student before modification:") # Give all the information about the student.
            for col in ['Matricule', 'Firstname', 'Lastname', 'Date of Birth', 'Place of Birth', 'Address', 'Telephone', 'Email', 'Gender', 'Academic Year', 'Curriculum', 'Campus']:
                print(f"{col}: {data.at[student_index, col]}")
            for course, grade in data.iloc[student_index].items(): # Display all the course that the student has already done
                if course not in field_mapping.values():
                    print(f"{course}: {grade}")

            print(f"\nModifying the student with matricule {matricule_to_modify}:\n") # display the information and what can be modified
            print("1.  Firstname")
            print("2.  Lastname")
            print("3.  Date of Birth")
            print("4.  Place of Birth")
            print("5.  Address")
            print("6.  Telephone")
            print("7.  Email")
            print("8.  Sex (M | F | O)")
            print("9.  Academic Year")
            print("10. Curriculum")
            print("11. Courses already passed and their grade")
            print("12. Campus")

            field_to_modify = int(input("Enter the number of the field you want to modify: "))

            field_name_to_modify = field_mapping.get(field_to_modify, None)
            print(f"You are modifying the field: {field_name_to_modify}")

            matricule = None

            if field_to_modify == 1:  # If the field to modify is the name (Name)
                while True:
                    firstname = input("What is the name you want to modify? ")
                    if name_pattern.match(firstname):  # respect the pattern, same as register function
                        print(f"The firstname is valid : {firstname}")
                        if field_to_modify in (1, 2, 3): # if you are modifying one of the 3 informations it will modify the matricule.
                            matricule = generate_matricule(firstname, data.at[student_index, 'Lastname'], data.at[student_index, 'Date of Birth'])
                        data.at[student_index, 'Firstname'] = firstname
                        break  # Exit the loop if the name is valid
                    else:
                        print("The name is not valid. Make sure to follow the specified format.")
            elif field_to_modify == 2:
                while True:  # Ask the user for the surname
                    lastname = input("What is the surname? ")
                    if name_pattern.match(lastname):  # respect the pattern, same as register function
                        print(f"The lastname is valid : {lastname}")
                        if field_to_modify in (1, 2, 3):  # if you are modifying one of the 3 informations it will modify the matricule.
                            matricule = generate_matricule(data.at[student_index, 'Firstname'], lastname, data.at[student_index, 'Date of Birth'])
                        data.at[student_index, 'Lastname'] = lastname
                        break  # Exit the loop if the surname is valid
                    else:
                        print("The surname is not valid. Make sure to follow the specified format.")
            elif field_to_modify == 3:
                while True:
                    date_of_birth = input("Please enter a date in the format dd/mm/yyyy: ")
                    if date_pattern.match(date_of_birth):  # respect the pattern, same as register function
                        print(f"The date is valid : {date_of_birth}")
                        if field_to_modify in (1, 2, 3):  # if you are modifying one of the 3 informations it will modify the matricule.
                            matricule = generate_matricule(data.at[student_index, 'Firstname'], data.at[student_index, 'Lastname'], date_of_birth)
                        data.at[student_index, 'Date of Birth'] = date_of_birth
                        break  # Exit the loop if the date is valid
                    else:
                        print("The date is not valid. Make sure to follow the format dd/mm/yyyy.")
            elif field_to_modify == 4:
                while True:
                    place_of_birth = input("What is the city of birth? ")
                    if place_of_birth_pattern.match(place_of_birth):  # respect the pattern, same as register function
                        print(f"The city of birth is valid : {place_of_birth}")
                        data.at[student_index, 'Place of Birth'] = place_of_birth
                        break  # Exit the loop if the city of birth is valid
                    else:
                        print("The city of birth is not valid. Make sure to use only letters and spaces.")
            elif field_to_modify == 5:
                while True:
                    address = input("Please enter an address in the format 'street number, city': ")
                    if address_pattern.match(address): # respect the pattern, same as register function
                        print(f"The address is valid : {address}")
                        data.at[student_index, 'Address'] = address
                        break  # Exit the loop if the address is valid
                    else:
                        print("The address is not valid. Make sure to follow the format 'street number, city'.")
            elif field_to_modify == 6:
                while True:
                    telephone = input("What is the telephone number? (in the format 000/00.00.00) ")
                    if telephone_pattern.match(telephone):  # respect the pattern, same as register function
                        print(f"The telephone number is valid : {telephone}")
                        data.at[student_index, 'Telephone'] = telephone
                        break  # Exit the loop if the telephone number is valid
                    else:
                        print("The telephone number is not valid. Make sure to follow the requested format.")
            elif field_to_modify == 7:
                while True:
                    email = input("Enter the university email (@student.uclouvain.be): ")
                    if email_pattern.match(email):
                        print(f"The email is valid : {email}")
                        data.at[student_index, 'Email'] = email
                        break  # Exit the loop if the email is valid
                    else:
                        print("The email is not valid. Make sure to follow the requested format.")
            elif field_to_modify == 8:
                while True:
                    gender = input("What is your gender? (For Male enter M, for Female enter F, and for other type enter O): ")
                    if gender_pattern.match(gender):
                        print(f"The gender is valid : {gender}")
                        data.at[student_index, 'Gender'] = gender
                        break  # Exit the loop if the gender is valid
                    else:
                        print("The gender is not valid. Make sure to follow the requested format.")
            elif field_to_modify == 9:
                while True:
                   academic_year = input("What is your academic year? (BAC1/BAC2/BAC3/MA1/MA2): ")

                   if academic_year_pattern.match(academic_year):
                       print(f"The academic year is valid: {academic_year}")

                       if academic_year in ['BAC1', 'BAC2', 'BAC3']: # it attributes automatically the curriculum based on the academic year
                           curriculum = "INGM1BA"
                       elif academic_year in ['MA1', 'MA2']:
                           curriculum = "INGM2M"
                       else:
                           print("Invalid academic year for curriculum assignment.")
                           continue

                       data.at[student_index, 'Academic Year'] = academic_year # attributes the values in the column for the student concerned
                       data.at[student_index, 'Curriculum'] = curriculum
                       break  # Exit the loop if the academic year is valid
                   else:
                       print("The academic year is not valid. Make sure to follow the requested format.")
            elif field_to_modify == 10:
                while True:
                    curriculum = input("What is your curriculum? (INGM1BA/INGM2M): ")

                    if curriculum_pattern.match(curriculum):
                        if curriculum == 'INGM1BA':
                            valid_academic_years = ['BAC1', 'BAC2', 'BAC3'] # defines the valid academic years
                        elif curriculum == 'INGM2M':
                            valid_academic_years = ['MA1', 'MA2']

                        academic_year = input(f"What is your academic year? ({'/'.join(valid_academic_years)}): ")

                        if academic_year in valid_academic_years and academic_year_pattern.match(academic_year): # verify if the academic year and curriculum correspond
                            print(f"The academic year for {curriculum} is valid: {academic_year}")
                            data.at[student_index, 'Academic Year'] = academic_year
                            data.at[student_index, 'Curriculum'] = curriculum
                            break  # Exit the loop if both curriculum and academic year are valid
                        else:
                            print("Invalid academic year for the selected curriculum. Make sure to follow the requested format.")
                    else:
                        print("Invalid curriculum. Make sure to follow the requested format.")
            elif field_to_modify == 11:  # Courses and grades
                print("Courses already passed and their grade:\n")
                courses = [course for course in data.iloc[student_index].index if course not in field_mapping.values()]
                for i, course in enumerate(courses, start=1):
                  grade = data.at[student_index, course]
                  print(f"{i}. {course}: {grade}")

                while True:
                    course_number_to_modify = input("Enter the number of the course you want to modify: ")

                    try:
                        course_number_to_modify = int(course_number_to_modify)
                    except ValueError:
                        print("Please enter a valid number.")
                        continue


                    if 1 <= course_number_to_modify <= len(courses):
                        course_to_modify = courses[course_number_to_modify - 1]
                        print(f"The specified course ({course_number_to_modify}) has been found: {course_to_modify}.")
                        break
                    else:
                      print("Invalid course number. Please select a valid one.")

                new_grade = input(f"Enter the new grade for {course_to_modify}: ")

                while not new_grade.isdigit() or int(new_grade) not in range(0, 21):
                    print("The grade must be an integer between 0 and 20.")
                    new_grade = input(f"Enter the new grade for {course_to_modify}: ")

                data.at[student_index, course_to_modify] = int(new_grade)

            elif field_to_modify == 12:
                while True:
                    campus = input("Enter 'Louvain-la-Neuve' or 'Mons' depending on the campus: ")
                    if campus_pattern.match(campus):
                        print(f"The campus choice is valid : {campus}")
                        data.at[student_index, 'Campus'] = campus
                        break  # Exit the loop if the campus choice is valid
                    else:
                      print("The campus choice is not valid. Make sure to follow the requested format.")

        else:
            print("Modification canceled.")
            break  # Exit the loop if modification is canceled

        if matricule is not None:
            data.at[student_index, 'Matricule'] = matricule  # Update the Matricule column with the new matricule

        print("Be careful because of a modification the registration number has changed :") # Tell the user that the firstname,lastname or birthdate has been modified

        print(f"the new matricule is : {matricule}") # give the new matricule

        # Save the modified data to the Excel file
        data.to_excel(file_path, index=False) # append the file with data modified
        data = reload_data(file_path) # reload the data to update the data base.
        print("Modification successfully done.")

# Mapping for field names to DataFrame column names
field_mapping = {
    1:  'Firstname',
    2:  'Lastname',
    3:  'Date of Birth',
    4:  'Place of Birth',
    5:  'Address',
    6:  'Telephone',
    7:  'Email',
    8:  'Gender',
    9:  'Academic Year',
    10: 'Curriculum',
    11: 'Courses and Grades',
    12: 'Campus'
}


# DELETION OF A STUDENT based on his matricule because it's unique as the modification function.
def delete(data):
    while True:
        user_input = input("Enter 'q' to quit or any other key to continue: ")
        if user_input.lower() == 'q':
            print("Operation canceled.")
            return

        matricule_to_delete = input("Enter the matricule of the student you want to delete: ")
        student_index = data[data['Matricule'] == matricule_to_delete.lower()].index.tolist() # no fuzzywuzzy because I wanted the matricule to be entered correctly

        if not student_index:
            print("No student found with the specified matricule.")
            return

        student_index = student_index[0]
        print(f"\nDeleting the student with matricule {matricule_to_delete}:\n")

        print("Details of the student before deletion:")  # Display the details of the student before deletion
        print(data.iloc[student_index]) # give all the data of the student

        confirmation = input("Do you really want to delete this student? (YES/NO) ").upper() # to make sure the user really want to delete the student
        if confirmation == "YES":
            data = data.drop(index=student_index) # .drop allows the deletion

            data.to_excel(file_path, index=False)  # Save the modified data to the Excel file
            print("Deletion successful.")
        else:
            print("Deletion canceled.")


# FIND the student based on different search criteria
def find_student(data):
    while True:
        user_input = input("Enter 'q' to quit or any other key to continue: ")
        if user_input.lower() == 'q':
            print("Operation canceled.")
            return
        print("Below are the search criteria:")
        print("1. By his/her Lastname")
        print("2. By his/her Firstname")
        print("3. By his/her Matricule")

        while True:
            search_criteria = input("Enter the number of what you want to do: ")

            if search_criteria == "1":
                surname_search = input("Enter the lastname of the student: ")
                results = find_similar_data(data['Lastname'], surname_search, 'Lastname')
                break
            elif search_criteria == "2":
                name_search = input("Enter the firstname of the student: ")
                results = find_similar_data(data['Firstname'], name_search, 'Firstname')
                break
            elif search_criteria == "3":
                matricule_search = input("Enter the matricule of the student: ")
                results = find_similar_data(data['Matricule'], matricule_search, 'Matricule')
                break
            else:
                print("Invalid search criteria. Please enter a valid number.")

        if results.empty:
            print("No student found with the specified criteria.")
        else:
            print("Student(s) found:")
            for index, row in results.iterrows():
                print(f"Firstname: {row['Firstname']}, Lastname: {row['Lastname']}, Matricule: {row['Matricule']}")

def find_similar_data(column, search_term, column_name):

    results = process.extractBests(search_term, column, score_cutoff=80)  # Using fuzzywuzzy to find similar values in the specified column with a specified threshold.
    similar_values = [result[0] for result in results]

    if similar_values: # Display suggestions if there are similar values
        print(f"Suggestions for {column_name}: {', '.join(similar_values)}")

    filtered_data = column.isin(similar_values)  # Filter the DataFrame based on similar values
    return data[filtered_data]

# SHOW all the student
def filter_students(data):
    if data.empty:
        print("The list of students is empty.")
    else:
        table_data = []
        for index, row in data.iterrows():
            table_data.append([row['Firstname'], row['Lastname'], row['Matricule']]) # the data that are displayed

        headers = ["Firstname", "Lastname", "Matricule"]
        print(tabulate(table_data, headers=headers, tablefmt="pretty")) # using tabulate is better in term of display

        export_to_excel(data) # call the finction to export
    read_choice = input("Do you want to read the exported list from an Excel file? (YES/NO): ").upper()
    if read_choice == "YES":
        read_exported_list() # read an exported file on the terminal

def export_option(data):
    while True:
        export = input("Do you want to export in a file? (YES/NO) ").upper()
        if export == "YES":
            filename = input("Enter the filename without .xlsx: ")
            filename = filename + '.xlsx'
            export_data_to_excel(data, filename)
            break
        elif export == "NO":
            print("Export canceled.")
            break
        else:
            print("Invalid input. Please enter either 'YES' or 'NO'.")


def export_to_excel(data):
    excel_filename = input("Enter the name of the Excel file (without extension): ")
    excel_filename += ".xlsx"

    try:
        data.to_excel(excel_filename, index=False) #
        print(f"List successfully exported to {excel_filename}.")
    except Exception as e:
        print(f"An error occurred during export: {e}")

def read_exported_list(): # Enter the file name with the extension to display it in the terminal
    excel_filename = input("Enter the name of the Excel file to read (include .xlsx extension): ")

    try:
        exported_data = pd.read_excel(excel_filename) # try to open the doc
        print("\nExported List:")
        print(exported_data)
        print("\nExported list successfully read from Excel.")
    except FileNotFoundError: # the doc can't be found that's an exception
        print(f"File not found: {excel_filename}")
    except Exception as e: # sometimes the type of error is different and must be display to understand the issue
        print(f"An error occurred during reading: {e}")



# SORTING
def sort(data):
    print("Below are the sort criteria:")
    sort_options = [
        ["1", "Sort in ascending alphabetical order"],
        ["2", "Sort in descending alphabetical order"],
        ["3", "Sort by date of birth"],
        ["4", "Sort by age"],
        ["5", "Sort by matricule"],
        ["6", "Sort by academic year"],
        ["7", "Get all people who passed a course"],
        ["8", "Get all people who failed a course"],
        ["9", "Get all Bachelor students"],
        ["10", "Get all Master students"]
    ]

    print(tabulate(sort_options, headers=["Option", "Description"], tablefmt="pretty", colalign=("center", "left")))

    sorting_choice = input("Enter the number of what you want to do: ")
    if sorting_choice == "1":
        sort_ascending(data)  # all the differents call / type of sorting
    elif sorting_choice == "2":
        sort_descending(data)
    elif sorting_choice == "3":
        sort_by_date(data)
    elif sorting_choice == "4":
        sort_by_age(data)
    elif sorting_choice == "5":
        sort_by_matricule(data)
    elif sorting_choice == "6":
        sort_by_academic_year(data)
    elif sorting_choice == "7":
        sort_passed(data)
    elif sorting_choice == "8":
        sort_failed(data)
    elif sorting_choice == "9":
        sort_bachelor(data)
    elif sorting_choice == "10":
        sort_master(data)
    return

# all the export option is done with all the data (Firstname,...,Address, and all the course) sorting with a specific type
# all the show option is done with the most important informations about the students.
def sort_ascending(data):
    sorted_data = data.sort_values(by=['Firstname', 'Lastname'], ascending=[True, True])
    see_the_data(sorted_data, columns_to_show=['Firstname', 'Lastname', 'Matricule'])
    export_option(sorted_data) # asking if the user want to export

def sort_descending(data):
    sorted_data = data.sort_values(by=['Firstname', 'Lastname'], ascending=[False,True])
    see_the_data(sorted_data, columns_to_show=['Firstname', 'Lastname', 'Matricule'])
    export_option(sorted_data)

def sort_by_date(data):
    data['Date of Birth'] = pd.to_datetime(data['Date of Birth'], format='%d/%m/%Y')
    sorted_data = data.sort_values(by=['Date of Birth', 'Firstname', 'Lastname'])# also sort by firstname and lastname to be more precise
    see_the_data(sorted_data, columns_to_show=['Firstname', 'Lastname', 'Date of Birth'])
    export_option(sorted_data)

def sort_by_age(data):
    data['Date of Birth'] = pd.to_datetime(data['Date of Birth'], format='%d/%m/%Y')
    today = pd.to_datetime('today')
    age_timedelta = today - data['Date of Birth']
    data['Age'] = (age_timedelta / pd.Timedelta(days=365.25)).astype(int) # allow us to transform the data by age
    sorted_data = data.sort_values(by=['Age', 'Firstname', 'Lastname'], ascending=[True,True,True]) # also sort by firstname and lastname to be more precise
    see_the_data(sorted_data, columns_to_show=['Firstname', 'Lastname', 'Age'])
    export_option(sorted_data)

def sort_by_matricule(data):
    sorted_data = data.sort_values(by='Matricule', ascending=True) # matricule is unique so no  other sorting type needed
    see_the_data(sorted_data, columns_to_show=['Firstname', 'Lastname', 'Matricule'])
    export_option(sorted_data)

def sort_by_academic_year(data):
    sorted_data = data.sort_values(by=['Academic Year', 'Firstname', 'Lastname'], ascending=[True,True,True]) # also sort by firstname and lastname to be more precise
    see_the_data(sorted_data, columns_to_show=['Firstname', 'Lastname', 'Academic Year'])
    export_option(sorted_data)


def sort_passed(data):
    course_columns = data.columns[12:] # take the data from the 12 to the last
    print("Available Courses:")
    for i, course in enumerate(course_columns, 1):
        print(f"{i}. {course}") # print all the course

    while True:
        try:
            choice = int(input("Enter the number of the course you want to display: "))
            selected_course = course_columns[choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

    passed_data = data[data[selected_course] >= 10] # course transfer in a list for the course with note more than 10 or equal to

    passed_data = passed_data.sort_values(by=['Firstname', 'Lastname', selected_course], ascending=[True, True,True])

    see_the_data(passed_data, columns_to_show=['Firstname', 'Lastname', selected_course])
    export_option(passed_data)



def sort_failed(data):
    course_columns = data.columns[12:]  # take the data from the 12 to the last
    print("Available Courses:")
    for i, course in enumerate(course_columns, 1):
        print(f"{i}. {course}")

    while True:
        try:
            choice = int(input("Enter the number of the course you want to display: "))
            selected_course = course_columns[choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

    failed_data = data[data[selected_course] < 10]  # course transfer in a list for the course with note less than 10

    failed_data = failed_data.sort_values(by=['Firstname', 'Lastname', selected_course], ascending=[True, True,True])

    see_the_data( failed_data, columns_to_show=['Firstname', 'Lastname', selected_course])
    export_option(failed_data)


def sort_bachelor(data): # search all the student of bachelor and sort them by academic year to have a better view
    bachelor_data = data[data['Academic Year'].isin(['BAC1', 'BAC2', 'BAC3'])].sort_values(by=['Academic Year', 'Firstname', 'Lastname'], ascending=[True, True,True])
    see_the_data(bachelor_data, columns_to_show=['Firstname', 'Lastname', 'Academic Year'])
    export_option(bachelor_data)

def sort_master(data):
    master_data = data[data['Academic Year'].isin(['MA1', 'MA2'])].sort_values(by=['Academic Year', 'Firstname', 'Lastname'], ascending=[True, True,True])
    see_the_data(master_data, columns_to_show=['Firstname', 'Lastname', 'Academic Year'])
    export_option(master_data)

# exporting the data
def export_option(data):
    export = input("Do you want to export in a file? (YES/NO) ").upper()
    if export == "YES":
        filename = input("Enter the filename without .xlsx : ")
        filename = filename + '.xlsx'
        export_data_to_excel(data, filename)


def export_data_to_excel(data, filename):
    data.to_excel(filename, index=False)
    print(f"\nData exported to {filename}")

# see the data needed
def see_the_data(data, columns_to_show=None):
    if columns_to_show is None:
        columns_to_show = data.columns

    data_to_show = data[columns_to_show]
    table = tabulate(data_to_show, headers='keys', tablefmt='grid')
    print(table)



# STATS
def statistics_analysis(data):
    print_menu(["Get basic statistics of a student", "Get all grades of a student", "Get all grades of a course"]) # call the function pritnt menu

    stats_choice = get_valid_input("Enter the number of what you want to do: ", 1, 3) # user enter the number he want to do.

    if stats_choice == 1:
        results = search_and_display_stats(data, "Statistics")
    elif stats_choice == 2:
        results = search_and_display_stats(data, "Grades")
    elif stats_choice == 3:
        results = course_grades(data)

def print_menu(options):
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

def get_valid_input(prompt, lower_limit, upper_limit): # verify if the input is correct
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            user_choice = int(user_input)
            if lower_limit <= user_choice <= upper_limit:
                return user_choice
            else:
                print(f"The choice must be between {lower_limit} and {upper_limit}.")
        else:
            print("Invalid input. Please enter a valid number.")

def search_and_display_stats(data, stats_type):
    print_menu(["Search by Firstname", "Search by Lastname", "Search by Matricule"])
    search_criteria = get_valid_input(f"Enter the number of the search criteria for student {stats_type}: ", 1, 3)

    if search_criteria == 1:
        field_name = "Firstname"
    elif search_criteria == 2:
        field_name = "Lastname"
    elif search_criteria == 3:
        field_name = "Matricule"
    else:
        print("Invalid search criteria.")
        return

    search_term = input(f"Enter the {field_name.lower()} of the student: ")
    results = data[data[field_name].str.contains(search_term, case=False, na=False)] # search the stat with the search criteria

    if not results.empty:
        if stats_type == "Statistics":
            display_statistics(results, data)
        elif stats_type == "Grades":
            display_student_grades(results, data)
    else:
        print(f"No students found with the specified {field_name}.")


# STATISTICAL_STUDENT selected via the menu
def display_statistics(results, data):
    numeric_columns = results.select_dtypes(include=['number']).columns


    with pd.ExcelWriter('student_statistics.xlsx', engine='xlsxwriter') as excel_writer: # Create a pandas excel writer
        for index, row in results.iterrows():
            student_name = f"{row['Firstname']} {row['Lastname']}"
            student_grades = [row[column] for column in numeric_columns if not pd.isnull(row[column])]

            if student_grades:
                # Print and save student statistics
                print_student_statistics(student_name, student_grades, excel_writer)

        print("Statistics exported to student_statistics.xlsx.")

def export_statistics(export_path, overwrite) :
    if overwrite == "NO":
        new_file_name = input("Enter a new Excel file name (without extension): ") + '.xlsx'
        export_path = new_file_name

    return export_path

def calculate_student_stats(student_grades) :
    student_stats = {
        "Lowest grade": min(student_grades),
        "Highest grade": max(student_grades),
        "Average grade": statistics.mean(student_grades),
        "Median grade": statistics.median(student_grades),
        "Standard deviation of grades": statistics.stdev(student_grades)
    }

    return pd.DataFrame(list(student_stats.items()), columns=["Metric", "Value"])

def print_student_statistics(student_name, student_grades, excel_writer) :
    lowest_grade = min(student_grades)
    highest_grade = max(student_grades)
    average_grade = statistics.mean(student_grades)
    median_grade = statistics.median(student_grades)
    std_deviation = statistics.stdev(student_grades)

    table = [
        ["Lowest grade", lowest_grade],
        ["Highest grade", highest_grade],
        ["Average grade", average_grade],
        ["Median grade", median_grade],
        ["Standard deviation of grades", std_deviation]
    ]

    # Print student statistics
    print(f"\nStatistics for student {student_name}:")
    print(tabulate(table, headers=["Metric", "Value"], tablefmt="pretty"))


    export_df = calculate_student_stats(student_grades)  # Save student statistics to a separate Excel sheet
    export_df.to_excel(excel_writer, sheet_name=student_name, index=False)



# STUDENT_GRADES
def display_student_grades(results, data) :
    student_data_dict = {}# Create a dictionary to store data for each student

    for index, row in results.iterrows() :
        student_name = f"{row['Firstname']} {row['Lastname']}"
        print(f"\nGrades for student {student_name}:")
        table = [[column, grade] for column, grade in row.items() if pd.notna(grade) and column not in ['Firstname', 'Lastname', 'Academic Year', 'Curriculum', 'Place of Birth', 'Telephone', 'Address', 'Gender', 'Email', 'Campus', 'Date of Birth', 'Matricule']]
        print(tabulate(table, headers=["Course", "Grade"], tablefmt="pretty"))

        export_choice = input(f"Do you want to export these statistics for {student_name}? (YES/NO): ").upper()

        while export_choice not in ["YES", "NO"] :
            print("Please enter a valid response (YES or NO).")
            export_choice = input(f"Do you want to export these statistics for {student_name}? (YES/NO): ").upper()

        if export_choice == 'YES':
            student_data_dict[student_name] = row # Store data for each student in the dictionary

    if student_data_dict:
        export_student_grades(student_data_dict)

def export_student_grades(student_data_dict) :
    file_name = input("Enter the Excel file name (without extension): ") + '.xlsx'
    export_path = file_name


    while os.path.exists(export_path): # Verify if the file already exists
        overwrite = input("File already exists. Do you want to overwrite it? (YES/NO) ").upper()
        if overwrite == "YES":
          break
        else :
            new_file_name = input("Enter a new Excel file name (without extension): ") + '.xlsx'
            export_path = new_file_name


    with pd.ExcelWriter(export_path, engine='xlsxwriter') as writer: # Create a pandas excel writer using xlsxwriter as the engine
        for student_name, student_data in student_data_dict.items(): #  Iterate through the dictionary and write each student's data to a separate sheet
            columns_to_remove = ['Firstname', 'Lastname', 'Academic Year', 'Curriculum', 'Place of Birth', 'Telephone', 'Address', 'Gender', 'Email', 'Campus', 'Date of Birth', 'Matricule']
            export_df = pd.DataFrame([student_data], columns=student_data.index).drop(columns=columns_to_remove)

            # Melt the DataFrame to have data in columns with courses and grades
            export_df_melted = pd.melt(export_df, id_vars=[], value_vars=export_df.columns, var_name='Course', value_name='Grade')

            # Write each student's data to a separate sheet
            export_df_melted.to_excel(writer, sheet_name=student_name, index=False)

    print(f"Data exported to {export_path}.")


# COURSE_GRADES
def course_grades(data):
    course_dict = {}
    print("Here is the list of courses:")
    for i, course in enumerate(data.columns[12:], 1):
        course_dict[i] = course
        print(f"{i}. {course}")

    while True:
        try:
            choice = int(input("Enter the number of the course you want to display grades for: "))
            selected_course = course_dict.get(choice)
            if selected_course is not None:
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a valid number.")

    if selected_course in data.columns:
        students_in_course = data[data[selected_course].notnull()]

        if not students_in_course.empty:

            students_in_course = students_in_course.sort_values(by=['Firstname', 'Lastname', selected_course])

            display_course_grades(students_in_course, selected_course, data)
            export_course_grades(students_in_course, selected_course)
        else:
            print(f"No students participated in the course {selected_course}.")
    else:
        print(f"The specified course ({selected_course}) was not found.")
        return

def display_course_grades(students_in_course, course_name, data):
    print(f"\nGrades of students for the course {course_name} (sorted):")
    table = [["Firstname", "Lastname", "Matricule", "Grade"],
             *[[row['Firstname'], row['Lastname'], row['Matricule'], row[course_name]] for _, row in students_in_course.iterrows() if not pd.isnull(row[course_name])]
    ]
    print(tabulate(table, headers="firstrow", tablefmt="pretty"))

def export_course_grades(students_in_course, course_name):
    export_choice = input("Do you want to export these statistics? (YES/NO): ").upper()

    while export_choice not in ["YES", "NO"]:
        print("Please enter a valid response (YES or NO).")
        export_choice = input("Do you want to export these statistics? (YES/NO): ").upper()

    if export_choice == 'YES':
        file_name = input("Enter the Excel file name (without extension): ") + '.xlsx'
        export_path = file_name

        while os.path.exists(export_path):
            overwrite = input("File already exists. Do you want to overwrite it? (YES/NO) ").upper()
            if overwrite == "YES":
               break
            else :
              new_file_name = input("Enter a new Excel file name (without extension): ") + '.xlsx'
              export_path = new_file_name

        export_df = students_in_course[['Firstname', 'Lastname', 'Matricule', course_name]] # export the data
        export_df.to_excel(export_path, index=False)
        print(f"Data exported to {export_path}.")


def action(data): # This is the menu (called everytime to do smth on the app)
    menu_options = [
        ["1", "Register a student"],
        ["2", "Modify one or more fields"],
        ["3", "Delete a student"],
        ["4", "Find a student"],
        ["5", "Show"],
        ["6", "Sort, display, or export the list"],
        ["7", "View statistics"],
        ["8", "To stop the program"]
        ]

    print("What do you want to do?\nBelow, you will find what is possible followed by the commands to type:")
    print(tabulate(menu_options, headers=["Option", "Description"], tablefmt="pretty", colalign=("center", "left")))

    while True:
        command = input("Enter the number of what you want to do: ")  # Check if the command is an integer
        if command.isdigit():  # Convert the command to an integer
            command_int = int(command)  # Check if the command is between 1 and 8
            if 1 <= command_int <= 8:
                print("The command is valid.")
                break  # Exit the loop if the command is valid
            else:
                print("The command must be one of those proposed.")

    if command == "1":
        register_student(data)
    elif command == "2":
        modify(data)
    elif command == "3":
        delete(data)
    elif command == "4":
        find_student(data)
    elif command == "5":
        filter_students(data)
    elif command == "6":
        sort(data)
    elif command == "7":
        statistics_analysis(data)
    elif command == "8":
        return False

menu = []

while True:
    data = reload_data(file_path)
    response = action(data)
    if response is False:
        break
    else:
        if response: # Reload the menu if the file was modified
            menu = []
        else:
            menu.append(response)