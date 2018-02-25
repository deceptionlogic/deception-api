# Deception Logic API

Deception Logic API Client Library - A python wrapper and CLI for the Deception Logic API.

[![Latest Version](https://img.shields.io/pypi/v/deceptionlogic.svg)](https://pypi.python.org/pypi/deceptionlogic/)
[![Build Status](https://travis-ci.org/deceptionlogic/deception-api.svg?branch=master)](https://travis-ci.org/deceptionlogic/deception-api)

### Installation

`pip install deceptionlogic`

### CLI usage

`$ deception --get alerts`

Run `deception --help` for a complete list of CLI options.

### Module usage

```
from deceptionlogic import api
delo = api.Client('keyid', 'secret')
delo.get_alerts()
```

See example.py for inline usage comments and reference implementation.
