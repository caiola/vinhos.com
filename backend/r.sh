#!/bin/sh
rm -rf coverage_report
poetry run pytest -vv --cov=api --cov-report=html:coverage_report