![](http://pinaxproject.com/pinax-design/patches/pinax-submissions.svg)

# Pinax Submissions

[![](https://img.shields.io/pypi/v/pinax-submissions.svg)](https://pypi.python.org/pypi/pinax-submissions/)

[![CircleCI](https://img.shields.io/circleci/project/github/pinax/pinax-submissions.svg)](https://circleci.com/gh/pinax/pinax-submissions)
[![CodeCov](https://img.shields.io/codecov/c/github/pinax/pinax-submissions.svg)](https://codecov.io/gh/pinax/pinax-submissions)
[![](https://img.shields.io/github/contributors/pinax/pinax-submissions.svg)](https://github.com/pinax/pinax-submissions/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-submissions.svg)](https://github.com/pinax/pinax-submissions/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-submissions.svg)](https://github.com/pinax/pinax-submissions/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Features](#features)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)

## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-submissions

### Overview

`pinax-submissions` is an app for proposing and reviewing submissions.

#### Features

* propose items
* review items
* facilitate conservation between proposer and reviewer


#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---
2.2  |  *  |  *  |  *
3.0  |  *  |  *  |  *


## Documentation

### Installation

To install pinax-submissions:

```shell
    $ pip install pinax-submissions
```

Add `pinax.submissions` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.submissions",
    ]
```

Add `pinax.submissions.urls` to your project urlpatterns:

```python
    urlpatterns = [
        # other urls
        url(r"^submissions/", include("pinax.submissions.urls", namespace="pinax_submissions")),
    ]
```


## Change Log

### 2.0.0

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 1.0.3

* Allow use with any account-management package by removing django-user-accounts dependency

### 1.0.2

* Update installation requirements
* Update CI configuration
* Update .gitignore
* Remove unused MANIFEST entries
* Update patch target links
* Add namespacing to tests/urls.py

### 1.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10 and Python 3.3 support
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description
* Standardize documentation layout
* Add django>=1.11 to requirements

### 0.3.0

### 0.2.4

### 0.2.3

### 0.2.2

### 0.2.1

### 0.2


## History

`pinax-submissions` was extracted from the `symposion` project.


## Contribute

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
