file_name = 'Q23.jpg'

index = file_name.find('.')
renamed_file = file_name[:index] + '01' + file_name[index:]
renamed_file = renamed_file.replace('Q', '')

print(renamed_file)
