=====
notifications
=====

notifications is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'notificaions',
      )

2. Run `python manage.py syncdb` to create the notificaion models.

