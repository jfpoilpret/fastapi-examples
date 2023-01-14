Python FstAPI Example 1
=======================

This first example simply demonstrates a simple REST API with FastAPI, without authentication or persistence.
The purpose is to learn FastAPI step by step.
Finally, this shows how to easily run a server (with Uvicorn) and test it live, with swagger.

TODO
----
- add unit tests: anything FastAPI specific for that?

Preparation
-----------
Prepare a virtual environment for the project sample:

	cd example1
	python3 -m venv .venv
	source .venv/bin/activate
	pip3 install fastapi
    pip3 install pydantic[email]
	pip3 install "uvicorn[standard]"

Also install useful tools during project development:

	pip3 install pytest	# Automated tests library

Develop first example
---------------------
Create a main module (same name as application, why is that mandatory? I don't know):

	mkdir example1
	
Create the main application file `main.py`:

    ...

Now run the server with uvicorn:

	uvicorn main:app --reload

Check doc and execute with swagger:

    http://localhost:8000/docs

Debug with Visual Studio Code
-----------------------------

TODO Open `server.py` file and run Debug "Python: Current File".
