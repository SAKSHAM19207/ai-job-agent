from typing import Any
from .utils import normalize_trajectory, get_action, get_match_ratio, clamp

def grade(trajectory: Any) -> float:
    steps = normalize_trajectory(trajectory)
    if not steps:
        return 0.05

    successes = 0.0
    optimized = False

    for step in steps:
        action = get_action(step)
        match_ratio = get_match_ratio(step) or 0.0

        if 0.5 <= match_ratio < 0.7 and action == "OPTIMIZE_RESUME":
            optimized = True

        if action == "APPLY" and optimized and match_ratio >= 0.5:
            successes += 1.0
            optimized = False

        if action == "SKIP":
            optimized = False

    return clamp(0.05 + 0.90 * (successes / max(len(steps), 1)))
