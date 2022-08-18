"""Transform data to json and add to a file."""
import json

def add_to_file(data: dict, folder_name: str, file_name: str) -> None:
    """Transform data to json and add it to a .txt file
    Args:
        data (dict): dictionary that contains all fields information
    Returns:
        None
    """
    # Remove .jpg
    file_name = file_name.replace('.jpg','')

    # Transform to json
    output = json.dumps(data)

    # Write json on file
    output_file = open(f'{folder_name}/{file_name}.txt',"w+")
    output_file.write(output)
    output_file.close()

    return