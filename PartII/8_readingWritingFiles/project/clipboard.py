import sys 
import json 
import pyperclip 

FILE = "clipboard.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
        
    except:
        return {} 

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def main():
    data = load_data()

    if len(sys.argv) < 2:
        print("Usage: save <key> | load <key> | list")

        return 
    
    command = sys.argv[1]

    if command == 'save':
        key = sys.argv[2]
        data[key] = pyperclip.paste()
        save_data(data)
        print(f"Saved under '{key}'")

    elif command == 'load':
        key = sys.argv[2]
        pyperclip.copy(data.get(key, ""))
        print(f"Loaded '{key}' to clipboard")

    elif command == "list":
        print(list(data.keys()))

main()
