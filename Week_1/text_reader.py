# necessary imports
import re

# input for dynamic path
path = input("Enter path of the text or log file : ").strip("'\"")

# validation function to check if the give link is of .txt or .log
if re.findall(".log$|.txt$", path):
    with open(path) as f:
        data = f.read().lower()
        start_text = input("Enter start text : ").lower()
        End_text = input("Enter end text : ").lower()
        pattern = fr"{re.escape(start_text)}(.*?)(?={re.escape(End_text)})"
        match = re.search(pattern, data,re.DOTALL) 
        if match:
            # .strip() removes any leading or trailing whitespace/newlines
            extracted_data = match.group(1).strip()
            print(extracted_data)
        else:
            print("Did not find specified pattern in the given context.")
else:
    print("Not a .txt or .log file")