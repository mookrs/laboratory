from flask import Flask, session, redirect, url_for, request, render_template, flash
from flask_oauthlib.client import OAuth, OAuthException

app = Flask(__name__)
app.debug = True
app.secret_key = 'AA0Zr98j/3yXR~XHH!jmN]LWX/,?RT'

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


@fanfou.tokengetter
def get_fanfou_token():
    return session.get('fanfou_token')


@app.route('/')
def index():
    if 'fanfou_token' not in session:
        flash('Unable to load fanfou_oauth.')
    return render_template('index.html')


@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['tweet']
    if not status:
        return redirect(url_for('index'))
    resp = fanfou.post('statuses/update.json', data={
        'status': status
    })
    if resp.status == 403:
        flash('Your tweet was too long.')
    elif resp.status == 401:
        flash('Authorization error with Fanfou.')
    else:
        flash('Successfully!')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    callback = url_for('oauthorized', next=request.args.get('next') or request.referrer or None, _external=True)
    return fanfou.authorize(callback=callback)


@app.route('/logout')
def logout():
    session.pop('fanfou_token', None)
    return redirect(url_for('index'))


@app.route('/oauthorized')
def oauthorized():
    next_url = request.args.get('next') or url_for('index')
    resp = fanfou.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
    if isinstance(resp, OAuthException):
        flash('Access denied: %s' % resp.message)
    session['fanfou_token'] = resp
    return redirect(next_url)


if __name__ == '__main__':
    app.run()