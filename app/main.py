from flask import Flask
import logging
import logging_loki


handler = logging_loki.LokiHandler(
	url="http://loki:3100/loki/api/v1/push",
	tags={"application": "my-app"},
	version="1",
	)

logger = logging.getLogger("my-logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

app = Flask(__name__)


@app.route("/")
def hello():
    logger.info(
	"Something happened",
	extra={"tags": {"service": "my-service"}},
	)
    return "Hello World from Flask"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
