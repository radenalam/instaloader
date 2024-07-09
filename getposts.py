import instaloader
import csv
import re
import os
import time

# Initialize Instaloader
L = instaloader.Instaloader()

# Define session file
session_file = 'insta_session'

username = input(str("Masukkan username: "))
password = input(str("Masukkan password: "))

# Load session if it exists, otherwise login and save session
if os.path.exists(session_file):
    L.load_session_from_file(username, session_file)
    print("Sudah Login, load session")
else:
    L.login(username, password)
    L.save_session_to_file(session_file)
    print("Logged in and session saved")


target = input(str("Ketik username target: "))
# Get the profile
profile = instaloader.Profile.from_username(L.context, target)

# Initialize a list to store post data
posts_data = []

# Retrieve the latest 500 posts
count = 0
for post in profile.get_posts():
    if count == 2:
        break
    # Clean the caption by removing unwanted characters and newlines
    cleaned_caption = re.sub(r'\s+', ' ', post.caption.replace('â£', ' '))
    # Append shortcode, cleaned caption, and number of likes
    posts_data.append([post.shortcode, cleaned_caption, post.likes])
    count += 1
    # Print progress
    print(f"Retrieved post {count} with shortcode {post.shortcode}")
    # Add delay to avoid detection
    time.sleep(2)  # Adjust the delay time as needed

# Write data to CSV
with open(f'data_{target}.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Shortcode', 'Caption', 'Likes'])
    # Write the rows
    writer.writerows(posts_data)

print(f'data_{target}.csv has been written')