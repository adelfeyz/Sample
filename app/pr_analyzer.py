def analyze_prs(prs):
    total_prs = len(prs)
    ai_assisted_prs = sum(1 for pr in prs if pr.get("ai_assisted") is True)
    non_ai_assisted_prs = total_prs - ai_assisted_prs

    return {
        "overall": {
            "total_prs": total_prs,
            "ai_assisted_prs": ai_assisted_prs,
            "non_ai_assisted_prs": non_ai_assisted_prs,
            "ai_usage_rate": round(ai_assisted_prs / total_prs, 2) if total_prs else 0
            #"ai_usage_rate": 999
        }
    }