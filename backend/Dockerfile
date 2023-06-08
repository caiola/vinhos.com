ARG PYTHON_VERSION
FROM python:3.10

# Make a working directory in the image and set it as working dir.
RUN mkdir /app
WORKDIR /app

# make sure that pip & setuptools are installed and to date
RUN pip install --upgrade pip setuptools wheel && pip install poetry

# ERROR "you need a C compiler to build uWSGI"
RUN apt-get -y install gcc

# We are using /mnt
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY . .

CMD [ "uwsgi", "--ini", "app.ini" ]
