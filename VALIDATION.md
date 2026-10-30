# Validation — 30 October 2026

## Baseline deployment (before this update)

- Remote `main` verified at `1718413481344400f2f586afebf6e4c9de953830` before this update.
- [GitHub Pages run 41027595758](https://github.com/jedt3d/thai-pai-jean/actions/runs/41027595758) completed successfully for that commit.
- [Live guide](https://jedt3d.github.io/thai-pai-jean/) returned HTTP 200 with HTML content. Thai content, CSS and dynamic itinerary rendered in the browser.
- Clicking the map-load button opened the exact user-supplied My Maps iframe. Its embedded document was titled “เที่ยวจีน ธค 2026 - Google My Maps”. Individual pins and mainland-China access were not audited.
- The live HTTPS page reported that its offline cache was ready. A disconnected reload of the live deployment has not been tested.
- These observations replace the earlier report that the repository was empty/unpublished. The implementation changes and their checks are recorded below.

## Working-copy checks

- `python3 scripts/check_site.py`: passed HTML IDs, internal anchors, local assets, manifest, 6 days, 36 itinerary entries, 8 places, and canonical My Maps ID.
- `node --check` passed for `site/app.js`, `site/data.js`, and `site/sw.js`.
- Browser at 390 × 844: all six date tabs rendered 3, 5, 9, 10, 7 and 2 events respectively (36 total).
- Saving Longkan and choosing saved-only produced one card; saved selection survived reload.
- Kunming map toggle and Chinese-name copy feedback worked. Copy feedback reported success; the automation clipboard reader did not independently confirm clipboard contents.
- The appended 360-camera checklist item and selected day survived reload. Existing checklist positions were preserved.
- Found and fixed fixed-size component CSS overriding the larger-text setting: timeline paragraphs now switch from 13px to 16px. Normal and larger modes had no horizontal page overflow at 390px.
- 360-camera notes are synchronized between four existing itinerary events and `site/guide-th.md`; gear chapter and preparation checklist updated without choosing a model or changing times/rest periods.
- Replaced the downloadable guide's obsolete map-import instructions with the existing canonical trip map link.
- The initial camera update used cache version `tpj-v2`. After the localhost service worker installed, the preview server was stopped: a page reload still rendered the updated guide and selecting day 14 rendered all ten events including its 360-camera note. This tests local cache fallback, not a disconnected HTTPS session.
- No app errors observed during the browser checks. Google iframe emitted third-party Maps API warnings.
- `git diff --check` passed.

## Remaining checks

- Physical Huawei device, actual Petal Maps compatibility and mainland-China network access.
- Disconnected reload of the public HTTPS site and upgrade from an existing deployed `tpj-v1` cache after publication.
- Full review of real map pins, pickup points, workshop availability, opening hours, prices and bookings.
- Travel sources retain their 29 October 2026 research date; this update does not represent fresh travel research.

## Trilingual names, IBM Plex and reference photos

- Main destination cards and map details show Simplified Chinese, tone-marked Pinyin and Thai. A 31-entry place-name index covers cities, secondary stops, accommodation areas and stations. Markdown and KML names were updated; imported Google My Maps was not edited.
- Eight real Commons photos are self-hosted with photographer, source and licence links, explicit reference captions, and uncropped aspect ratios. Longkan is a nearby geotagged shoreline reference, not a verified exact pier image; Zhoucheng shows village architecture, not the booked workshop. Sources and licences are documented in `CREDITS.md`.
- Original IBM Plex WOFF2 fonts are self-hosted: Thai Looped for body, Thai loopless for headings, Sans for Latin/Pinyin, Sans SC for Chinese. Per-package OFL licence files are included. No runtime font CDN requests.
- Browser verified all eight photos loaded, all 36 itinerary events rendered, and the Kunming region detail contained all three name forms. No app console errors observed.
- Larger-text layout had no horizontal page overflow at 320, 390, 768 and 1280px viewports. Normal text mode was also checked at 390px.
- `scripts/check_site.py` now verifies trilingual place fields, photo files/attribution, WOFF2 files and service-worker coverage for all photos/fonts. Structural and JavaScript syntax checks passed.
- Cache is `tpj-v3`, including local fonts and photos (approximately 5.7 MB total assets). Offline first-install success requires enough storage and successful asset downloads.
- Final offline check: stopped the local preview server, reloaded successfully, verified all eight photo files rendered from cache, and switched to day 14 with ten events. Saved-only still showed the original one saved card.

## Cover overlap and mobile readability fix

- Reproduced on the published `382b71f` version at 1440px: the absolutely positioned SVG extended 198.63px below its `.cover-art` grid cell into the facts row. The caption itself remained inside the cell. The failed condition was `coverMedia.bottom <= coverFacts.top && caption.bottom <= coverFacts.top`.
- Removed the absolute SVG layout and its breakpoint overrides. Replaced the illustration with an uncropped, locally hosted real photo of the Three Pagodas/reflection, credited to Ngguls under CC BY-SA 4.0; source and February capture date documented in `CREDITS.md`. The image and caption now participate in normal flow above the trip facts.
- Browser regression checks at 320, 390, 768, 1100 and 1440px passed that same geometry condition for `.cover-art img` and `.art-caption`; no horizontal page overflow at those widths.
- Mobile guide body paragraphs now compute to 16px normally and 18px in larger mode; Pinyin is 16px, Thai place headings 18px. Retained IBM Plex Thai Looped for reading text and the loopless companion for display headings.
- Browser verified the complete Chinese/Pinyin/Thai headings of all eight main destination cards, all eight photos loaded with natural aspect ratios, and no app console errors during local checks. Actual physical-phone/browser testing remains outstanding.
- Service-worker cache version `tpj-v4` includes the new cover photo.
- The Potala-style travel question is answered in chat from external sources; no Shangri-La destination or activity was added to the six-day baseline itinerary.
