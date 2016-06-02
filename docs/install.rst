Jelastic install
================

Create environment
[Jelastic - Django Apps Deployment | Jelastic](https://docs.jelastic.com/django)

virtenv already present
::
	source virtenv/bin/activate
	pip install django

Edit the suggested wsgi.py file to our actual directory structure.
Sym link application to the wsgi.py file or just rename it "application"

To install psycopg2 per
[How to Deploy Mezzanine CMS to Jelastic](http://blog.jelastic.com/2016/05/05/how-to-get-mezzanine-cms-inside-jelastic-cloud/)
::

	PATH=$PATH:/usr/pgsql-9.4/bin/ pip install psycopg2

To set up local Postgres client access to remote db:
[Jelastic - Remote Access to PostgreSQL Database Server | Jelastic](https://docs.jelastic.com/remote-access-postgres)
