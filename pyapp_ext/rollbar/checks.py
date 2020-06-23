from pyapp.checks import register, Critical


@register
def rollbar_settings(settings, **_):
    """
    Check if rollbar settings are defined.
    """
    if not hasattr(settings, "ROLLBAR"):
        return Critical(
            "ROLLBAR setting not defined",
            hint="Define the ROLLBAR setting.",
            obj="settings.ROLLBAR",
        )
