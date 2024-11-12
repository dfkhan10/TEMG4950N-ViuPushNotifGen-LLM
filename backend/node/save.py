import csv
import os

def save_to_csv(data, filename):
    header = ['English', 'Eng_Title', 'Eng_Body', 'Malay', 'Malay_Title', 'Malay_Body']

    file_exists = os.path.exists(filename)
    print(file_exists)

    try:
        with open(filename, mode='a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(header)

            english_data = data['english']
            malay_data = data['malay']

            row = [
                'English',                     # Language
                english_data['title'],         # English Title
                english_data['body'],          # English Body
                'Malay',                       # Language
                malay_data['title'],           # Malay Title
                malay_data['body']             # Malay Body
            ]

            writer.writerow(row)  # Write the data row
            print(f'Successfully saved data to {filename}')
    except Exception as e:
        print(f'Error: {e}')


# Example JSON data
json_data = {
    "english": {
        "title": "KIM Ha Neul's Life Turned Upside Down! 🤯",
        "body": "The queen of romantic comedies is now a murder suspect? 🤔 Don't believe it! Watch Nothing Uncovered to uncover the truth behind the scandal! 💥 #KimHaNeul #NothingUncovered"
    },
    "malay": {
        "title": "Kehidupan KIM Ha Neul Terbalik! 🤯",
        "body": "Ratu komedi romantik kini menjadi suspek pembunuhan? 🚔️ Jangan percayya! Tonton Nothing Uncovered untuk mengungkapkan kebenaran di sebalik skandal! 💥 #KimHaNeul #NothingUncovered"
    }
}

# Save the JSON data to CSV
save_to_csv(json_data, 'utils\history.csv')