django-agile-boards
===================

This project is an attempt to get Kanban or Scrum boards implemented with
Django.

In order to get started, you need to install the project:

    $ pip install git+https://github.com/linovia/django-agile-boards.git

You can then bootstrap the installation process by generating a sample
configuration file:

    $ agileboards init

Then edit the file in ~/.agileboards/agileboards.conf.py and change
whatever is needed - remember it's a Django settings file.

You need to create the database:

    $ agileboards syncdb
    $ agileboards migrate

Last, you'll need to start the server. By default, it'll be on localhost:8000:

    $ agileboards runserver


Please note that the agilboards command is similar to the django-admin.py
script. You can get all the available commands with:

    $ agileboards help
