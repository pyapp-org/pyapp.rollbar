from pyapp.checks import register, Info, Critical


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

    config = settings.ROLLBAR

    if not config.get("access_token"):
        return Info(
            "Rollbar not enabled",
            hint="To enable Rollbar add an `access_token` value into the ROLLBAR "
                 "setting.",
            obj="settings.ROLLBAR[access_token]",
        )
