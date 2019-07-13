from flask_restplus import Namespace, Resource

api = Namespace("code", description="download code archive of a run")


@api.route("/<string:run_id>", strict_slashes=False)
class Code(Resource):
    def get(self, run_id):
        """ Download code archive of a run """
        return {"run_id": run_id}
