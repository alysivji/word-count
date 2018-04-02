# Word Count

This project will list top word frequencies for given text.

## Setup Instructions

Requires Docker, Docker-Compose, Make.

1. Clone repo
1. `make build`
1. `make up`

App is live at `http://localhost:5000`

## Solution Overview

Implemented a single serving [Flask](http://flask.pocoo.org/) that takes in a text file or user input and calculates the 25 most frequently used words. Users have the option of excluding stopwords (pulled from [NLTK](http://www.nltk.org/book/)) from being counted.

Can either upload a file (higher precedence) or enter text.

Styled using Bootstrap.
