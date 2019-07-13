from flask_restplus import Namespace, Resource, fields

api = Namespace("workspace", description="workspace management and status")


@api.route("/", strict_slashes=False)
class Workspace(Resource):
    def get(self):
        """ Get information about the workspace """
        return {"info": "I am a workspace"}
