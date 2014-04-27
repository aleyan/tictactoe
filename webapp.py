from flask import Flask, render_template
  
app = Flask(__name__)
  
@app.route('/')
def pick():
  return render_template('pick.html')
  
@app.route('/pvp')
def pvp():
  return render_template('board.html')

@app.route('/aio')
def aio():
  return render_template('board.html')

@app.route('/aix')
def aix():
  return render_template('board.html')  
  
if __name__ == '__main__':
  app.run(debug=True)