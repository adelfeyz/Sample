from app.pr_analyzer import analyze_prs


def test_overall_summary():
    prs = [
        {"developer": "Alice", "team": "Payments", "ai_assisted": True},
        {"developer": "Bob", "team": "Payments", "ai_assisted": False},
        {"developer": "Carol", "team": "Risk", "ai_assisted": True},
    ]

    result = analyze_prs(prs)

    assert result["overall"]["total_prs"] == 3
    assert result["overall"]["ai_assisted_prs"] == 2
    assert result["overall"]["non_ai_assisted_prs"] == 1
    assert result["overall"]["ai_usage_rate"] == 0.67