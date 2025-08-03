from flask import Flask, request, jsonify, redirect, abort
from .storage import URLStore
from .utils import is_valid_url, generate_code

app = Flask(__name__)
store = URLStore()

@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    url = data.get("url")

    if not url or not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_code()
    while store.get_url(short_code):
        short_code = generate_code()

    store.save_url(short_code, url)
    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    })

@app.route("/<short_code>")
def redirect_url(short_code):
    record = store.get_url(short_code)
    if not record:
        abort(404)
    store.increment_click(short_code)
    return redirect(record["url"])

@app.route("/api/stats/<short_code>")
def stats(short_code):
    record = store.get_url(short_code)
    if not record:
        abort(404)
    return jsonify({
        "url": record["url"],
        "clicks": record["clicks"],
        "created_at": record["created_at"]
    })
