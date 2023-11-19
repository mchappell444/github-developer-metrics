import os
import datetime
import csv
from github import Github

# GitHub Configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPOSITORY = "mchappell444/github-basics"
START_DATE = datetime.datetime(2023, 9, 1)  # Example date
END_DATE = datetime.datetime(2023, 9, 23)  # Example date

# CSV Configuration
CSV_FILENAME = "github_metrics.csv"

# Initialize Github instance
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPOSITORY)

# Fetch Pull Requests
pull_requests = repo.get_pulls(state="all")

# Prepare data for CSV
data = []
headers = [
    "Username",
    "Created At",
    "Merged At",
    "Number of Comments",
    "Additions",
    "Deletions",
    "Review Requests",
]
data.append(headers)

for pr in pull_requests:
    created_at = pr.created_at
    if START_DATE <= created_at <= END_DATE:
        data.append(
            [
                pr.user.login,
                pr.created_at,
                pr.merged_at,
                len(pr.get_comments()),
                pr.additions,
                pr.deletions,
                len(pr.get_review_requests()),
            ]
        )

# Export data to CSV
with open(CSV_FILENAME, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print(f"Data exported successfully to {CSV_FILENAME}!")
