from typing import Any
from .utils import normalize_trajectory, get_action, get_match_ratio, clamp

def grade(trajectory: Any) -> float:
    steps = normalize_trajectory(trajectory)
    if not steps:
        return 0.05

    successes = 0.0
    for step in steps:
        if get_action(step) == "APPLY" and (get_match_ratio(step) or 0.0) >= 0.7:
            successes += 1.0

    return clamp(0.05 + 0.90 * (successes / max(len(steps), 1)))
