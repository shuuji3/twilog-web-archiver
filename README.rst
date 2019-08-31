twilog-web-archiver
===================

.. image:: https://circleci.com/gh/shuuji3/twilog-web-archiver.svg?style=svg
    :target: https://circleci.com/gh/shuuji3/twilog-web-archiver

Save month list pages of twilog.org using archive.org.

Requirement
-----------

- :code:`Python >= 3.6`

Install
-------

.. code-block:: bash

    $ pip install twilog-web-archiver

Usage
-----

.. code-block:: bash

    $ twilog-web-archiver SCREEN_NAME

Description
-----------

When a user has registered twilog.org, you will see the month list page in the user archive page, i.e. `https://twilog.org/NHK_PR/archives <https://twilog.org/NHK_PR/archives>`_.

This program saves every pages in this month list into Wayback Machine on `archive.org <archive.org>`_.

License
-------

- `GNU GPL 3.0 or later <LICENSE>`_
