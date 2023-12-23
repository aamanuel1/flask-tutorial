#!/bin/sh
flask --app flaskr init-db
flask --app flaskr run --debug --host=0.0.0.0