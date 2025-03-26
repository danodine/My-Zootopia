import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def main():
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        print(f"Name: {animal['name']}")
        print(f"Diet: {animal['characteristics']['diet']}")
        for location in animal['locations']:
            print(f"Location: {location}")
        if 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")


if __name__ == '__main__':
    main()