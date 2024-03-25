#!/bin/sh
clear
rm -rf coverage_report
poetry run pytest -vv --cov=api --cov-report=html:coverage_report
# poetry run pytest test/api/models/test_abc.py -vv --cov=api --cov-report=html:coverage_report
