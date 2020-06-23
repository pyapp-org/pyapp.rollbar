"""
pyApp - Rollbar
~~~~~~~~~~~~~~~

pyApp Extension for Rollbar_ error tracking.

"""
import sys
from pathlib import Path

import rollbar
from pyapp.app import get_running_application, CommandOptions, CommandGroup, argument, KeyValueAction
from pyapp.conf import settings


def _get_root_path():
    """
    Determine your applications root path.

    This uses the `root_module` identified by `pyapp.app.CliApplication`.

    """
    app = get_running_application()
    root_path = Path(app.root_module.__file__).resolve().parent
    return root_path.as_posix()


def rollbar_init():
    """
    Initialise rollbar client from settings
    """
    init_settings = settings.ROLLBAR.copy()

    # Only activate if an access token is provided
    if init_settings.get("access_token"):

        # Determine root path if not provided
        if "root" not in init_settings:
            init_settings["root"] = _get_root_path()

        rollbar.init(**init_settings)


def _monkeypatch_exception_report():
    """
    Apply Rollbar top level handler to the current running application.
    """
    app = get_running_application()
    default_report = app.exception_report

    def rollbar_exception_report(exception: BaseException, opts: CommandOptions):
        rollbar.report_exc_info(sys.exc_info(), extra_data=opts.__dict__)
        return default_report(exception, opts)

    app.exception_report = rollbar_exception_report


class Extension:
    """
    pyApp - Rollbar
    """

    default_settings = ".default_settings"
    checks = ".checks"

    @staticmethod
    @argument("DATA", nargs="+", action=KeyValueAction)
    @argument("-m", "--message", default="Sample Message")
    @argument("-l", "--level", default="debug", choices=('critical', 'error', 'warning', 'info', 'debug'))
    async def message(opts: CommandOptions):
        """
        Report a message to rollbar
        """
        rollbar.report_message(
            opts.message,
            level=opts.level,
            extra_data=opts.DATA
        )

    @staticmethod
    def register_commands(root: CommandGroup):
        group = root.create_command_group("rollbar")
        group.command(Extension.message)

    @staticmethod
    def ready():
        rollbar_init()

        if settings.ROLLBAR_EXCEPTION_REPORT:
            _monkeypatch_exception_report()
