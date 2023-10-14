

continent_name = str('south_america')
continent_name = continent_name.replace("_", " ")
print(continent_name)
continent_name_upper = continent_name.title()
print(continent_name_upper)
print('*********')
continent_name = continent_name.replace(" ", "_")
print(continent_name)
image_path = f'./img/pie_{continent_name}.png'
print(image_path)