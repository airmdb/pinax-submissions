from setuptools import find_packages, setup


LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/blank.svg
    :target: https://pypi.python.org/pypi/pinax-submissions/

=================
Pinax Submissions
=================
.. image:: https://img.shields.io/pypi/v/pinax-submissions.svg
    :target: https://pypi.python.org/pypi/pinax-submissions/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-submissions/
.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-submissions.svg
    :target: https://circleci.com/gh/pinax/pinax-submissions
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-submissions.svg
    :target: https://codecov.io/gh/pinax/pinax-submissions
.. image:: https://img.shields.io/github/contributors/pinax/pinax-submissions.svg
    :target: https://github.com/pinax/pinax-submissions/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-submissions.svg
    :target: https://github.com/pinax/pinax-submissions/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-submissions.svg
    :target: https://github.com/pinax/pinax-submissions/pulls?q=is%3Apr+is%3Aclosed
.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/


``pinax-submissions`` is an app for proposing and reviewing submissions. It was pulled from ``symposion``.


Supported Django and Python Versions
------------------------------------
+-----------------+-----+-----+-----+-----+
| Django \ Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
| 1.11            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
| 2.0             |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""


setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a Django app for proposing and reviewing submissions. It was pulled from Symposion.",
    name="pinax-submissions",
    long_description=LONG_DESCRIPTION,
    version="1.0.1",
    url="http://github.com/pinax/pinax-submissions/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "submissions": []
    },
    test_suite="runtests.runtests",
    tests_require=[
    ],
    install_requires=[
        "django>=1.11",
        "Markdown>=2.6.3",
        "django-model-utils>=2.3.1",  # needs 3.1.1 which is not on pypi at this time
        "django-appconf>=1.0.1",
        "django-user-accounts>=2.0.0"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
