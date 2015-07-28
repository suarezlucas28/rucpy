# RUCPY
This project aims to provide information of the RUC of Paraguay./Este proyecto tiene como objetivo proporcionar información de los RUC del Paraguay.


# REQUERIMENTS/REQUERIMIENTOS

Django>=1.8	

Django REST Framework

PostgreSQL


# INSTRUCTIONS/INSTRUCCIONES

1- Run python manage.py syncdb. (not for Django 1.9)/ Correr python manage.py syncdb. (no para django 1.9)

2- Restore Database ruc_db.backup, search it in folder "db"./ Restaurar base de datos ruc_db.backup, buscarlo en el directorio "db".

3- Run python manage.py runserver for test./ Correr python manage.py runserver para testear.

4- Use url: http://127.0.0.1:8000/rucs/ruc/1000060, replace "1000060" for own ci./ Usar url: http://127.0.0.1:8000/rucs/ruc/1000060, reemplace "1000060" por tu propia ci.
