import csv
import os
from datetime import datetime

count : int = 0

def get_mood(message):
    if message == "happy":
        return ":)"
    elif message == "sad":
        return ":( "
    else:
        return ":|"

class JournalEntry:
    def __init__(self,  message:str, mood:str, timestamp:str):
        self.id = count+1
        self.message = message
        self.mood = mood
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "mood": self.mood,
            "timestamp": self.timestamp
        }

def init_csv():
    if os.path.exists("data.csv"):
        return
    with open("data.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "message", "mood", "timestamp"])
        writer.writeheader()

def handle_write_entry():
    message : str = input("Write your journal message: How do you feel today? (happy/sad/neutral)")
    while message not in ["happy", "sad", "neutral"]:
        message: str = input("Write your journal message: How do you feel today? (happy/sad/neutral)")
    entry = JournalEntry(message, get_mood(message), datetime.now().strftime("%Y-%m-%d %H:%M"))
    with open("data.csv", "a" ) as f:
        writer = csv.DictWriter(f, fieldnames=entry.to_dict().keys())
        writer.writerow(entry.to_dict())
    print("Your message has been saved!")

def handle_view_entries():
    with open("data.csv", "r" ) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def handle_exit(name):
    print(f"Goodbye {name} 👋")
    exit()

def main():
    init_csv()
    print("Welcome to the Secret Journal!")
    name : str = input("Enter your name:")
    print(f"Hello {name} 👋 Let's start journaling!")

    print("What would you like  to  do? \n1. Write a new journal entry \n2. View saved entries \n3. Exit")
    choice : int = int(input("Enter your choice: "))
    count : int = 0

    while choice != 3:
        if choice == 1:
            handle_write_entry()
        elif choice == 2:
            handle_view_entries()
        elif choice == 3:
            handle_exit(name)
        else:
            print("Invalid choice")

        print("What would you like  to  do? \n1. Write a new journal entry \n2. View saved entries \n3. Exit")
        choice = int(input("Enter your choice: "))

if __name__ == "__main__":
    main()