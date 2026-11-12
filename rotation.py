"""Simulate PagerDuty-style primary and secondary escalation offline."""
import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Shift:
    start: int
    end: int
    primary: str
    secondary: str


def simulate(shifts, incident, timeout, acknowledgment=None):
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    if acknowledgment is not None and acknowledgment < incident:
        raise ValueError("acknowledgment precedes the incident")
    ordered = sorted(shifts, key=lambda shift: shift.start)
    for shift in ordered:
        if shift.start >= shift.end or shift.primary == shift.secondary:
            raise ValueError("a shift needs a positive duration and distinct responders")
    if any(left.end > right.start for left, right in zip(ordered, ordered[1:])):
        raise ValueError("shifts overlap")
    shift = next((item for item in ordered if item.start <= incident < item.end), None)
    if shift is None:
        raise ValueError("no on-call coverage at incident start")
    events = [(incident, "page", shift.primary)]
    deadline = incident + timeout
    if acknowledgment is None or acknowledgment > deadline:
        events.append((deadline, "escalate", shift.secondary))
    if acknowledgment is not None:
        responder = shift.primary if acknowledgment <= deadline else shift.secondary
        events.append((acknowledgment, "acknowledge", responder))
    return events


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--incident", type=int, default=55)
    parser.add_argument("--ack", type=int)
    parser.add_argument("--timeout", type=int, default=5)
    args = parser.parse_args()
    shifts = [Shift(0, 60, "Alex", "Sam"), Shift(60, 120, "Sam", "Jo")]
    try:
        events = simulate(shifts, args.incident, args.timeout, args.ack)
    except ValueError as exc:
        parser.error(str(exc))
    for minute, action, person in events:
        print(f"{minute:03d}  {action:12} {person}")


if __name__ == "__main__":
    main()
