# CloudBeBot

**Cloudbet Pulse Alpha Engine**

CloudBeBot treats sportsbook odds as prices. It scans Cloudbet markets, compares them with external reference markets, estimates fair value, ranks positive-EV opportunities, and surfaces Pulse-ready picks with strict risk controls.

## V1 Goal

```text
Cloudbet Feed + Reference Odds
            ↓
      Market Normalizer
            ↓
      Fair Value Engine
            ↓
        +EV Scanner
            ↓
       Pulse Score
            ↓
      Mobile Approval
            ↓
       Cloudbet Pulse
            ↓
     ROI + CLV + Tails
```

V1 is **Pulse-assisted**, not blind auto-betting.

## Stack

- Python 3.12 / FastAPI
- Supabase PostgreSQL
- Redis
- Fly.io
- Next.js dashboard later
- Cloudbet Feed API v2
- Cloudbet Trading API v4

## Trading Modes

- `SHADOW` — record signals only
- `PULSE_ASSISTED` — generate picks for manual Pulse placement
- `PLAY_EUR` — test Cloudbet execution lifecycle
- `API_LIVE` — disabled until explicitly validated

## Initial Strategy

- Prematch only
- Straight bets only
- Soccer / basketball / tennis
- Primary liquid markets
- External no-vig consensus
- Conservative EV
- Steam / stale-price detection
- Pulse Score
- CLV tracking

The default action is **NO TRADE**. A pick must pass market integrity, freshness, liquidity, fair-value and risk checks.

## Deployment

```text
Fly.io
├── API
├── Cloudbet collector
├── Signal worker
├── Execution/reconciliation workers later
└── Redis coordination

Supabase
└── PostgreSQL
```

See `docs/ARCHITECTURE.md`, `docs/RISK.md`, and `docs/ROADMAP.md`.
