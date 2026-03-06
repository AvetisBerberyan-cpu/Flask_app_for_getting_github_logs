import os
import requests

TOKEN = os.getenv("TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}


def get_pull_requests(state="open"):
    """
    Fetch pull requests from the boto/boto3 repository.

    Returns a list of dicts:
    [
        {"title": "Add useful stuff", "num": 56, "link": "..."},
        {"title": "Fix something", "num": 57, "link": "..."},
    ]
    """

    url = "https://api.github.com/repos/boto/boto3/pulls"
    params = {"state": state, "per_page": 30}

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code != 200:
        print(f"Error fetching PRs: {response.status_code} - {response.text}")
        return []

    prs_data = response.json()

    pull_requests = []
    for pr in prs_data:
        pull_requests.append(
            {
                "title": pr.get("title"),
                "num": pr.get("number"),
                "link": pr.get("html_url"),
                "state": pr.get("state"),
            }
        )

    return pull_requests
