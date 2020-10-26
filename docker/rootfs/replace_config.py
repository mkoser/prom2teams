#!/usr/bin/env python
import os

with open('/opt/prom2teams/config.ini', 'r') as file:
  filedata = file.read()

filedata = filedata.replace("prom2teamsport", os.environ.get("PROM2TEAMS_PORT"))
filedata = filedata.replace("prom2teamshost", os.environ.get("PROM2TEAMS_HOST"))
filedata = filedata.replace("prom2teamssslcert", os.environ.get("PROM2TEAMS_SSL_CERT"))
filedata = filedata.replace("prom2teamssslkey", os.environ.get("PROM2TEAMS_SSL_KEY"))
filedata = filedata.replace("prom2teamsconnector", os.environ.get("PROM2TEAMS_CONNECTOR"))
filedata = filedata.replace("prom2teamsgroupalertsby", os.environ.get("PROM2TEAMS_GROUP_ALERTS_BY"))

with open('/opt/prom2teams/config.ini', 'w') as file:
  file.write(filedata)
