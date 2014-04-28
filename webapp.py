import board
import ai

from flask import Flask, render_template
  
app = Flask(__name__)
  
@app.route('/')
def pick():
  	return render_template('pick.html')

@app.route('/pvp/')
def pvp_start():
	return pvp("")

@app.route('/pvp/<moves>')
def pvp(moves):
	brd = board.Board(moves)
  	return render(brd)

@app.route('/ai/<moves>')
def ai_route(moves):
	if moves == 'o':
		brd = board.Board('5')
	elif moves == 'x':
		brd = board.Board('')
	else:
		player = board.Board(moves)
		if player.who_won()!=None:
			brd = player
		else:
			res = ai.evaluate(player)
			brd = player.make_move(res[2])
	return render(brd)
  	

def render(brd):
 	won = brd.who_won()
 	turn = brd.whose_turn()
 	message="Your Turn!"
 	if won==-1:
 		message="Os won!"
 	elif won==1:
 		message="Xs won!"
 	elif won==0:
 		message="Draw!"
 	else:
 		if turn==-1:
 			message="Os, your turn."
 		else:
 			message="Xs, your turn."

 	return render_template('board.html', board=brd.display(), message=message)
  
if __name__ == '__main__':
  	app.run(debug=True)