from flask_restplus import Namespace, Resource
import threading

api = Namespace("status", description="Status of the management server")


@api.route("/", strict_slashes=False)
class Code(Resource):
    def get(self):
        """ Get management server status information """
        return {
            "status": "happy",
            "num_active_threads": threading.active_count(),
            "active_threads": [f"{t.name} ({t.ident})" for t in threading.enumerate()],
        }
