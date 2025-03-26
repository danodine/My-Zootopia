import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html(file_path):
    """ Loads a html file """
    with open(file_path, "r") as handle:
        return handle.read()


def create_animal_string(animals_data):
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">'
        output += '<div class ="card__title">'
        output += f"{animal['name']}\n"
        output += '</div>'
        output += '<p class ="card__text">'
        output += '<ul>'
        output += f"<li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>\n"
        for location in animal['locations']:
            output += f"<li><strong>Location:</strong> {location}</li>\n"
        if 'type' in animal['characteristics']:
            output += f"<li><strong>Type:</strong> {animal['characteristics']['type']}</li>\n"
        output += '</ul>'
        output += '</p>'
        output += '</li>'
    return output


def filter_animals(animals_data, animal_skin_type):
    filtered_animals = [item for item in animals_data if item.get("characteristics", {}).get("skin_type").strip().lower() == animal_skin_type]
    output = create_animal_string(filtered_animals)
    return output


def write_new_html_page(new_html_page, file_path):
    """ writes a html file """
    with open(file_path, "w") as handle:
        return handle.write(new_html_page)


def get_animals_skin(animals_data):
    skin_types = []
    print('the skin types are:')
    for animal in animals_data:
        if 'skin_type' in animal['characteristics']:
            if animal['characteristics']['skin_type'].strip().lower() not in skin_types:
                skin_types.append(animal['characteristics']['skin_type'].strip().lower())
                print(animal['characteristics']['skin_type'])
    while True:
        user_selection = input('By what skin type wold you like to filter: ')
        if user_selection in skin_types:
            return user_selection
        else:
            print('you must enter a valid skin type')


def main():
    animals_data = load_data('animals_data.json')
    input_valid = False
    animal_skin_type = ''
    while not input_valid:
        new_game =  input('Do you want to filter by skin type Y/N: ').strip().lower()
        if new_game == 'y':
            animal_skin_type = get_animals_skin(animals_data)
            input_valid = True
        elif new_game == 'n':
            input_valid = True
        else:
            print("Invalid input. Please enter Y or N.")
    html_page = read_html('animals_template.html')
    if animal_skin_type != '':
        output = filter_animals(animals_data, animal_skin_type)
    else:
        output = create_animal_string(animals_data)
    new_html_page = html_page.replace('__REPLACE_ANIMALS_INFO__', output)
    write_new_html_page(new_html_page, 'animals.html')


if __name__ == '__main__':
    main()
