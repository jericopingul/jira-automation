import asyncio
from jira import JIRA

### Constants ###
# user email
user = "your@email.com"
# api key generated from JIRA from user
# https://confluence.atlassian.com/cloud/api-tokens-938839638.html
apikey = "xxxxx"
# ticket numbers to release / transition
ticket_numbers = ["JIRA-1"]
# status to transition to - to do | in progress | done ...etc
transition_status = "to do"
# version name to create (release)
version_name = "VERSION_NAME"
# text to add to release  description
version_description = "Version description"
# project key (usually ticket number prefix)
project_key = "JIRA"
# server url
server = "https://<your-domain>.atlassian.net"


def login(user, apikey):
    options = {"server": server}
    return JIRA(options, basic_auth=(user, apikey))


async def set_transition(issue_numbers, transition_name):
    for issue_number in issue_numbers:
        issue = jira.issue(issue_number)
        transition_id = jira.find_transitionid_by_name(issue, transition_name)
        jira.transition_issue(issue, transition_id)
        await asyncio.sleep(0.1)


async def create_version(name, project_key, description):
    jira.create_version(name, project_key, description)
    await asyncio.sleep(0.1)


async def version_issues(issues, version):
    for issue_number in issues:
        issue = jira.issue(issue_number)
        issue.add_field_value("fixVersions", {"name": version})
        await asyncio.sleep(0.1)


jira = login(user, apikey)
loop = asyncio.get_event_loop()
loop.run_until_complete(set_transition(ticket_numbers, transition_status))
loop.run_until_complete(create_version(version_name, project_key, version_description))
loop.run_until_complete(version_issues(ticket_numbers, version_name))
loop.close()

print(jira.projects())
print(jira.project_versions(project_key))
