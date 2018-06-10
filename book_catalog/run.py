from booky import create_app, db
from booky.auth.models import User


if __name__ == '__main__':
    flask_app = create_app('dev')

    with flask_app.app_context():
        db.create_all()

    flask_app.run()

