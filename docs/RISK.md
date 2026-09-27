# Risk Policy

Initial bootstrap parameters:

```text
MIN_RAW_EV                     = 3.0%
MIN_ADJUSTED_EV                = 2.0%
KELLY_MULTIPLIER               = 0.20

MAX_STAKE_BANKROLL_PCT         = 1.0%
MAX_HIGH_CONF_STAKE_PCT        = 1.5%
MAX_EVENT_EXPOSURE_PCT         = 2.0%
MAX_COMPETITION_EXPOSURE_PCT   = 5.0%
MAX_SPORT_EXPOSURE_PCT         = 10.0%

DAILY_DRAWDOWN_KILL_PCT        = 4.0%
MAX_PENDING_BETS               = 5
MAX_RETRY_COUNT                = 1
MIN_REFERENCE_PROVIDERS        = 3
MIN_PULSE_SCORE                = 75
```

These are starting values, not assumed optimums.

Execution must stop on stale feeds, ambiguous mapping, failed reconciliation,
critical data-store failure, drawdown kill, or manual kill switch.
