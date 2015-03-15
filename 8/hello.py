from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
from flask_oauthlib.client import OAuth, OAuthException

app = Flask(__name__)

oauth = OAuth(app)

fanfou = oauth.remote_app(
    'fanfou',
    base_url='http://api.fanfou.com/',
    request_token_url='http://fanfou.com/oauth/request_token',
    access_token_url='http://fanfou.com/oauth/access_token',
    authorize_url='http://fanfou.com/oauth/authorize',
    consumer_key='bd58c28d30ba2a1fe7b7ca96dd71f7ea',
    consumer_secret='f975fa68779936ce967921356a315853',
)

x = '2'

@fanfou.tokengetter
def get_fanfou_token(token=None):
    return session.get('fanfou_token')


@app.route('/')
def index():
    session['foo'] = 42
    global x
    if 'fanfou_token' not in session:
        flash('Unable to load fanfou_oauth.' + x)
    return render_template('index.html')


@app.route('/tweet', methods=['POST'])
def tweet():
    session['fo'] = 42
    status = request.form['tweet']
    if not status:
        return redirect(url_for('index'))
    resp = fanfou.post('statuses/update.json', data={
        'status': status
    })
    if resp.status == 403:
        return 'Your tweet was too long.'
    elif resp.status == 401:
        return 'Authorization error with Twitter.'
    else:
        return '?'
    return redirect(url_for('index'))


@app.route('/login')
def login():
    global x
    x = '22'
    callback = url_for(
        'authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True
    )
    return fanfou.authorize(callback=callback)


@app.route('/logout')
def logout():
    session.pop('fanfou_token', None)
    return redirect(url_for('index'))


@app.route('/authorized')
def authorized():
    global x
    x = '3'
    next_url = request.args.get('next') or url_for('index')
    resp = fanfou.authorized_response()
    if isinstance(resp, OAuthException):
        return 'Access denied: %s' % resp.message
    if resp is None:
        x = '4'
        flash('Access denied')
    else:
        x = '5'
        #session['fanfou_token'] = (resp['oauth_token'], '')
        #session['fanfou_key'] = resp['oauth_consumer_key']
    return redirect(next_url)


if __name__ == '__main__':
    app.secret_key = 'AA0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)