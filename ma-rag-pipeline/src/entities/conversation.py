from pathlib import Path
from typing import List, Dict, Optional, Any
import json
from datetime import datetime
import uuid

CONVERSATIONS_PATH = Path("../../data/conversations.json")

class Conversation:
    def __init__(
        self,
        conversation_id: Optional[str] = None,
        user_id: Optional[str] = None,
        date: Optional[str] = None,
        timestamp: Optional[str] = None,
        step_content: Optional[str] = None,
        persona_used: Optional[str] = None,
        conversation_type: Optional[str] = None,
        user_name: Optional[str] = None,
        spiritual_view: Optional[str] = None,
        openness_level: Optional[str] = None,
        emotional_tone_start: Optional[str] = None,
        emotional_tone_end: Optional[str] = None,
        total_messages: Optional[int] = None,
        duration_minutes: Optional[int] = None,
        key_insights: Optional[List[str]] = None,
        action_items: Optional[List[str]] = None,
        ready_for_steps: Optional[bool] = None,
        follow_up_suggested: Optional[bool] = None,
        rag_sources_used: Optional[List[Any]] = None,
        conversation_data: Optional[Dict[str, Any]] = None,
    ):
        self.conversation_id = conversation_id or str(uuid.uuid4())[:8]
        self.user_id = user_id
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        self.timestamp = timestamp or datetime.now().isoformat()
        self.step_content = step_content
        self.persona_used = persona_used
        self.conversation_type = conversation_type
        self.user_name = user_name
        self.spiritual_view = spiritual_view
        self.openness_level = openness_level
        self.emotional_tone_start = emotional_tone_start
        self.emotional_tone_end = emotional_tone_end
        self.total_messages = total_messages
        self.duration_minutes = duration_minutes
        self.key_insights = key_insights or []
        self.action_items = action_items or []
        self.ready_for_steps = ready_for_steps
        self.follow_up_suggested = follow_up_suggested
        self.rag_sources_used = rag_sources_used or []
        self.conversation_data = conversation_data or {}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Conversation":
        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__

def load_conversations(path: Path = CONVERSATIONS_PATH) -> List[Conversation]:
    if path.exists():
        with open(path, "r") as f:
            data = json.load(f)
        return [Conversation.from_dict(d) for d in data if d]
    return []

def save_conversations(conversations: List[Conversation], path: Path = CONVERSATIONS_PATH):
    with open(path, "w") as f:
        json.dump([c.to_dict() for c in conversations], f, indent=2)

def append_conversation(convo: Conversation, path: Path = CONVERSATIONS_PATH):
    conversations = load_conversations(path)
    conversations.append(convo)
    save_conversations(conversations, path)

def get_conversations_by_user(user_id: str, path: Path = CONVERSATIONS_PATH) -> List[Conversation]:
    conversations = load_conversations(path)
    return [c for c in conversations if c.user_id == user_id]

def get_recent_conversations(user_id: str, n: int = 3, path: Path = CONVERSATIONS_PATH) -> List[Conversation]:
    user_convos = get_conversations_by_user(user_id, path)
    user_convos = sorted(user_convos, key=lambda c: c.timestamp, reverse=True)
    return user_convos[:n]

# Example usage:
if __name__ == "__main__":
    # Load all conversations
    convos = load_conversations()
    print(f"Loaded {len(convos)} conversations.")

    # Create and append a new conversation
    new_convo = Conversation(user_id="00001", conversation_type="initial_meeting", user_name="Test User")
    append_conversation(new_convo)
    print("Appended new conversation.")