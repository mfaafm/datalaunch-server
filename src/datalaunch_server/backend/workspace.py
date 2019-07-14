from datalaunch_server.db import DBApi
from datalaunch_server.storage import StorageAPI


class WorkspaceBackend(object):
    def __init__(
        self, workspace_path="workspace", db=DBApi(), storage=StorageAPI("workspace")
    ):
        self.workspace_path = workspace_path
        self.db = db
        self.storage = storage
