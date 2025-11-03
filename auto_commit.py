import os

commit_message = input("Enter your commit message: ")

os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git branch -M main")
os.system("git push -u origin main")

print("✅ Git push completed successfully!")
