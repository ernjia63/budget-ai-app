import requests


APP_ID = "YOUR_ADZUNA_APP_ID"
APP_KEY = "YOUR_ADZUNA_APP_KEY"


def search_student_jobs(location):
    """
    Find nearby student part-time jobs.
    """

    url = (
        "https://api.adzuna.com/v1/api/jobs/"
        "my/search/1"
    )

    parameters = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 5,
        "what": "part time student",
        "where": location
    }

    response = requests.get(
        url,
        params=parameters
    )

    data = response.json()

    return data.get("results", [])