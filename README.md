# The World in One Page — 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/canglvam/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/canglvam/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026, for the
[make.fun "Sum up 19 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261119).

A newspaper front page, drawn in code: the masthead names the date, the lead
story is GTA VI's worldwide launch, and six cards cover the day across
regions and fields — the Xi–Putin–Trump summit in Shenzhen, oil tankers
ablaze off the Strait of Hormuz, Anthropic's record $81.3bn IPO, the World
Court ruling on the Rohingya case, Voyager 1 reaching one light-day, and the
ground operation in central Gaza — with an "Also today" strip for the rest.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` — the
1024×1024 image, drawn at build time with Pillow — to `/output/entry.png`
(or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader). No network, fully
deterministic: every run writes the same bytes.
