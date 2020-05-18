# tracking-id-injector
[![Build Status](https://travis-ci.org/msufa/tracking-id-injector.svg?branch=master)](https://travis-ci.org/msufa/tracking-id-injector)
[![codecov](https://codecov.io/gh/msufa/tracking-id-injector/branch/master/graph/badge.svg)](https://codecov.io/gh/msufa/tracking-id-injector)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/msufa/tracking-id-injector/blob/master/LICENSE)

A simple script for ingesting Google Analytics tracking tags into HTML documents.

The main purpose of this script is to use it in CI for static WWW pages to ingest tracking code for Google Analytics.

## Installation
Optionally you might want to set up `virtualenv` before installing the script:

```
$ virtualenv env
$ . ./env/bin/activate
```

Next:

```
$ git clone git@github.com:msufa/tracking-id-injector.git
$ cd tracking-id-injector
$ python setup.py install
$ tracking-id-injector
usage: tracking-id-injector tracking_id input_filename output_filename
```

`tracking_id` should be set to the `UA...` Tracking ID from the Google Analytics Tracking Info page.

## Usage
To inject tracking tags into every HTML file in `./www` directory:

```
find ./www -maxdepth 1 -name "*.html" | xargs -n 1 -I {} tracking-id-injector $GOOGLE_TRACKING_ID {} {}
```

You might consider storing the value of your Tracking ID under `GOOGLE_TRACKING_ID`
in the environment variables of e.g. you CI pipeline.

## Testing
```
$ python setup.py flake8
$ python setup.py test
```

## Caveats
This script injects a Google tracking JavaScript tag between `head` tags in a HTML document.
If there are `meta` tags that are not properly closed inside of `head`, the tracking script might be injected
under the last open `meta` tag and an additional closing `meta` tag might be added.
This is caused by intricacies of [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) which is used to
parse and manipulate HTML.

Dummy change to trigger CI
