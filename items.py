import requests

def get_items_dict(url="https://raw.githubusercontent.com/Wesmania/dspbp/master/data/en/items.txt"):
    # The dictionary to store item IDs and names
    items_dict = {}
    try:
        # Attempt to open the file if it has already been downloaded
        with open("items.txt", "r") as file:
            content = file.readlines()
    except FileNotFoundError:
        # If the file does not exist, download it
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text.split('\n')
            # Save the downloaded content for future use
            with open("items.txt", "w") as file:
                file.write(response.text)
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")
            return {}
    
    # Process the content to fill the dictionary
    for line in content:
        if line.strip():  # Ensure the line is not empty
            parts = line.split('  ')  # Split by double space
            item_id = parts[0].strip()
            item_name = parts[1].strip() if len(parts) > 1 else None
            if item_name:  # Ensure there is an item name
                items_dict[item_id] = item_name
    
    return items_dict

if __name__ == "__main__":
    items_dict = get_items_dict()
    print(items_dict)
