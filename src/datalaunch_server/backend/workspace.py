from datalaunch_server.db import DBApi


class WorkspaceBackend(object):
    def __init__(self, workspace_path="workspace", db=DBApi()):
        self.workspace_path = workspace_path
        self.db = db
