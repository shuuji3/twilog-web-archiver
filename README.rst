twilog-web-archiver
===================

Save month list pages of twilog.org using archive.org.

Requirement
-----------

- :code:`Python >= 3.9`

Install
-------

.. code-block:: bash

    pip install twilog-web-archiver

Usage
-----

.. code-block:: bash

    twilog-web-archiver SCREEN_NAME

Example output
--------------

.. code-block:: bash

    twilog-web-archiver nhk_pr
    archived (cached: True): https://web.archive.org/web/20230411042930/https://twilog.org/NHK_PR/month-2304
    archived (cached: True): https://web.archive.org/web/20230411051906/https://twilog.org/NHK_PR/month-2303
    archived (cached: False): https://web.archive.org/web/20230411051956/https://twilog.org/NHK_PR/month-2303/2
    archived (cached: False): https://web.archive.org/web/20230411052032/https://twilog.org/NHK_PR/month-2303/3
    ...

Description
-----------

When a user has registered twilog.org, you will see the month list page in the user archive page, i.e. `https://twilog.org/NHK_PR/archives <https://twilog.org/NHK_PR/archives>`_.

This program saves every pages in this month list into Wayback Machine on `archive.org <archive.org>`_.

License
-------

- `GNU GPL 3.0 or later <LICENSE>`_
