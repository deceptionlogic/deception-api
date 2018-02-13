# Deception Logic API

Deception Logic API Client Library - A python wrapper and CLI for the Deception Logic API.

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
