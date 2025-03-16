#!/bin/bash

TEST_TYPE=$1

case $TEST_TYPE in
    "smoke")
        PATTERN="smoke"
        ;;
    "sanity")
        PATTERN="sanity"
        ;;
    "regression")
        PATTERN="regression"
        ;;
    "login")
        PATTERN="login"
        ;;
    "search")
        PATTERN="search"
        ;;
    "task1")
        PATTERN="task1"
        ;;
    "task2")
        PATTERN="task2"
        ;;
    "task3")
        PATTERN="task3"
        ;;
    *)
        PATTERN="all"
        ;;
esac

# Run tests
pytest -v -s tests/ --disable-warnings -m "$PATTERN" --alluredir=./allure-results

# Generate and open Allure report
allure serve allure-results 