# Cupcake REST & JSON APIs

## App Creation Notes

I set up the project by following these steps:

1. `pip install -r requirements.txt`

2. to create a virtual environment named `venv` you can run this command:
`python3 -m venv venv`

3. There is a virtual environment already set up for this project so you need to activate it:

`source venv/bin/activate`

4. In `Flask`, the `FLASK_APP` environment variable is used to specify how to load the application which can be set to a python file, a module, or a package. In this case, it's being set to the `app.py` file which is where my `Flask` application is defined. When you execute the command `flask run`, `Flask` uses the value of `FLASK_APP` to find my application and run it. If `FLASK_APP` is not set, `Flask` won't know where the application is and won't be able to run it. So before you run the application you must run the command:

`export FLASK_APP=app.py`

5. Now you can run the application with the debugger module activated using the command:

`flask run --debugger`

### configuring `.env` and `.gitignore`

I created these files and added `.env` to the `.gitignore` file.  Then I created a `DATABASE_URL` variable and a `DEBUG_SECRET_KEY` variable so I could hide my `psql` username and password.  I also added the "cupcakes" database name to the end of the URL so the syntax is: `DATABASE_URL=postgresql://myUsername:myPassword@localhost/cupcakes`



### psql and the database:

1. Since this is a Unix-based system you must activate the PostgreSQL service with the command:
   NB--> be prepared to enter your `psql` password

`sudo service postgresql start`

2. To log in to your PSQL account you must use the `psql` command with the `-U` option followed by your username:

`psql -U your_username`

3. I created a database called "cupcakes" by running the command below while logged into my PSQL account:

`CREATE DATABASE cupcakes;`

4. Then I ran the file `seed.py` to populate the database by exiting my `psql` terminal ( `ctrl` + `q`) and navigating to the folder that contained `seed.py` in my project directory.  Then I ran the command

### Postman

There is a Postman account associated with this project.

