# cf-predict

Cloud Foundry Python Predictive API Boilerplate

[![Build Status](http://img.shields.io/travis/ronert/cf-predict/master.svg)](https://travis-ci.org/ronert/cf-predict)
[![Coverage Status](http://img.shields.io/coveralls/ronert/cf-predict/master.svg)](https://coveralls.io/r/ronert/cf-predict)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/ronert/cf-predict.svg)](https://scrutinizer-ci.com/g/ronert/cf-predict/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/cf-predict.svg)](https://pypi.python.org/pypi/cf-predict)
[![PyPI Downloads](http://img.shields.io/pypi/dm/cf-predict.svg)](https://pypi.python.org/pypi/cf-predict)

## About

The cf-predict microservice is part of a pluggable ecosystem of cloud native data science microservices for Cloud Foundry.

![Data Science Microservices](https://rodropshare.s3-eu-central-1.amazonaws.com/microservices.png) 

## Getting Started

### Requirements

* Python 3.4+

### Installation

cf-predict can be installed with pip:

```
$ pip install cf-predict
```

or directly from the source code:

```
$ git clone https://github.com/ronert/cf-predict.git
$ cd cf-predict
$ python setup.py install
```

### File Structure

## Basic Usage

After installation, the package can imported:

```
$ python
>>> import cf_predict
>>> cf_predict.__version__
```

## Development

### Make environment

`make env`

### Development Installation

`make develop`

### System Installation

`make install`

### Run All Tests

`make tests`

#### Unit Tests

`make test-unit`

#### Integration Tests

`make test-int`

#### Read Coverage

`make read-coverage`

### Run CI

`make ci`

### Static Analaysis

`make check`

### Watch

`make watch`

### Release

`make upload`

## Documentation

Read the full documentation [here](http://ronert.github.io/cf-predict).
