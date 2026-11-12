# On Call Rotation Lab architecture

A local simulator for PagerDuty-style primary and secondary escalation using synthetic responders. It makes shift boundaries and acknowledgment timing explicit.

```mermaid
flowchart LR
    N0["CLI arguments"]
    N1["rotation.py"]
    N2["Select shift coverage at the event boundary and simulate escalation at the deadline."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
