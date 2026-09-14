# Orka's Tarot Pro — Streamlit Edition

A faithful **Streamlit port of the original Android tarot application**
(`com.orka.taropro`, v1.0.1). The recovered Android sources contained the
manifest, three activities (`CelticCrossActivity`, `MirrorActivity`,
`CardActivity`) and the 3D flip animation utilities; this project
reconstructs the whole application from that skeleton and ports it to a
multi-file Python web app.

## Features

- **Five spreads** — One Card, Three Card, Horseshoe (7 cards),
  Celtic Cross (10 cards, as in `CelticCrossActivity`) and Mirror
  (11 cards, honouring `MirrorActivity`'s 11-row layout).
- **Full 78-card deck** — 22 Major Arcana + 56 Minor Arcana, each with
  keywords, meaning and distinct **upright / reversed** interpretations
  (the `Card.getReading()` / `setDirect()` data model, ported).
- **Shared deck widget** — one generic shuffle panel (`Shuffle & deal`,
  `Reshuffle`, `Turn all`, `Clear`) used by every spread, as in the
  Android app's single shared `CardDeck`.
- **Tap-to-flip interaction** — cards start face down on the shared
  burgundy back and are turned with numbered buttons; the reveal plays a
  CSS `rotateY(-90deg → 0deg)` flip over 500 ms, ported from
  `Flip3dAnimation` / `SwapViews`.
- **Card detail view** — the `CardActivity` screen: card, name,
  *Card Meaning*, *Upright Reading*, *Reverse Reading*.
- **Full reading interpretation** — the `ReadingActivity` role: a
  position-by-position summary plus a synthesis of Major Arcana weight
  and reversals once the spread is complete.
- **Deck Browser** — browse and filter all 78 cards, inspect any card.
- **Elegant parchment theme** — cream ground, burgundy & bronze accents,
  Cinzel + EB Garamond typography.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Screenshots of the running app live in [`screenshots/`](screenshots/).

## Project structure

```
app.py                     entry point: theme, sidebar menu, st.navigation routing
styles.py                  parchment theme CSS (injected globally)
state.py                   session state + the onResume() reading-type port
domain/
  card.py                  Card (card_id → card_%02d, name, meaning, readings)
  deck.py                  CardDeck.shuffle() / deal() — the shared deck
  reading.py               CardReadingType enum, Reading, SpreadCard
data/
  major_arcana.py          22 trumps (ids 1–22)
  suits_wands.py           Wands 23–36   (fire)
  suits_cups.py            Cups 37–50    (water)
  suits_swords.py          Swords 51–64  (air)
  suits_pentacles.py       Pentacles 65–78 (earth)
  tarot_data.py            deck assembly (validates 78 unique ids)
spreads/
  base.py                  SpreadPosition / Spread definitions + registry
components/
  card_view.py             shared card back + parchment faces + detail view
  shuffle_panel.py         the generic shuffle/deal widget for all spreads
  spread_layout.py         spread boards (single/row/arc/cross/mirror) + flips
  spread_flow.py           shared page flow for the five spread pages
  summary.py               full reading interpretation generator
views/
  home.py                  TaroQuestionsActivity (launcher) port
  one_card.py … mirror.py  one thin page per spread activity
  deck_browse.py           DeckBrowseActivity port
  about.py                 help + Android→Streamlit mapping
```

## Android → Streamlit mapping

| Android activity | Streamlit page |
| --- | --- |
| `TaroQuestionsActivity` (launcher) | Ask the Cards |
| `OneCardActivity` | One Card |
| `ThreeCardActivity` | Three Card |
| `HorseshoeActivity` | Horseshoe |
| `CelticCrossActivity` | Celtic Cross |
| `MirrorActivity` | Mirror |
| `CardActivity` | Card detail panels / Deck Browser |
| `DeckBrowseActivity` | Deck Browser |
| `ReadingActivity` | Full Reading Interpretation section |
| `Flip3dAnimation` / `SwapViews` | CSS `flipIn` keyframes |
| `AdActivity` / `TapForTapActivity` | intentionally not ported |

## Notes

- Card ids keep the original `card_%02d` numbering (1 = The Fool … 78 =
  King of Pentacles), so real card images can be dropped in later by
  editing `components/card_view.py` alone.
- Entering a different spread clears the current reading and reshuffles,
  exactly mirroring the `onResume()` logic of the original activities.
- Half of the dealt cards may appear reversed (the deck honours both
  polarities, as the original's upright/reverse readings imply).
