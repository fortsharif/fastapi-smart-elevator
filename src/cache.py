elevators = {}


floor_elevators = {floor: [] for floor in range(10)}


def get_elevator(elevator_id: str):
    return elevators.get(elevator_id)


def update_elevator(elevator_id: str, floor: int):
    elevator = elevators.get(elevator_id)
    if elevator:
        direction, _ = elevator
        elevators[elevator_id] = [direction, floor]
        return True
    return False


def get_floor_elevators(floor: int):
    return floor_elevators.get(floor)


def update_floor_elevators(floor: int, elevator_ids: list):
    if floor_elevators.get(floor):
        floor_elevators[floor] = elevator_ids
        return True
    return False


def create_elevator(elevator_id: str, floors: list[int], direction_from_panel: str):
    elevators[elevator_id] = [direction_from_panel, 0]
    if 0 not in floors:
        floor_elevators[0].append(elevator_id)
    for floor in floors:
        floor_elevators[floor].append(elevator_id)
