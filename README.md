Website for Graffathon (http://graffathon.fi), a computer graphics hatckathon organized by DOT (http://dot.ayy.fi/)

## Running in production

Production configuration is kept in GIT (settings/prod.py). However, the actual setting values are read from environment variables.

```
git clone https://github.com/anttihirvonen/graffathon.git
cd graffathon
mkvirtualenv pyenv
source pyenv/bin/activate
pip install -r config/prod.txt
mkdir env
```

Put all required setting values into env/ as separate files.

All that is left to do is initialize database, collect static files and run the app using Gunicorn (currently using port 36757 on Kapsi, but any port will do). 

```
envdir env python manage.py initialize_database
envdir env python manage.py collect
envdir env/ gunicorn -b 0.0.0.0:36757 app:app
```

Finally, configure reverse proxy so that all other requests except static files are redirected to the running Gunicorn instance.

## Updating

Pull from GIT, run ```collect``` and restart Gunicorn. Simple!
