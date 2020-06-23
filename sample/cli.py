from pyapp.app import CliApplication

APP = CliApplication()


@APP.command()
def error(opts):
    """
    Generate an error
    """
    raise Hell


def main(args=None):
    APP.dispatch(args)
