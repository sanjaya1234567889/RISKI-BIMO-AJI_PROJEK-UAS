from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rahasia'  # untuk session

# Data login dummy
USER_CREDENTIALS = {
    'admin': 'admin'
}

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        session['user'] = username
        return redirect(url_for('dashboard'))
    return "Login gagal! <a href='/'>Coba lagi</a>"

@app.route("/dashboard")
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template("dashboard.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    if 'user' not in session:
        return redirect(url_for('index'))
    if request.method == "POST":
        nama = request.form["nama"]
        jumlah = request.form["jumlah"]
        print(f"Data disimpan: {nama}, jumlah: {jumlah}")
        return render_template("success.html")
    return render_template("create.html")

@app.route("/logout")
def logout():
    session.pop('user', None)
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)