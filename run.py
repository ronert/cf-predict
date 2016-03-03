#!/usr/bin/env python
import os
from cf_predict import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
