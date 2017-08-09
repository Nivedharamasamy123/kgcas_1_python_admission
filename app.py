from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def start():
   return render_template("start.html")
   
@app.route('/login.html')
def register():
   return render_template("login.html")
   
@app.route('/register.html')
def login():
   return render_template("register.html")  
   
if __name__ == '__main__':
   app.run()
