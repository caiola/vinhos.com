#!/bin/sh
rm -rf coverage_report
poetry run pytest --cov=api --cov-report=html:coverage_report