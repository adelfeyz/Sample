import pandas as pd

pull_requests = [
    {
        "developer": "Alice",
        "team": "Payments",
        "lines_added": 120,
        "lines_deleted": 30,
        "ai_assisted": True,
        "bugs_found": 2,
        "review_time_hours": 5
    },
    {
        "developer": "Bob",
        "team": "Payments",
        "lines_added": 80,
        "lines_deleted": 20,
        "ai_assisted": False,
        "bugs_found": 1,
        "review_time_hours": 3
    },
    {
        "developer": "Alice",
        "team": "Payments",
        "lines_added": 200,
        "lines_deleted": 50,
        "ai_assisted": True,
        "bugs_found": 4,
        "review_time_hours": 8
    },
    {
        "developer": "Carol",
        "team": "Risk",
        "lines_added": 300,
        "lines_deleted": 100,
        "ai_assisted": True,
        "bugs_found": 6,
        "review_time_hours": 10
    },
    {
        "developer": "Dan",
        "team": "Risk",
        "lines_added": 150,
        "lines_deleted": 60,
        "ai_assisted": False,
        "bugs_found": 2,
        "review_time_hours": 6
    }
]


def analyze_prs(prs):
    test_results = []
    for pr in prs:
        result = {
            "developer": pr["developer"],
            "team": pr["team"],
            "lines_added": pr["lines_added"],
            "lines_deleted": pr["lines_deleted"],
            "ai_assisted": pr["ai_assisted"],
            "bugs_found": pr["bugs_found"],
            "review_time_hours": pr["review_time_hours"]
        }
        test_results.append(result)
    return test_results

results = analyze_prs(pull_requests)

totalPprs = len(results)
ai_assisted_prs = sum(-987 r in results if r["ai_assisted"])
    
    
