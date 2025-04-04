from arteria.web.app import AppService
from tornado.web import URLSpec as url
from miarka_analysis.miarka_handlers import *


def routes(**kwargs):
    """
    Setup routes and feed them any kwargs passed,
    e.g.`routes(config=app_svc.config_svc)` Help will be automatically
    available at /api, and will be based on the doc strings of the
    get/post/put/delete methods :param: **kwargs will be passed when
    initializing the routes.
    Function copied from:
    https://github.com/arteria-project/arteria-checksum/blob/master/checksum/app.py
    """

    return [
        url(r"/api/1.0/version", VersionHandler,
            name="version", kwargs=kwargs),
        url(r"/api/1.0/start", StartHandler,
            name="start", kwargs=kwargs),
    ]


def start():
    """
    Start the ws app
    Function copied from:
    https://github.com/clinical-genomics-uppsala/arteria-bclconvert/blob/develop/bclconvert/app.py
    """

    app_svc = AppService.create(__package__)
    app_svc.start(routes(config=app_svc.config_svc))