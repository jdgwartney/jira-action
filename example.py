#!/usr/bin/env python
from jira import JIRA
import json
import os

user = os.environ['JIRA_USER']
password = os.environ['JIRA_PASSWORD']

jira = JIRA('https://boundary.jira.com', basic_auth=(user, password))

issue = jira.issue('PLUG-8')
print(type(issue))
#print(json.dumps(issue.fields))
print(issue.fields.project.key)
print(issue.fields.issuetype.name)
print(issue.fields.reporter.displayName)
