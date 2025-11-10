import os
from datetime import datetime


current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

commit_message = current_time


os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git branch -M main")
os.system("git push -u origin main")



print("✅ Git push completed successfully!")