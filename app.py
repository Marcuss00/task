from flask import Flask, render_template, request
from cs50 import SQL

db = SQL("sqlite:///tasks.db")

app = Flask (__name__)

# preparing home route 
@app.route('/')
def index () :
    return render_template('index.html')


# working with second route 

@app.route('/success', methods = ["POST"])

def success():
    # getting value of task from form 
    task = request.form.get('task')

    if not task or task.strip()=="" : 
        return 'enter task '; 
# :task is parameter to bind values... like here :task = task_check

    task_check = task; 
    rows = db.execute("SELECT * FROM task WHERE task= :task", task = task_check)  
    
    # checking  for values if any matches..

    if len(rows) > 0 :
        return render_template('failure.html')
    
    else :
        # inserting values into database 

        db.execute("INSERT INTO task (task)VALUES (?)", task)

        return render_template('success.html', tasks = task )