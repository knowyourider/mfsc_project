Jelastic Maintenance
====================

Control Panel
---------

Restart Apache after GIT update 

Shell
------

Shell access:
::

	ssh 1664@gate.jelastic.eapps.com -p 3022
	ssh 1721@gate.jelastic.eapps.com -p 3022

Activate virtenv:
::
	source virtenv/bin/activate
	cd ROOT

Created special version of manage.py that calls settings.staging
::
	cd mfsc
	./stageman.py

Database
--------

Local and remote have same name and same owner.

Remote pgAdmin access:
http://postgres11311-env-6285052.njs.jelastic.vps-host.net

Local to Remote

Backup with PGAdmin3
	- Custom
	- all default options

Restore with PGAdmin3 connected to remote
	- Restore opts #2 - Clean data first

Misc
--------

Logs at: /opt/repo/logs/
