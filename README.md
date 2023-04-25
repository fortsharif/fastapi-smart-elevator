Requirements
------------

- Python 3.11

Installation
------------

It is recommended to use a virtual environment and install the required packages using the `requirements.txt` file. To do so, run the following commands (bash):

```
python -m venv venv
source venv/Script/activate
pip install -r requirements/base.txt
```

Usage
-----

To run the application, use the following command:

```uvicorn src.main:app --reload``` 
(reload flag will provide automatic reload)

Documentation
-------------

Once application is running you can checkout the fastapi auto-generated docs at http://localhost:8000/docs (or whatever port you are running the application in)