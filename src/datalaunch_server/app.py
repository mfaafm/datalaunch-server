import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from datalaunch_server.api import api_v0

APP_BASE_PATH = os.getenv("DL_APP_BASE_PATH", "")
API_BASE_URL = APP_BASE_PATH + "/api/v{}"

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(api_v0, url_prefix=API_BASE_URL.format(0))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
