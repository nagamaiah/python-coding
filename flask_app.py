from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_FORM = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask Basic Form</title>
    <style>
      body { font-family: Arial, sans-serif; background: #f9f9f9; }
      .form-container {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        max-width: 400px;
        margin: 30px auto;
      }
      input[type=text], input[type=email] {
        width: 100%;
        padding: 8px;
        margin: 8px 0 16px 0;
        border: 1px solid #ccc;
        border-radius: 4px;
      }
      input[type=submit] {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      input[type=submit]:hover {
        background-color: #45a049;
      }
    </style>
  </head>
  <body>
    <form class="form-container" method="POST">
      <label for="username">Username:</label><br>
      <input type="text" id="username" name="username" required><br>
      <label for="email">Email:</label><br>
      <input type="email" id="email" name="email" required><br>
      <input type="submit" value="Submit">
    </form>
    {% if username and email %}
      <div class="form-container">
        <h4>Submitted!</h4>
        <p>Username: {{ username }}</p>
        <p>Email: {{ email }}</p>
      </div>
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    username = email = None
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
    return render_template_string(HTML_FORM, username=username, email=email)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
