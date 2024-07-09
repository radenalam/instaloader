import instaloader
import csv
import os

# Initialize Instaloader
L = instaloader.Instaloader()

# Define session file
session_file = 'insta_session'

# Load session if it exists, otherwise login and save session
if os.path.exists(session_file):
    L.load_session_from_file('jajanmoeloek', session_file)
    print("Sudah Login, load session")
else:
    L.login('jajanmoeloek', 'Popokbasah21')
    L.save_session_to_file(session_file)
    print("Logged in and session saved")


shortcode = input(str("Masukkan shortcode: "))
post = instaloader.Post.from_shortcode(L.context, shortcode)

for comment in post.get_comments():
    print(f"Owner: {comment.owner.username}")
    print(f"Text: {comment.text}")
    print(f"Likes: {comment.likes_count}")
    print("Answers:")
    for answer in comment.answers:
        print(f"  {answer.owner.username}: {answer.text}")
    print("----------")
