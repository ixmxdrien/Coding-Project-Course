import csv

# Déclarer categories en tant que variable globale
categories = []

def read_movie_series_info(file_path):
    catalog = {}
    with open(file_path, 'r', encoding='utf-8') as info_file:
        info_reader = csv.reader(info_file)
        next(info_reader)  # Skip header row
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

def create_category_matrix(catalog, categories):
    # Créez la matrice avec une rangée et une colonne supplémentaires pour les noms de catégories
    category_matrix = [[0 for _ in range(len(categories) + 1)] for _ in range(len(categories) + 1)]

    # Ajoutez les noms de catégories à la première ligne et à la première colonne
    for i in range(len(categories)):
        category_matrix[0][i + 1] = categories[i]  # Ajoutez les noms de catégories à la première ligne
        category_matrix[i + 1][0] = categories[i]  # Ajoutez les noms de catégories à la première colonne
    
    # Remplissez la matrice avec les données
    for show_id, movie_categories in catalog.items():
        for i in range(len(categories)):
            if categories[i] in movie_categories[1]:
                for j in range(len(categories)):
                    if categories[j] in movie_categories[1]:
                        category_matrix[i + 1][j + 1] += 1  # Commencez à remplir à partir de la deuxième ligne et de la deuxième colonne
    # Ajoutez les noms de catégories à la première colonne et les données de la matrice
    return category_matrix


def recommend_movies(user_id, catalog, user_ratings, category_matrix, threshold=0.5):
    global categories  # Déclarer categories en tant que variable globale

    user_id = int(user_id)  # Convertir user_id en entier

    suggestions = {}

    # Créer le dictionnaire pour stocker les indices des catégories
    category_index = {category: i + 1 for i, category in enumerate(categories)}
    print(category_index)

    for show_id, categories in catalog.items():
        # Check if the user has rated the show
        if show_id in user_ratings and user_id in user_ratings[show_id] and user_ratings[show_id][user_id] == 0:
            # Liste des catégories communes entre le film/série et les films/séries notés par l'utilisateur
            common_categories = [category for category in categories[1] if category in catalog[show_id][1]]
            if common_categories:
                # Calculez la similarité entre le film/série et les films/séries notés par l'utilisateur
                similarity = sum(
                    min(category_matrix[category_index[category]][category_index[user_category]] for user_category in common_categories)
                    for category in categories[1]
                )

                # Ne recommandez que des films/séries dont la similarité dépasse le seuil spécifié
                if similarity > threshold:
                    suggestions[show_id] = {'title': catalog[show_id][0], 'similarity': similarity}

    # Triez les suggestions par similarité décroissante
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1]['similarity'], reverse=True)

    return sorted_suggestions[:5]

if __name__ == "__main__":

    # Replace file_path_1 and file_path_2 with the actual file paths
    file_path_1 = "/Users/adrien/vscodeworkspace/coding-project/projet_en_groupe/data_cp_2023/netflix_titles-2.csv"
    file_path_2 = "/Users/adrien/vscodeworkspace/coding-project/projet_en_groupe/data_cp_2023/ratings.csv"

    user_id = input("quel est ton user ? ")

    try:
        user_id = int(user_id)
    except ValueError:
        print("Veuillez entrer un identifiant d'utilisateur valide.")
        exit()

    # Read data from CSV files
    catalog = read_movie_series_info(file_path_1)
    ratings = read_user_ratings(file_path_2)
    # Create category matrix
    categories = list(set(category for _, movie_info in catalog.items() for category in movie_info[1]))
    category_matrix = create_category_matrix(catalog, categories)

    # Display movies already viewed by the user
    """print("Films déjà vus par l'utilisateur:")
    for show_id, user_rating in ratings.items():
        if user_id in user_rating and user_rating[user_id] > 0:
            print(f"- {catalog[show_id][0]}")"""

    # Recommend movies
    recommended_movies = recommend_movies(user_id, catalog, ratings, category_matrix, threshold=0.5)

    # Display top 5 recommendations
    print("\nTop 5 recommandations:")
    for show_id, info in recommended_movies:
        print(f"Title: {info['title']}, Similarity: {info['similarity']}")