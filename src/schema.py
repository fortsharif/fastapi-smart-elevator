from pydantic import BaseModel


class ElevatorConfig(BaseModel):
    elevator_id: str
    floors: list[int]
