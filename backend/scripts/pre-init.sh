#!/bin/sh

echo "============ Updating database ============"
task migrate
echo ""

echo "============ Run Application ============"
echo ""
exec "$@"