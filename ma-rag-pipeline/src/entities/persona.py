import json
from pathlib import Path
from typing import Optional, List, Dict

PERSONAS_PATH = Path("../../data/personas.json")

class Persona:
    def __init__(
        self,
        persona_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        language_style: Optional[str] = None
    ):
        self.persona_id = persona_id
        self.name = name
        self.description = description
        self.language_style = language_style

    @classmethod
    def from_dict(cls, data: Dict) -> "Persona":
        return cls(
            persona_id=data.get("persona_id"),
            name=data.get("name"),
            description=data.get("description"),
            language_style=data.get("language_style"),
        )

    def to_dict(self) -> Dict:
        return {
            "persona_id": self.persona_id,
            "name": self.name,
            "description": self.description,
            "language_style": self.language_style,
        }

def load_personas(path: Path = PERSONAS_PATH) -> List[Persona]:
    if path.exists():
        with open(path, "r") as f:
            data = json.load(f)
        return [Persona.from_dict(p) for p in data if isinstance(p, dict) and p.get("language_style")]
    return []

def get_persona_by_id(persona_id: str, personas: List[Persona]) -> Optional[Persona]:
    for persona in personas:
        if persona.persona_id == persona_id:
            return persona
    return None

def save_personas(personas: List[Persona], path: Path = PERSONAS_PATH) -> None:
    with open(path, "w") as f:
        json.dump([p.to_dict() for p in personas], f, indent=2)