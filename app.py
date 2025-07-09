from flask import Flask, render_template, request, redirect
import webbrowser

app = Flask(__name__)

BASE_URLS = {
    "TippmixPro": "https://www.tippmixpro.hu",
    "Vegas": "https://www.vegas.hu",
    "Unibet": "https://www.unibet.hu",
    "Tippmix.hu": "https://www.tippmix.hu"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        match = request.form.get('match', '').strip()
        event = request.form.get('event', '').strip()
        site = request.form.get('site', '')

        if not match or not event or site not in BASE_URLS:
            error = "Kérlek tölts ki minden mezőt helyesen!"
            return render_template('index.html', error=error, BASE_URLS=BASE_URLS)

        # Nincs ismert URL, így csak a főoldalra irányítjuk
        url = BASE_URLS[site]
        return redirect(url)

    return render_template('index.html', BASE_URLS=BASE_URLS)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
