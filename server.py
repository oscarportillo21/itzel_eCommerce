from flask import Flask, render_template, redirect

app = Flask (__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/display')
def display_item():
    return render_template('display.html')

@app.route('/stickers')
def stickers():
    return render_template('stickers.html')

@app.route('/branding')
def branding():
    return render_template('branding.html')

@app.route('/request_confirmation')
def request_confirmationPage():
    return render_template('reqconfirmation.html')

@app.route('/requestSub', methods=['POST'])
def request_submission():
    return redirect('/request_confirmation')


@app.route('/shoppingcart')
def shoppingcart():
    return render_template('checkout.html')

@app.route('/order')
def order():
    return render_template('order.html')


if __name__ == "__main__":
    app.run(debug= True)