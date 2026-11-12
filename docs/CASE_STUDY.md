# On Call Rotation Lab walkthrough

## Business problem

A local simulator for PagerDuty-style primary and secondary escalation using synthetic responders. It makes shift boundaries and acknowledgment timing explicit.

## Reproduce the workflow

Run `python3 rotation.py --incident 59 --timeout 5 --ack 65` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
059  page         Alex
064  escalate     Sam
065  acknowledge  Sam
```

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
