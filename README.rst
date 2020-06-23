###############
pyApp - Rollbar
###############

*Let us handle the boring stuff!*

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
      :alt: Once you go Black...

Integration with Rollbar_ error tracking. The extension provides the following
features.

Initialise Client
    On startup of the application the client is configured ready for use.

Top-Level Error Reporting
    Register a top level exception handler to catch any exceptions that are not
    handled by the application

.. _Rollbar: https://rollbar.com/


Installation
============

Install using *pip*::

    pip install pyapp.rollbar


Configuration
-------------

Settings can be provided in one of two ways, via the `ROLLBAR` settings key or
via the `ROLLBAR_ACCESS_TOKEN` and `ENVIRONMENT` environment variables.


Usage
=====

Rollbar itself is a singleton available from the `rollbar` module. eg

.. code-block:: python

    import rollbar

    rollbar.report_message("Hi!")
