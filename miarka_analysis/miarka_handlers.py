import json
import subprocess
from arteria.web.handlers import BaseRestHandler

from miarka_analysis import __version__ as version


class ArteriaBaseHandler(BaseRestHandler):
    """
    Base handler for Arteria handlers.
    """

    def initialize(self, config, **kwargs):
        """
        Ensures that any parameters feed to this are available
        to subclasses.

        :param: config configuration used by the service
        """
        self.config = config


class VersionHandler(ArteriaBaseHandler):

    """
    Get the version of the service
    """

    def get(self):
        """
        Returns the version of the checksum-service as json. Format looks as follows:
        {
           "version": "1.0.0"
        }
        """
        self.write_object({"version": version})


class StartHandler(ArteriaBaseHandler):

    """
    Start the start-script
    """
    def post(self):
        request_data = json.loads(self.request.body)
        print(request_data)
        script = "{}start_{}_{}.sh".format(self.config["script_dir"], request_data["wp"], request_data["analysis"])
        print(script)
        subprocess.run(script)
        response_data = {"job_id": "job_id", "service_version": "version", "link": "status_end_point", "state": "State.STARTED", "md5sum_log": "log_file.name"}
        self.write_object(response_data)
        
