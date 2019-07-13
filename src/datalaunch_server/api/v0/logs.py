from flask_restplus import Namespace, Resource

api = Namespace("logs", description="retrieve logs from a run")


@api.route("/<string:run_id>", strict_slashes=False)
class Logs(Resource):
    def get(self, run_id):
        """ Get logs of a run """
        return {"run_id": run_id}
