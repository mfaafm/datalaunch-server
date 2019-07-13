from flask_restplus import Namespace, Resource

api = Namespace("runs", description="get information about all runs")


@api.route("/", strict_slashes=False)
class Runs(Resource):
    def get(self):
        """ Get detailed information about all runs """
        return [{"id": "123", "duration": 23}, {"id": "456", "duration": 42}]
