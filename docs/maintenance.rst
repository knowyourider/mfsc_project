Maintenance
===========

Jelastic
---------

Shell access:
::

	ssh 1664@gate.jelastic.eapps.com -p 3022

Activate virtenv:
::

	source virtenv/bin/activate

Created special version of manage.py that calls settings.staging
::
	./stageman.py

Database
--------

Local and remote have same name and same owner.

Remote pgAdmin access:
https://postgres11311-env-6285052.dal.jelastic.vps-host.net/

Local to Remote

Backup with PGAdmin3
	- Custom
	- all default options

Restore with PGAdmin3 connected to remote
	- Restore opts #2 - Clean data first
