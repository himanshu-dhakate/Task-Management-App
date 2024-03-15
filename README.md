## Steps to run the project
- Create a virtual environment in python
- Install the requirements
```sh
pip install -r requirements.txt
```
- Install sqlite3 db (Optional)
- Inside the folder todo_project run server
```sh
python manage.py runserver
```
- You will notice that db.sqlite3 file is created.
- Migrate the models into the database.
```sh
python manage.py makemigrations
python manage.py migrate
```
- Run server again
```sh
python manage.py runserver
```
- Go to the URL specified in the terminal. It will be something like `127.0.0.1:port_number`
**Note- Use a strong password for the user**
