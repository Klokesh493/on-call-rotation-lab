# On-call rotation lab

A local simulator for PagerDuty-style primary and secondary escalation using synthetic responders. It makes shift boundaries and acknowledgment timing explicit.

## Quick start

With Python 3.10 or newer:

```sh
python3 rotation.py --incident 59 --timeout 5 --ack 65
python3 -m unittest -v
```

The example pages Alex at minute 59, escalates to Sam at 64, and records acknowledgment at 65. Incidents retain the responders assigned at incident start. An acknowledgment at the deadline suppresses escalation.

The simulator runs offline, stores no incident state, and never sends a real page. Live PagerDuty integration and time zones are outside its scope.

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.
