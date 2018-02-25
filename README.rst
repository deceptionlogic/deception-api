==================
deceptionlogic
==================

.. image:: https://img.shields.io/pypi/v/deceptionlogic.svg
    :target: https://pypi.python.org/pypi/deceptionlogic/
    :alt: Latest Version

.. image:: https://travis-ci.org/deceptionlogic/deception-api.svg?branch=master
    :target: https://travis-ci.org/deceptionlogic/deception-api

``deceptionlogic`` is a Python wrapper and CLI tool for the `Deception Logic REST API`_.

Installation
------------
.. code-block:: bash

    $ pip install deceptionlogic

CLI usage
---------
.. code-block:: bash

    $ deception --get alerts

Module usage
------------
.. code-block:: python

    from deceptionlogic import api
    delo = api.Client('keyid', 'secret')
    delo.get_alerts()

More details and the latest updates can be found on the `GitHub Project Page`_.

.. _Deception Logic REST API: https://deceptionlogic.com/
.. _GitHub Project Page: https://github.com/deceptionlogic/deception-api