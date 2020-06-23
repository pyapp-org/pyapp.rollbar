###############
pyApp - Rollbar
###############

*Let us handle the boring stuff!*

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
      :alt: Once you go Black...

Integration with Rollbar_ error tracking. Provides both access to a Rollbar
client and integration with the toplevel error handler to capture unhandled
exceptions.

.. _Rollbar: https://rollbar.com/


Installation
============

Install using *pip*::

    pip install pyapp.rollbar


Usage
=====

Add a rollbar entry into settings:

.. code-block:: python

  ROLLBAR = {
  }
