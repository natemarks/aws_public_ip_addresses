========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/aws_public_ip_addresses/badge/?style=flat
    :target: https://readthedocs.org/projects/aws_public_ip_addresses
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/natemarks/aws_public_ip_addresses.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/natemarks/aws_public_ip_addresses

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/natemarks/aws_public_ip_addresses?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/natemarks/aws_public_ip_addresses

.. |requires| image:: https://requires.io/github/natemarks/aws_public_ip_addresses/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/natemarks/aws_public_ip_addresses/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/natemarks/aws_public_ip_addresses/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/natemarks/aws_public_ip_addresses

.. |version| image:: https://img.shields.io/pypi/v/aws-public-ip-addresses.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/aws-public-ip-addresses

.. |commits-since| image:: https://img.shields.io/github/commits-since/natemarks/aws_public_ip_addresses/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/natemarks/aws_public_ip_addresses/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/aws-public-ip-addresses.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/aws-public-ip-addresses

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/aws-public-ip-addresses.svg
    :alt: Supported versions
    :target: https://pypi.org/project/aws-public-ip-addresses

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/aws-public-ip-addresses.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/aws-public-ip-addresses


.. end-badges

download and manipulate AWS public IP address list

* Free software: BSD 2-Clause License

Installation
============

::

    pip install aws-public-ip-addresses

Documentation
=============


https://aws_public_ip_addresses.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
