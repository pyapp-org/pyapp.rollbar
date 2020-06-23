import os

ROLLBAR_EXCEPTION_REPORT: bool = True
"""
Register Rollbar as the exception reporter.
"""

ROLLBAR = {
    "access_token": None,
    "environment": os.getenv("ENVIRONMENT", "production"),
}
"""
Rollbar client configuration::

    ROLLBAR = {
        "access_token": "YOUR_ROLLBAR_ACCESS_TOKEN",
        "environment": os.getenv("ENVIRONMENT", "production"),
    }

At a minimum you must provide an access token. If this value is not supplied
the handler will not be activated

A full list of configuration options is available in the Rollbar 
documentation_.
 
.. _documentation: https://docs.rollbar.com/docs/python#configuration-reference

"""
