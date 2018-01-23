#
# Foreman Procfile (primarily used for Heroku instances).
#

web: uwsgi --ini=uwsgi.ini --req-logger="file:/dev/null" --route=".* basicauth:RH,$BASIC_AUTH"
