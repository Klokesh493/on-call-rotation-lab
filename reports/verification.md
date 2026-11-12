# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 rotation.py --incident 59 --timeout 5 --ack 65
059  page         Alex
064  escalate     Sam
065  acknowledge  Sam
test_ack_at_deadline_suppresses_escalation (test_rotation.RotationTests) ... ok
test_late_ack_uses_incident_shift (test_rotation.RotationTests) ... ok
test_missing_coverage_is_explicit (test_rotation.RotationTests) ... ok
test_new_incident_at_handoff_uses_next_shift (test_rotation.RotationTests) ... ok
test_overlapping_shifts_are_rejected (test_rotation.RotationTests) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
````
