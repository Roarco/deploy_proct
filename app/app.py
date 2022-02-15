from aplication import app
from utils.db import db

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    app.run(debug=True)
