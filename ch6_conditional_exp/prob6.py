"""Write a program to find out whether a given post is talking about “Harry” or not."""

post = input("Enter the post: ")

if "Harrry".lower() in post.lower():
    print("Harry is detected in the post")
else:
    print("Harry is not detected in the post")
