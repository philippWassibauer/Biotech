
mkvirtualenv biotech
workon biotech
pip install -r requirements/project.txt
./manage.py syncdb --all
./manage.py migrate --fake
./manage.py runserver