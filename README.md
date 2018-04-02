# Word Count

This project will list top word frequencies for given text.

## Setup Instructions

Requires Docker, Docker-Compose, Make.

1. Clone repo
1. `make build`
1. `make up`

App is live at `http://localhost:5000`

## Solution Overview

Implemented a single serving [Flask](http://flask.pocoo.org/) site that takes in a text file and calculates the 25 most frequently used words. Users have the option of excluding stopwords (pulled from [NLTK](http://www.nltk.org/book/)) from the calculation.

Can either upload a file (higher precedence) or enter text. Mouseover word in resulting table to get occurence count.

Styled using Bootstrap.

## Solution Details

* [`routes.py`](https://github.com/alysivji/word-count/blob/master/app/routes.py) is the main module of this program
* HTML templates are stored [here](https://github.com/alysivji/word-count/tree/master/app/templates)
* Basic tests for "stemming" words are in [`routes_test.py`](https://github.com/alysivji/word-count/blob/master/tests/routes_test.py)
