import os

# 👇 Change this to the folder you want to push
folder_path = r"C:\Users\black\OneDrive\Desktop\AI ML\DSA With Pyhton"

# 👇 Your GitHub repo URL
repo_url = "https://github.com/shaikmaviya/LearnAI-and-Ml-StepbyStep.git"

# 👇 Your commit message
commit_message = "Added new AI project files"

# Go to the target folder
os.chdir(folder_path)

# Run Git commands
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git branch -M main")
os.system("git push -u origin main")

print("✅ Folder pushed to GitHub successfully!")
