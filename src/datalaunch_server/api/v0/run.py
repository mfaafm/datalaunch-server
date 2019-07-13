from flask_restplus import Namespace, Resource, fields
from datalaunch_server.backend import WorkspaceBackend, RunBackend
from .helpers import serialize_datetime

api = Namespace("run", description="run management and status")

environment_model = api.model("environment variable specification", {})
conda_spec_model = api.model("conda specification", {})
docker_spec_model = api.model("docker specification", {})

run_model = api.model(
    "run specification",
    {
        "name": fields.String(required=True),
        "environment": fields.Nested(environment_model),
        "conda_spec": fields.Nested(conda_spec_model),
        "docker_spec": fields.Nested(docker_spec_model),
    },
)

run_backend = RunBackend(WorkspaceBackend())


@api.route("/", strict_slashes=False)
class RunList(Resource):
    def get(self):
        """ Get a list of all run IDs """
        return run_backend.get_run_ids()

    @api.expect(run_model, validate=True)
    def post(self):
        """ Create and start a new run """
        run = run_backend.create_run(api.payload)
        return serialize_datetime(run)


@api.route("/<string:run_id>", strict_slashes=False)
class Run(Resource):
    def get(self, run_id):
        """ Get information about a run """
        run = run_backend.get_run(run_id)
        return serialize_datetime(run)

    def put(self, run_id):
        """ Terminate an ongoing run """
        run_backend.terminate_run(run_id)
        return {"run_id": run_id}

    def delete(self, run_id):
        """ Delete a run """
        run_backend.delete_run(run_id)
        return {"run_id": run_id}
