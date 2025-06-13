import json
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any

class User:
    def __init__(self, user_dict: Dict[str, Any]):
        self.user_id = user_dict.get("user_id")
        self.first_name = user_dict.get("first_name", "")
        self.last_name = user_dict.get("last_name", "")
        self.created_at = user_dict.get("created_at")
        self.persona = user_dict.get("persona")
        self.view = user_dict.get("view")
        self.step = user_dict.get("step")
        self.step_in_progress = user_dict.get("step_in_progress")
        self.first_sober_date = user_dict.get("first_sober_date")
        self.openness_level = user_dict.get("openness_level", None)
        self.last_updated = user_dict.get("last_updated", None)
        # Add other fields as needed

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at,
            "persona": self.persona,
            "view": self.view,
            "step": self.step,
            "step_in_progress": self.step_in_progress,
            "first_sober_date": self.first_sober_date,
            "openness_level": self.openness_level,
            "last_updated": self.last_updated,
        }

def load_users(users_path: Path) -> List[User]:
    if users_path.exists():
        with open(users_path, "r") as f:
            users_data = json.load(f)
        return [User(u) for u in users_data]
    return []

def get_user_by_id(user_id: str, users: List[User]) -> Optional[User]:
    for user in users:
        if user.user_id == user_id:
            return user
    return None

def get_next_user_id(users: List[User]) -> str:
    if not users:
        return "00001"
    max_id = max(int(u.user_id) for u in users if u.user_id and u.user_id.isdigit())
    return f"{max_id + 1:05d}"

def save_users(users: List[User], users_path: Path):
    with open(users_path, "w") as f:
        json.dump([u.to_dict() for u in users], f, indent=2)

def add_user(user_data: Dict[str, Any], users_path: Path) -> User:
    users = load_users(users_path)
    user_id = get_next_user_id(users)
    user_data["user_id"] = user_id
    user_data["created_at"] = datetime.now().isoformat()
    user = User(user_data)
    users.append(user)
    save_users(users, users_path)
    return user

def update_user(user_id: str, updates: Dict[str, Any], users_path: Path) -> Optional[User]:
    users = load_users(users_path)
    user = get_user_by_id(user_id, users)
    if not user:
        return None
    for k, v in updates.items():
        setattr(user, k, v)
    user.last_updated = datetime.now().isoformat()
    save_users(users, users_path)
    return user