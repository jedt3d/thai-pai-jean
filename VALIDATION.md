# Validation — 29 October 2026

- HTML IDs, internal anchors, assets and manifest checked.
- JavaScript syntax checks passed for app.js and sw.js.
- Data validated: 6 days, 36 itinerary entries, 8 locations.
- Browser checked: day tabs, saved-location filtering, regional map toggle and My Maps iframe insertion.
- Mobile checked in a 390px iframe: content width 375px with scrollbar, no horizontal overflow. Mobile cover visually reviewed.
- My Maps iframe uses the exact user-supplied map ID. The browser did not confirm Google map content loaded; sharing/network availability needs live verification.
- Service worker could not run on the preview HTTP origin. Offline behavior remains unverified until an HTTPS deployment.
- No GitHub files were written: create_file returned GitHub 403 Resource not accessible by integration. GitHub Pages is not published.
