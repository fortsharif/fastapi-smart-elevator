from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

import src.cache as cache
from src.schema import ElevatorConfig
from src.service import find_closest_elevator, create_elevators


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return "smart elevator app"


elevator_router = APIRouter(
    prefix="/elevator",
    tags=["elevator"],
)


@elevator_router.get("/status/{elevator_id}")
def get_elevator_status(elevator_id: str):
    return {
        "elevator_id": elevator_id,
        "floor": cache.get_elevator(elevator_id)[1],
        "direction": cache.get_elevator(elevator_id)[0],
    }


@elevator_router.get("/")
def get_all_elevators():
    return [
        {
            "elevator_id": elevator,
            "floor": elevator_info[1],
            "direction": elevator_info[0],
        }
        for elevator, elevator_info in cache.elevators.items()
    ]


@elevator_router.post("/configure")
def configure_elevators(elevator_config: list[ElevatorConfig]):
    return (
        {"status": "success", "message": "Successfully configurated"}
        if create_elevators(elevator_config)
        else {"status": "error", "message": "Configuration failed"}
    )


floor_router = APIRouter(
    prefix="/floor",
    tags=["floor"],
)


@floor_router.get("/")
def get_elevator_to_take(from_floor: int, to_floor: int):
    elevator = find_closest_elevator(from_floor, to_floor)

    return {"elevator_id": elevator, "direction": cache.elevators[elevator][0]}


app.include_router(elevator_router, prefix="/api")
app.include_router(floor_router, prefix="/api")
