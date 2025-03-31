import json


def load_data(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict or list: Parsed JSON data.
    """
    with open(file_path, "r", encoding='utf-8') as handle:
        return json.load(handle)


def read_html(file_path):
    """
    Read the contents of an HTML file.

    Args:
        file_path (str): Path to the HTML file.

    Returns:
        str: Contents of the HTML file.
    """
    with open(file_path, "r", encoding='utf-8') as handle:
        return handle.read()


def create_animal_string(animals_data):
    """
    Create an HTML string representation for a list of animals.

    Args:
        animals_data (list): List of animal dictionaries.

    Returns:
        str: HTML formatted string of animal data.
    """
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">'
        output += '<div class="card__title">'
        output += f"{animal['name']}\n"
        output += '</div>'
        output += '<p class="card__text">'
        output += '<ul>'
        output += f"<li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>\n"
        len_animal_locations = len(animal['locations'])
        location_str = ''
        for key, location in enumerate(animal['locations']):
            print(len_animal_locations)
            if len_animal_locations > 1:
                if key == len_animal_locations-2:
                    location_str += f"{location} and "
                elif key == key == len_animal_locations-1:
                    location_str += f"{location}"
                else:
                    location_str += f"{location}, "
            else:
                location_str += f"{location}"
        output += f"<li><strong>Location:</strong> {location_str}</li>\n"
        if 'type' in animal['characteristics']:
            output += f"<li><strong>Type:</strong> {animal['characteristics']['type']}</li>\n"
        output += '</ul>'
        output += '</p>'
        output += '</li>'
    return output


def filter_animals(animals_data, animal_skin_type):
    """
    Filter animals by skin type.

    Args:
        animals_data (list): List of animal dictionaries.
        animal_skin_type (str): Skin type to filter by.

    Returns:
        str: HTML string of filtered animals.
    """
    filtered_animals = [
        item for item in animals_data
        if item.get("characteristics", {}).get("skin_type", "").strip().lower() == animal_skin_type
    ]
    return create_animal_string(filtered_animals)


def write_new_html_page(new_html_page, file_path):
    """
    Write a string to an HTML file.

    Args:
        new_html_page (str): HTML content to write.
        file_path (str): Path to the output file.

    Returns:
        int: Number of characters written.
    """
    with open(file_path, "w", encoding='utf-8') as handle:
        return handle.write(new_html_page)


def get_animals_skin(animals_data):
    """
    Prompt user to select a skin type from available animal data.

    Args:
        animals_data (list): List of animal dictionaries.

    Returns:
        str: User-selected skin type.
    """
    skin_types = []
    print('The skin types are:')
    for animal in animals_data:
        skin_type = animal['characteristics'].get('skin_type', '').strip().lower()
        if skin_type and skin_type not in skin_types:
            skin_types.append(skin_type)
            print(skin_type.capitalize())

    while True:
        user_selection = input('By what skin type would you like to filter: ').strip().lower()
        if user_selection in skin_types:
            return user_selection
        print('You must enter a valid skin type.')


def main():
    """
    Main function to run the animal HTML page generator.
    """
    animals_data = load_data('animals_data.json')
    input_valid = False
    animal_skin_type = ''

    while not input_valid:
        new_game = input('Do you want to filter by skin type Y/N: ').strip().lower()
        if new_game == 'y':
            animal_skin_type = get_animals_skin(animals_data)
            input_valid = True
        elif new_game == 'n':
            input_valid = True
        else:
            print("Invalid input. Please enter Y or N.")

    html_page = read_html('animals_template.html')

    if animal_skin_type:
        output = filter_animals(animals_data, animal_skin_type)
    else:
        output = create_animal_string(animals_data)

    new_html_page = html_page.replace('__REPLACE_ANIMALS_INFO__', output)
    write_new_html_page(new_html_page, 'animals.html')


if __name__ == '__main__':
    main()
