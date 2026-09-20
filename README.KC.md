# ExpressLRS 3.6.4 — KC (Korea) fork

This branch (`KC-3.6.4`) is **official [ExpressLRS](https://github.com/ExpressLRS/ExpressLRS) v3.6.4** with a
minimal patch that restricts the 2.4 GHz FHSS band to the range permitted for KC-certified
operation in Korea. It is maintained by [falconshop](https://www.falconshop.co.kr) so that Korean
users of newer receivers (which the original KC-domain branch, based on 3.4.0, never added) can run a
current ExpressLRS release while staying within the KC 2.4 GHz allocation.

It is published to satisfy the **GPLv3** obligation to provide the corresponding source for the KC
firmware binaries distributed at
the falconshop ELRS updater tool and its releases
(<https://github.com/falconshop/elrs-updater>).

## What changed vs. upstream 3.6.4

Only two files differ from the official `3.6.4` tag:

1. **`src/lib/FHSS/FHSS.cpp`** — the 2.4 GHz domain is narrowed from the ISM band
   (2400.4–2479.4 MHz, 80 channels, `"ISM2G4"`) to the KC range
   (**2420.4–2479.4 MHz, 60 channels, `"KC2G4"`**), for both the SX128x table and the
   LR1121 dual-band 2.4 side. This matches the hopping of a 2.4-only KC transmitter, so a KC
   receiver binds and hops only on the KC-permitted channels.

2. **`src/python/elrs_helpers.py`** — the reported version string is set to **`3.6.4-KC`** so the
   firmware clearly identifies itself as this KC build.

Nothing else (protocol, targets, features) is modified. `src/hardware` (the
[ExpressLRS/targets](https://github.com/ExpressLRS/targets) repo) is not part of this tree and is
fetched separately at build time, exactly as upstream does.

## Building

Build exactly as upstream ExpressLRS (PlatformIO). See the main
[README.md](README.md) and the [ExpressLRS docs](https://www.expresslrs.org/).

## License

GPLv3, inherited from ExpressLRS. See [LICENSE](LICENSE).
Upstream: <https://github.com/ExpressLRS/ExpressLRS/tree/3.6.4>
