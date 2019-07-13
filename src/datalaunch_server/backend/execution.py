import time
from datetime import datetime


class ExecutionBackend(object):
    def __init__(self, workspace):
        self.workspace = workspace
        self.db = workspace.db

    def build_run(self, run):

        run["status"] = "building"
        run["build_started"] = datetime.utcnow()
        self.db.update_run(run)

        # TODO: start build

        time.sleep(10)

        run["status"] = "build finished"
        run["build_finished"] = datetime.utcnow()

        return run

    def start_run(self):
        run = self.create_run()
        run = self.build_run(run)

        run["status"] = "running"
        run["run_started"] = datetime.utcnow()

        return run
