from flask_restplus import Namespace, Resource
from datalaunch_server.backend import WorkspaceBackend, RunBackend
from .helpers import serialize_datetime

api = Namespace("runs", description="get information about all runs")

run_backend = RunBackend(WorkspaceBackend())


@api.route("/", strict_slashes=False)
class Runs(Resource):
    def get(self):
        """ Get detailed information about all runs """
        results = run_backend.get_all_runs()
        return [serialize_datetime(r) for r in results]
