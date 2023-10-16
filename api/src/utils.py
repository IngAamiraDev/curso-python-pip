import os

def delete_images_in_directory(directory_path):
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(".png"):
                file_path = os.path.join(directory_path, filename)
                os.remove(file_path)
                print(f"Eliminada la imagen: {filename}")
    except Exception as e:
        print(f"Error al eliminar imágenes: {str(e)}")

def get_population(country_dict):
    labels = []
    values = []
    for label, value in country_dict.items():
        if 'Population' in label:
            year = label.split(' ')[0]            
            if year.isdigit():
                population_value = int(value)
                labels.append(year)
                values.append(population_value)
    return labels, values

def population_by_country(data, country):
    result = data[data['Country'] == country]
    return result