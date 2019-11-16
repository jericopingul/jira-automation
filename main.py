import asyncio
from jira import JIRA


def login(user, apikey):
    server = "https://<name>.atlassian.net"
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


user = "user-email"
apikey = "apikey"

jira = login(user, apikey)

loop = asyncio.get_event_loop()
loop.run_until_complete(set_transition(["TSP-1", "TSP-2"], "done"))
loop.run_until_complete(create_version("RELEASE_2", "TSP", "Test Release"))
loop.run_until_complete(version_issues(["TSP-1", "TSP-2"], "RELEASE_2"))
loop.close()

print(jira.projects())
print(jira.project_versions("TSP"))
