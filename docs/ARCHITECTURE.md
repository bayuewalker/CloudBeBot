# CloudBeBot Architecture

## Primary Flow

```text
Cloudbet Feed ─────────────┐
                           ├─> Event / Market Normalizer
Reference Odds ────────────┘
                                  ↓
                           Fair Value Engine
                                  ↓
                              EV Scanner
                                  ↓
                          Steam / Stale Check
                                  ↓
                              Pulse Score
                                  ↓
                              Risk Guard
                                  ↓
                         PULSE_ASSISTED Queue
                                  ↓
                         Mobile user approval
                                  ↓
                            Cloudbet Pulse
```

## Design Principles

1. Scanner and executor are separate.
2. A market must map exactly before it becomes actionable.
3. Fair probability comes from no-vig external consensus, not one bookmaker.
4. Conservative EV is used for decisions.
5. Default action is NO TRADE.
6. Cloudbet API credentials stay server-side.
7. Future order intents must be idempotent and auditable.
8. Pulse eligibility of API-placed bets must be validated before API_LIVE.
