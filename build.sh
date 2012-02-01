#!/bin/bash

function env {
    pip install -r requirements.pip
}

function run_test {
    nosetests;
}

function run {
    while true;do
        python pygoboard.py;
        sleep 2;
    done
}

function show_help {
  echo "Usage: build.sh [COMMAND]"
  echo ""
  echo "COMMAND:"
  echo -e "env: check env and install dependency"
  echo -e "test: run all test"
  echo -e "run: get status of ci, and send message to weibo or twitter"
}

function main {
	case $1 in
	    env) env;;
		test) run_test;;
		run) run;;
		*) show_help ; exit 1;;
	esac
}

main $@
