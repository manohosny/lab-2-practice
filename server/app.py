from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        gender = request.form.get('gender')
        country = request.form.get('country')
        
        if not all([name, email, gender, country]):
            return render_template('index.html', error="All fields are required!")
        
        user = {
            'name': name,
            'email': email,
            'gender': gender,
            'country': country
        }
        users.append(user)
        
        return redirect(url_for('users_list'))
    
    return render_template('register.html')

@app.route('/users')
def users_list():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)