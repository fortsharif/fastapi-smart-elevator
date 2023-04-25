import src.cache as cache


def find_closest_elevator(from_floor: int, to_floor: int):
    closest_elevator = None
    min_distance = float("inf")

    elevators_servicing_from_floor = cache.get_floor_elevators(from_floor)

    if not elevators_servicing_from_floor:
        return

    floors_to_check = {}
    if to_floor > from_floor:
        # Find all floors less than or equal to from floor that are serviced by the same elevators as the to floor
        for elevator_id in elevators_servicing_from_floor:
            if not elevator_services_floor(elevator_id, to_floor):
                continue

            for floor in range(from_floor, -1, -1):
                if elevator_services_floor(elevator_id, floor):
                    floors_to_check[elevator_id] = floor
                    break

    elif to_floor < from_floor:
        # Find all floors greater than or equal to from floor that are serviced by the same elevators as the to floor
        for elevator_id in elevators_servicing_from_floor:
            if not elevator_services_floor(elevator_id, to_floor):
                continue

            for floor in range(from_floor, 10):
                if elevator_services_floor(elevator_id, floor):
                    floors_to_check[elevator_id] = floor
                    break

    # Check each elevator on the floors to see which is the closest to the from floor
    for elevator_id, floor in floors_to_check.items():
        _, current_floor = cache.get_elevator(elevator_id)

        if (
            to_floor > from_floor
            and current_floor <= floor
            and floor - current_floor < min_distance
        ):
            closest_elevator = elevator_id
            min_distance = floor - current_floor
        elif (
            to_floor < from_floor
            and current_floor >= floor
            and current_floor - floor < min_distance
        ):
            closest_elevator = elevator_id
            min_distance = current_floor - floor

    if closest_elevator is not None:
        cache.update_elevator(closest_elevator, to_floor)

    return closest_elevator


def elevator_services_floor(elevator_id: str, floor: int):
    elevators_servicing_floor = cache.get_floor_elevators(floor)
    return elevator_id in elevators_servicing_floor


def create_elevators(elevators):
    for i, elevator in enumerate(elevators):
        direction_from_panel = "left" if i % 2 == 0 else "right"
        cache.create_elevator(
            elevator.elevator_id, elevator.floors, direction_from_panel
        )
    return True
