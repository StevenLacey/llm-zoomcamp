import json
from pathlib import Path
from typing import Optional, List, Dict

PERSONAS_PATH = Path("../../data/personas.json")


class Persona:
    def __init__(self, persona_id: str, name: str, description: str, language_style: str):
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


class PersonaManager:
    def __init__(self, personas_path: Path = PERSONAS_PATH):
        self.personas_path = personas_path
        self.personas = self.load_personas()

    def load_personas(self) -> List[Persona]:
        if self.personas_path.exists():
            with open(self.personas_path, "r") as f:
                data = json.load(f)
            return [Persona.from_dict(p) for p in data]
        return []

    def get_persona_by_id(self, persona_id: str) -> Optional[Persona]:
        for persona in self.personas:
            if persona.persona_id == persona_id:
                return persona
        return None

    def list_personas(self) -> List[Persona]:
        return self.personas

    def add_persona(self, persona: Persona) -> None:
        if self.get_persona_by_id(persona.persona_id):
            raise ValueError(f"Persona with id '{persona.persona_id}' already exists.")
        self.personas.append(persona)
        self.save_personas()

    def save_personas(self) -> None:
        with open(self.personas_path, "w") as f:
            json.dump([p.to_dict() for p in self.personas], f, indent=2)

    def remove_persona(self, persona_id: str) -> None:
        self.personas = [p for p in self.personas if p.persona_id != persona_id]
        self.save_personas()


# Example usage:
if __name__ == "__main__":
    manager = PersonaManager()
    # List all personas
    for persona in manager.list_personas():
        print(f"{persona.persona_id}: {persona.name} - {persona.description}")

    # Get a specific persona
    persona = manager.get_persona_by_id("spiritual_explorer")
    if persona:
        print(f"\nFound persona: {persona.name} ({persona.persona_id})")
        print(f"Description: {persona.description}")
        print(f"Language Style: {persona.language_style}")