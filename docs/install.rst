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

If a requirements.txt file is present Jelastic will try to re-install everything everytime you restart the server -- so I'm leaving it out

Static outside of ROOT

To install psycopg2 per
[How to Deploy Mezzanine CMS to Jelastic](http://blog.jelastic.com/2016/05/05/how-to-get-mezzanine-cms-inside-jelastic-cloud/)
::

	PATH=$PATH:/usr/pgsql-9.4/bin/ pip install psycopg2

To set up local Postgres client access to remote db:
[Jelastic - Remote Access to PostgreSQL Database Server | Jelastic](https://docs.jelastic.com/remote-access-postgres)

Here is where Apache is configured - /opt/repo/versions/2.4/etc/conf.d/openshift.conf
Added an Alias for media

Alias /robots.txt /opt/repo/ROOT/robots.txt
Alias /favicon.ico /opt/repo/ROOT/favicon.ico
Alias /images /opt/repo/ROOT/images
Alias /static /opt/repo/ROOT/static
Alias /media /opt/repo/ROOT/media


From support:
The configuration file for apache is located here:
/opt/repo//versions/2.4/etc/conf/httpd_nolog.conf
/opt/repo/versions/2.4/etc/conf/httpd_nolog.conf

The file above includes all .conf files in /opt/shared/conf/etc/conf.d/.
The port configuration is located here:
/opt/shared/conf/etc/conf.d/openshift.conf
The Listen directive in that file specifies that apache will listen on port 8080:
Listen 0.0.0.0:8080

You can get there by clicking on the configuration icon for the apache node, then under 'Favorites', you will see the conf folder, which directs you there.

Further scratch
in httpd_nolog.conf
::
	/var/lib/openshift/

Added to redirect http to https per support
File accessed in Jelastic dashboard
.. nginx/nginx-jelastic.conf
::
	# force https-redirects
        if ($http_X_Forwarded_Proto = http) {
                return 302 https://$host$request_uri;
        }
