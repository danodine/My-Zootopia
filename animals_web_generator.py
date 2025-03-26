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
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['characteristics']['diet']}\n"
        for location in animal['locations']:
            output += f"Location: {location}\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n"
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
    write_new_html_page(new_html_page, 'animals_template.html')


if __name__ == '__main__':
    main()
