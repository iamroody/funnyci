#!/bin/bash

function env {
    pip install -r requirements.pip
}

function run_test {
    nosetests;
}

function fake {
    python pygoboard.py test;
}

function real {
    python pygoboard.py;
}

function show_help {
  echo "Usage: build.sh [COMMAND]"
  echo ""
  echo "COMMAND:"
  echo -e "env: check env and install dependency"
  echo -e "test: run all test"
  echo -e "fake: read test data"
  echo -e "real: read real go data"
}

function main {
	case $1 in
	    env) env;;
		test) run_test;;
		fake) fake;;
		real) real;;
		*) show_help ; exit 1;;
	esac
}

main $@
