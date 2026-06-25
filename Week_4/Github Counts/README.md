# GitHub Contribution Calendar Exporter

A small Python script that fetches a GitHub user's contribution calendar using GitHub's official GraphQL API.

The script saves the result as JSON only:

```txt
<username>_github_contributions.json
```

Example:

```powershell
python .\api.py RAiU14
```

---

## What this project does

This project gets contribution calendar data from GitHub, similar to the green contribution graph shown on a GitHub profile.

For each day, it collects:

- Date
- Weekday
- Contribution count
- Contribution level
- GitHub heatmap color

It does **not** scrape the GitHub website.

Instead, it uses GitHub's official GraphQL API.

---

## What is GraphQL?

GraphQL is a query language for APIs.

In a normal REST API, you usually call a fixed endpoint and receive whatever data that endpoint returns.

In GraphQL, you send a query and ask for only the exact fields you want.

For this project, we only ask GitHub for contribution calendar fields such as:

```txt
date
weekday
contributionCount
contributionLevel
color
```

This makes the response smaller and more direct because we are not asking for unnecessary profile or repository data.

---

## Why GraphQL is used here

GitHub's contribution calendar data is available through GitHub's GraphQL API.

The API endpoint is:

```txt
https://api.github.com/graphql
```

GitHub's GraphQL API accepts a `POST` request with a JSON body containing a `query`.

In this project, Python sends this body:

```python
{
    "query": QUERY,
    "variables": {
        "login": username
    }
}
```

The `QUERY` contains the GraphQL command.

The `variables` section passes the GitHub username dynamically.

---

## Official documentation proof

This project is based on GitHub's official documentation.

Official documentation used:

- GitHub GraphQL API documentation:  
  https://docs.github.com/en/graphql

- Forming GitHub GraphQL API calls:  
  https://docs.github.com/en/graphql/guides/forming-calls-with-graphql

- GitHub Users GraphQL reference:  
  https://docs.github.com/en/graphql/reference/users

- GitHub GraphQL rate limits:  
  https://docs.github.com/en/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api

- GraphQL query basics:  
  https://graphql.org/learn/queries/

---

## Where the query came from

The query was built from GitHub's official GraphQL Users reference.

The documented path is:

```txt
user(login: $login)
└── contributionsCollection
    └── contributionCalendar
        ├── totalContributions
        └── weeks
            └── contributionDays
                ├── date
                ├── weekday
                ├── contributionCount
                ├── contributionLevel
                └── color
```

This means:

1. Look up a GitHub user by login.
2. Get that user's contribution collection.
3. Get the contribution calendar.
4. Get the total contribution count.
5. Get the calendar weeks.
6. Get each contribution day inside those weeks.

---

## GraphQL query used

```graphql
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            weekday
            contributionCount
            contributionLevel
            color
          }
        }
      }
    }
  }
}
```

---

## Query variables

The query uses a variable instead of hard-coding the username.

Example variable:

```json
{
  "login": "RAiU14"
}
```

In the GraphQL query:

```graphql
query($login: String!)
```

This means the query expects a required string variable called `login`.

Then this line uses that variable:

```graphql
user(login: $login)
```

So when the script is run like this:

```powershell
python .\api.py RAiU14
```

Python sends:

```json
{
  "login": "RAiU14"
}
```

---

## Explanation of each query field

### `query($login: String!)`

Starts a GraphQL query.

`$login` is a variable.

`String` means the value must be text.

`!` means the value is required.

---

### `user(login: $login)`

Looks up a GitHub user by username.

Example:

```txt
RAiU14
```

---

### `contributionsCollection`

Gets the user's contribution activity.

This can include commits, pull requests, issues, and other contribution activity.

---

### `contributionCalendar`

Gets the calendar-style contribution graph data.

This is the data used to build the contribution heatmap.

---

### `totalContributions`

Gets the total number of contributions in the calendar.

Example output:

```txt
113 contributions in the last year
```

---

### `weeks`

GitHub stores the contribution calendar in weekly groups.

That is why the script has to loop through weeks first.

---

### `contributionDays`

Each week contains multiple contribution days.

The script flattens these days into one simple list.

---

### `date`

The calendar date.

Example:

```txt
2026-05-22
```

---

### `weekday`

The day of the week as a number.

GitHub returns this as an integer.

---

### `contributionCount`

The number of contributions made on that date.

Example:

```json
"contributionCount": 4
```

---

### `contributionLevel`

GitHub's contribution intensity level for that day.

Possible values include:

```txt
NONE
FIRST_QUARTILE
SECOND_QUARTILE
THIRD_QUARTILE
FOURTH_QUARTILE
```

---

### `color`

The hex color GitHub uses for that contribution square.

Example:

```txt
#216e39
```

---

## How the Python script works

The script performs these steps:

1. Loads environment variables from `.env`.
2. Reads the GitHub username from the command line.
3. Reads the GitHub API token from `GITHUB_TOKEN`.
4. Sends the GraphQL query to GitHub.
5. Receives contribution calendar data.
6. Loops through the weekly calendar data.
7. Extracts all daily contribution records.
8. Saves the final result as JSON.

---

## Why the script loops through weeks

GitHub returns the contribution calendar in this structure:

```txt
weeks
└── contributionDays
```

That means the response is grouped like this:

```json
{
  "weeks": [
    {
      "contributionDays": [
        {
          "date": "2026-05-22",
          "contributionCount": 4
        }
      ]
    }
  ]
}
```

The script converts that nested structure into a simpler list:

```python
days = []

for week in calendar["weeks"]:
    days.extend(week["contributionDays"])
```

This makes the JSON output easier to use later.

---

## Output JSON structure

Example output file:

```txt
RAiU14_github_contributions.json
```

Example JSON shape:

```json
{
  "username": "RAiU14",
  "totalContributions": 113,
  "days": [
    {
      "date": "2026-05-22",
      "weekday": 5,
      "contributionCount": 4,
      "contributionLevel": "SECOND_QUARTILE",
      "color": "#216e39"
    }
  ],
  "source": {
    "api": "GitHub GraphQL API",
    "endpoint": "https://api.github.com/graphql",
    "documentation": [
      "https://docs.github.com/en/graphql",
      "https://docs.github.com/en/graphql/guides/forming-calls-with-graphql",
      "https://docs.github.com/en/graphql/reference/users"
    ]
  }
}
```

---

## Project structure

```txt
Week_4/
├── api.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Requirements

Install dependencies using:

```powershell
python -m pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```txt
requests
python-dotenv
truststore
```

---

## Environment variables

Create a `.env` file in the same directory as `api.py`.

```env
GITHUB_TOKEN=github_pat_your_token_here
```

Do not upload `.env` to GitHub.

---

## Creating a GitHub API token

Use a fine-grained personal access token.

Steps:

1. Go to GitHub.
2. Click your profile picture.
3. Open **Settings**.
4. Go to **Developer settings**.
5. Go to **Personal access tokens**.
6. Choose **Fine-grained tokens**.
7. Click **Generate new token**.
8. Give it a name, such as:

```txt
github-contribution-exporter
```

9. Set an expiration date.
10. Select yourself as the resource owner.
11. Under **Repository access**, choose:

```txt
Public repositories
```

12. Leave account permissions empty.
13. Generate the token.
14. Copy it into `.env`.

For public contribution calendar data, no write permission is needed.

---

## API cost and pricing

Expected cost for running this script:

```txt
$0
```

GitHub does not charge this script per API request.

Usage is controlled by GitHub API rate limits.

For normal personal access token usage, GitHub's GraphQL API uses a point-based rate limit.

The usual user limit is:

```txt
5,000 points per hour per user
```

This script sends one GraphQL request per username, so normal usage should stay far below the limit.

---

## Optional rate limit query

GitHub allows requesting rate limit information in a GraphQL query.

Example:

```graphql
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            weekday
            contributionCount
            contributionLevel
            color
          }
        }
      }
    }
  }

  rateLimit {
    cost
    remaining
    resetAt
  }
}
```

This returns:

- `cost`: how many GraphQL points the query used
- `remaining`: how many points are left
- `resetAt`: when the limit resets

---

## SSL certificate issue on Windows

During setup, this error happened:

```txt
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
```

This was not a GitHub token issue.

It happened because Python could not verify the HTTPS certificate chain.

The fix was to install `truststore`:

```powershell
python -m pip install truststore
```

Then this code was added at the very top of `api.py`, before importing `requests`:

```python
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass
```

This lets Python use the operating system's certificate store.

---

## Security notes

Never hard-code your GitHub token in `api.py`.

Good:

```python
token = os.getenv("GITHUB_TOKEN")
```

Bad:

```python
token = "github_pat_real_token_here"
```

Do not commit `.env`.

Recommended `.gitignore`:

```gitignore
.env
*_github_contributions.json
__pycache__/
```

---

## Troubleshooting

### `Set GITHUB_TOKEN first in your .env file.`

The `.env` file is missing or does not contain:

```env
GITHUB_TOKEN=your_token_here
```

---

### `401 Unauthorized`

The token is invalid, expired, missing, or copied incorrectly.

Create a new token and update `.env`.

---

### `GitHub user not found`

The username may be wrong.

Check the GitHub profile manually:

```txt
https://github.com/USERNAME
```

---

### SSL certificate error

Install `truststore`:

```powershell
python -m pip install truststore
```

Make sure this code is at the top of `api.py`:

```python
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass
```

Do not permanently use:

```python
verify=False
```

That disables SSL verification and is not safe for real usage.

---

## Final notes

This project uses the official GitHub GraphQL API.

It does not scrape HTML.

It only saves JSON output.

It uses a GitHub token stored in `.env`.

It costs `$0` for normal personal usage and is limited by GitHub's API rate limits.

NOTE: I used AI to type the complete thing faster. 
> Helps me save some time while I focus on learning programming.