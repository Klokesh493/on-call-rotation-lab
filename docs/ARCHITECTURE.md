# On Call Rotation Lab architecture

A local simulator for PagerDuty-style primary and secondary escalation using synthetic responders. It makes shift boundaries and acknowledgment timing explicit.

```mermaid
flowchart LR
    A["Shift coverage, incident time, and timeout"]
    B["Validate shifts and pick primary responder"]
    C{"Acknowledged by deadline?"}
    D["Record acknowledgment"]
    E["Escalate to secondary"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
