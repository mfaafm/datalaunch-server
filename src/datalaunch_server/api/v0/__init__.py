import os
from flask import Blueprint
from flask_restplus import Api
from .workspace import api as workspace_namespace
from .run import api as run_namespace
from .runs import api as runs_namespace
from .logs import api as logs_namespace
from .code import api as code_namespace


API_VERSION = "0"


blueprint = Blueprint(f"api_v{API_VERSION}", __name__)

swagger_active = os.getenv("DL_API_V0_SWAGGER", "True")
swagger_doc_path = "/" if swagger_active == "True" else False

api = Api(
    blueprint,
    title="datalaunch server api",
    version=API_VERSION,
    description="The datalaunch server run_backend api, which allows management of runs",
    doc=swagger_doc_path,
)

api.add_namespace(workspace_namespace)
api.add_namespace(run_namespace)
api.add_namespace(runs_namespace)
api.add_namespace(logs_namespace)
api.add_namespace(code_namespace)
