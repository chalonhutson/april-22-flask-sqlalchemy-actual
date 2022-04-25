#Step 1
## Created virtual environment.
### virtualenv env
#Step 2
## Install dependencies.
### pip install -r requirements.txt
#Step 3
## Connect to database interactive and create tables.
### python -i models.py
### >>> db.create_all()
#Step 4
## Party and have fun!!!