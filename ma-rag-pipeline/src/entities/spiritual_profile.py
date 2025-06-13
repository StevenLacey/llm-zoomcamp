from pathlib import Path
from typing import List, Dict, Optional, Any
import json
from datetime import datetime

SPIRITUAL_PROFILE_PATH = Path("../../data/spiritual_profile.json")

class SpiritualProfile:
    def __init__(
        self,
        user_id: str,
        current_profile: Dict[str, Any],
        history: Optional[List[Dict[str, Any]]] = None
    ):
        self.user_id = user_id
        self.current_profile = current_profile
        self.history = history or []

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SpiritualProfile":
        return cls(
            user_id=data["user_id"],
            current_profile=data["current_profile"],
            history=data.get("history", [])
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "current_profile": self.current_profile,
            "history": self.history
        }

    def archive_current_profile(self):
        # Archive the current profile to history with timestamp
        archived = self.current_profile.copy()
        archived["archived_at"] = datetime.now().isoformat()
        self.history.append(archived)

    def update_current_profile(self, updates: Dict[str, Any]):
        self.archive_current_profile()
        self.current_profile.update(updates)
        self.current_profile["updated_at"] = datetime.now().isoformat()

def load_spiritual_profiles(path: Path = SPIRITUAL_PROFILE_PATH) -> List[SpiritualProfile]:
    if path.exists():
        with open(path, "r") as f:
            data = json.load(f)
        return [SpiritualProfile.from_dict(d) for d in data if d]
    return []

def save_spiritual_profiles(profiles: List[SpiritualProfile], path: Path = SPIRITUAL_PROFILE_PATH):
    with open(path, "w") as f:
        json.dump([p.to_dict() for p in profiles], f, indent=2)

def get_profile_by_user_id(user_id: str, path: Path = SPIRITUAL_PROFILE_PATH) -> Optional[SpiritualProfile]:
    profiles = load_spiritual_profiles(path)
    for profile in profiles:
        if profile.user_id == user_id:
            return profile
    return None

def update_profile(user_id: str, updates: Dict[str, Any], path: Path = SPIRITUAL_PROFILE_PATH) -> Optional[SpiritualProfile]:
    profiles = load_spiritual_profiles(path)
    for profile in profiles:
        if profile.user_id == user_id:
            profile.update_current_profile(updates)
            save_spiritual_profiles(profiles, path)
            return profile
    return None

def add_spiritual_profile(profile_data: Dict[str, Any], path: Path = SPIRITUAL_PROFILE_PATH) -> SpiritualProfile:
    profiles = load_spiritual_profiles(path)
    profile = SpiritualProfile.from_dict(profile_data)
    profiles.append(profile)
    save_spiritual_profiles(profiles, path)
    return profile

# Example usage:
if __name__ == "__main__":
    # Load all profiles
    profiles = load_spiritual_profiles()
    print(f"Loaded {len(profiles)} spiritual profiles.")

    # Get a profile by user_id
    profile = get_profile_by_user_id("00001")
    if profile:
        print(profile.to_dict())
    else:
        print("Profile not found.")

    # Update a profile
    updated = update_profile("00001", {"openness_level": "medium"})
    if updated:
        print("Profile updated:", updated.to_dict())