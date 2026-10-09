# ormas-client-beta-fixtures

Small, deterministic Python/pytest fixtures used for a bounded client-side beta of the
Ormas task marketplace. Each task lives on its own branch at a fixed base commit:

| Branch | Base commit | Category |
|---|---|---|
| `task1-slugify` | `9947cff97524f5ed02ce9a6e8da33c2299bfc14e` | deterministic trivial fix |
| `task2-duration` | `465c6d4d9528a7faa397483ada60166975413f16` | small bug fix (diagnosis + implementation) |
| `task3-report-csv` | `ae619312dccb7a92e16c0402704c957e87119762` | bounded feature/change |
| `task4-config-rules` | `b8f08bdcd47c151cbd66662076585c347db73867` | verification-value (explicit multi-requirement proof) |
| `task5-wordfreq` | `8c547991e12e8a399927b6c80a1f2956d52db1c3` | direct-API comparison |

Every branch contains a tiny program, a hash-pinned `requirements.lock` (pytest only) and
`tests/test_acceptance.py`, which drives the program through `ormas_acceptance.run` and
fails on the base commit. The tests are the specification; nothing else is hidden.

No credentials, private data or production code are included.
