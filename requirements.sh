#!/bin/bash

if [ $PY_ENV == "dev" ]; then
    echo "The environment is dev!"
    pip3 install --no-cache-dir -r requirements.txt
    pip3 install --no-cache-dir -r requirements-dev.txt
else
    pip3 install --no-cache-dir -r requirements.txt
fi
