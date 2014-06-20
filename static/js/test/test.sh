#!/bin/bash

echo ""
echo "Starting Karma Server (http://karma-runner.github.io)"
echo "-------------------------------------------------------------------"

../node_modules/.bin/karma start ../test/config/karma.conf.js $*
