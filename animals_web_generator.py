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

def write_new_html_page(new_html_page, file_path):
    """ writes a html file """
    with open(file_path, "w") as handle:
        return handle.write(new_html_page)


def main():
    animals_data = load_data('animals_data.json')
    html_page = read_html('animals_template.html')
    output = create_animal_string(animals_data)
    new_html_page = html_page.replace('__REPLACE_ANIMALS_INFO__', output)
    write_new_html_page(new_html_page, 'animals.html')


if __name__ == '__main__':
    main()
