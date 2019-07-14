import docker
from datetime import datetime


class RunExecution(object):
    def __init__(self, workspace, run_id, docker_client=docker.from_env()):
        self.workspace = workspace
        self.run_id = run_id
        self.db = workspace.db
        self.docker_client = docker_client

    def _update_run(self, fields):
        run = self.db.get_run(self.run_id)
        run.update(fields)
        self.db.update_run(run)

    def run(self):
        self.build_run()
        self.start_run()

    def build_run(self):
        self._update_run({"status": "building", "build_started": datetime.utcnow()})

        image, build_logs = self.docker_client.images.build(
            path="/Users/martijnarts/External_code/datalaunch_internal/docker/miniconda/",
            tag=f"req:{self.run_id}",
            target="requirements",
        )

        print(list(build_logs))

        image, build_logs = self.docker_client.images.build(
            path="/Users/martijnarts/External_code/datalaunch_internal/docker/miniconda/",
            tag=f"run:{self.run_id}",
            target="run",
        )

        print(list(build_logs))

        self._update_run(
            {"status": "build finished", "build_finished": datetime.utcnow()}
        )

    def start_run(self):
        self._update_run({"status": "running", "run_started": datetime.utcnow()})

        result = self.docker_client.containers.run(
            f"run:{self.run_id}", "python /opt/project/run.py"
        )
        print(result)

        self._update_run({"status": "run finished", "run_finished": datetime.utcnow()})
