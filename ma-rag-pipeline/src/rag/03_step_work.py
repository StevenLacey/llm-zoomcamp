from pathlib import Path
from src.entities.user import load_users, get_user_by_id  # relative import

users_path = Path("data/users.json")  # Adjust path as needed
print(users_path.resolve())
users = load_users(users_path)
print([u.user_id for u in users])
user = get_user_by_id("00006", users)
print(user.to_dict() if user else "User not found")