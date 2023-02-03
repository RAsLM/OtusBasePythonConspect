#!/usr/bin/env bash

echo "Apply migration"

flask db upgrade

echo "migration ok"

exec "$@"