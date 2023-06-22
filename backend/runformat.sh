#!/bin/sh
poetry run black .
poetry run isort . --profile black
