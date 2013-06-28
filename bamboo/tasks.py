# coding: utf-8

# $Id: $
import re

from jira.client import JIRA
from bamboo.helpers import parse_config


class Tasks(object):
    def __init__(self, configfile='bamboo.cfg'):
        self.jira_user = 'bamboo'
        self.jira_password = 'bamboo'
        self.server_name = 'https://jira.rutube.ru'
        parse_config(self, configfile)
        self.jira = JIRA({'server': self.server_name},
                         basic_auth=(self.jira_user, self.jira_password))

    def get_versions(self, task_key):
        self.issue = self.jira.issue(task_key)
        result = []
        for v in self.issue.fields.fixVersions:
            # if v.archived or v.released:
            #     continue
            version = v.name
            if not re.match(r'^[\d]+\.[\d]+\.[\d]+$', version):
                continue
            result.append(version)
        return result

    def search_tasks(self, project_key, status=None, issue_type=None,
                     assignee=None, release=None):
        query = "project = %s" % project_key
        if isinstance(status, (tuple, list)):
            statuses = ', '.join('"%s"' % s for s in status)
            query += ' AND status IN (%s)' % statuses
        if isinstance(status, str):
            query += ' AND status = "%s"' % status
        if isinstance(issue_type, (tuple, list)):
            types = ', '.join('"%s"' % t for t in issue_type)
            query += ' AND type IN (%s)' % types
        if isinstance(issue_type, str):
            query += ' AND type = "%s"' % issue_type
        if assignee:
            query += ' AND assignee="%s"' % assignee
        if assignee:
            query += ' AND fixVersion="%s"' % release
        return self.jira.search_issues(query)
