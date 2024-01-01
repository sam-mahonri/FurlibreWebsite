from flask import render_template, send_file, url_for

def home(): return render_template('public/index.html')
def favicon(): return send_file('static/favicon.svg')