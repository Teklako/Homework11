import requests
import json
import sqlite3
response = requests.get("https://alexwohlbruck.github.io/cat-facts/")

if response.status_code == 200:
    print("Request successful!")
else:
    print("Request failed with status code:", response.status_code)

data = response.json()

for cat in data:
    print(f"Title: {cat['title']}")
    print(f"Completed: {cat['completed']}")
    print()

conn = sqlite3.connect("cat.db")

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS todos (title text, completed integer)")

for cat in data:
    title = cat["title"]
    completed = int(cat["completed"])
    c.execute("INSERT INTO cat(title, completed) VALUES (?, ?)", (title, completed))

conn.commit()
conn.close()