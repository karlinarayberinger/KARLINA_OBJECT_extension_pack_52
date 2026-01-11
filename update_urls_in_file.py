#########################################################################################
# file: update_urls_in_file.py
# type: Python
# date: 10_JANUARY_2026
# author: karbytes
# license: PUBLIC_DOMAIN 
#########################################################################################
'''
---------------------------------------------------------------------------------------------------------------------------
Modify a copy of journal_karbytes_10january2026_p1.txt (which is named temp.txt)
such that each instance of "https://raw.githubusercontent.com/[anonymous_username]/[public_github_repository_name]/main/"
which occurs in temp.txt is changed to "karlinarayberinger/KARLINA_OBJECT_extension_pack_52/".
---------------------------------------------------------------------------------------------------------------------------
'''
def replace_in_file(file_name, old_string, new_string):
    try:
        # Read the content of the file (named thing.html).
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the old string with the new string.
        updated_content = content.replace(old_string, new_string)

        # Write the updated content back to the file (named thing.html).
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Replaced all instances of '{old_string}' with '{new_string}' in {file_name}.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Parameters
file_name = "temp.txt"
old_string = "/informationcrystals/projects/main/"
new_string = "/karlinarayberinger/KARLINA_OBJECT_extension_pack_52/"

# Execute the function
replace_in_file(file_name, old_string, new_string)
