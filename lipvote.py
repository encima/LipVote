import sqlite3
from bottle import route, run, template, debug, request, redirect, static_file

#Multiple routes can bind to a single function
@route('/lipvote')
def choon_list():
	conn = sqlite3.connect('lipvote.db')
	c = conn.cursor()
	c.execute('SELECT id, choon, artist, votes FROM choons')
	result = c.fetchall()
	c.close()
	output = template('lipvote_index', rows=result)
	print result
	return(output)

@route('/new', method='GET')
def new_item():
    if request.GET.get('save','').strip():
        choon = request.GET.get('choon', '').strip()
        artist = request.GET.get('artist', '').strip()
        conn = sqlite3.connect('lipvote.db')
        c = conn.cursor()

        c.execute("INSERT INTO choons (choon, artist, votes) VALUES (?,?,?)", (choon, artist, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        redirect("/lipvote")
    else:
        redirect("/lipvote")

@route('/vote', method='GET')
def upvote():
    if request.GET.get('vote','').strip():
        id = request.GET.get('id', '').strip()
        votes = request.GET.get('votes', '').strip()+1
        conn = sqlite3.connect('lipvote.db')
        c = conn.cursor()
        c.execute("UPDATE choons SET VOTES = ? WHERE id = ?", votes, id)
        conn.commit()
        c.close()
        redirect("/lipvote")
    else:
        redirect("/lipvote")

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

#Start server on dev port (8080) and reload when script changes are made
run(reloader=True, port=8000)
