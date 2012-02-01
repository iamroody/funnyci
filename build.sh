#!/bin/bash
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
  echo -e "test: run all test"
  echo -e "run: get status of ci, and send message to weibo or twitter"
}

function main {
	case $1 in
		test) run_test;;
		run) run;;
		*) show_help ; exit 1;;
	esac
}

main $@
