#!/bin/bash

# Run your application as nbctfuser
exec gosu nbctfuser /data/venv/bin/flask run --host 0.0.0.0 -p 1337
