from flask import Flask,render_template,request,url_for,redirect
from utils.database import Database
from utils.files_finder import FilesFinder

app=Flask(__name__)
app.config['SECRET_KEY']="f26a3f21e2994f87d39c12c777c4338c"

surnames={"Surname" : ""}
login_id={"id" : ""}

@app.route('/', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        name = request.form.get("Uname")
        password = request.form.get("Pass")
        if name=="user" and password=="1234":
            login_id["id"]=True
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/home')
def home():
    if login_id["id"]==True:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if login_id["id"]==True:
        login_id["id"] = False
        return render_template('logout.html',message="GOODBYE")
    else:
        return redirect(url_for('login'))



@app.route('/table', methods=["GET","POST"])
def show_patients():
    if login_id["id"] == True:
        patients=Database.show_all()
        return render_template('table.html',data=patients)
    else:
        return redirect(url_for('login'))



@app.route('/link', methods=["GET","POST"])
def add_patient():
    if request.method == 'POST' and request.form['action'] == 'add patient':
        surname = request.form.get('Surname')
        name = request.form.get('Name')
        age = request.form.get('Age')
        telephone = request.form.get('Telephone')
        address = request.form.get('Address')
        cause = request.form.get('Cause')
        date = request.form.get('Date')
        summary = request.form.get('Summary')
        Database.insert(surname,name,age,telephone,address,cause,date,summary)
        return redirect(url_for('show_patients'))
    return redirect(url_for('home'))


@app.route('/search', methods=["GET","POST"])
def search_by_surname():
    if request.method == 'POST' and request.form['action'] == 'search patient':
        surname = request.form.get('Surname')
        surnames["Surname"]=surname
        patients,items=Database.search(surname)
        return render_template('items.html',data=patients,items=items)
    return redirect(url_for('home'))


@app.route('/find', methods=["GET","POST"])
def find_files():
    if request.method == 'POST':
        surname = surnames["Surname"]
        patients, items = Database.search(surname)
        file = FilesFinder(surname)
        file.make_dir()
        try:
            file.search_files()
        except FileNotFoundError:
            return render_template('items.html', data=patients, items=items,message="files not found")
        else:
            return render_template('items.html', data=patients, items=items,message="files downloaded successfully")
    return redirect(url_for('home'))



@app.route('/delete', methods=["GET","POST"])
def delete_patient():
    if request.method == 'POST' and request.form['action'] == 'delete patient':
        surname = request.form.get('Surname')
        Database.delete(surname)
        return redirect(url_for('show_patients'))
    return redirect(url_for('home'))


if __name__=='__main__':
    Database.database_exists()
    app.run(debug=True)


