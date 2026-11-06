# List code and UI audit

Audited 2026-11-06. Intro-only scope; no app behavior, package, lockfile, credential or pre-existing private notebook changed.

## Actual app opened

Opened https://frankie-list-songhaifans-projects.vercel.app and inspected the default 100 Life List gallery and notebook stack. The visible current product name is Frank's Life List. The introduction retains the actual app's ruled paper, #002fa7 Klein blue, punched checkboxes, gray shell and notebook metaphor while identifying the Frankie family.

Ran the current app on a fresh local origin at port8336. Opened its real stack, moved past the cover and checked two bundled items to inspect the yellow completion marker. Created a local-only shared snapshot of bundled data with staged marks; opened its compare-review flow and selected Compare this group. Verified the real result buckets contained one both-done, one only-me, one only-theirs and97 neither-done item. No personal list contents or full share keys are published. Captures are real rendered UI; staged ticks are labelled demonstration data.

## Code examined

- `src/index.css`: actual neutral shell, Klein blue, hybrid paper, punched-hole checkbox, yellow marker treatment.
- `src/components/AppHeader.tsx`, `AppMainContent.tsx`, `CardCover.tsx`, `CardStack.tsx`, `PageCard.tsx`, `MobileGroupList.tsx`: gallery, card stack, cover/content/back cover, mobile adaptation and notebook controls.
- `src/lib/workspace-constants.ts`: ten-item content pages and bundled100-item list. Intro validates the four sample items against this source at build time.
- `src/stores/app-data-store.ts`: separate groups, duplicate-item prevention, add/remove, extra pages, completion marks and fully completed page binding.
- `src/hooks/useAppViewModel.ts`: completing a full page moves it after a short delay; sharing active group; comparing after review; destructive reset/delete confirmation.
- `src/lib/app-state-storage.ts`: browser local ID and local archive; share-query import; compressed selected-notebook snapshot, not a server-synced room.
- `src/lib/notebook-utils.ts`: AES-GCM archive with key derived from same-browser ID; URI compression for shared groups; imported group merges by item identity. Encryption is not described as a password vault; share links are not described as encrypted or authenticated.
- `src/lib/app-selectors.ts`, `ComparisonPanel.tsx`: four comparison categories based on the two booleans. Intro sample is a small unsaved adaptation of these actual rules, not a fake screenshot or embedded full React app.
- `src/components/AppOverlays.tsx`: QR uses the same generated snapshot URL; no different live collaboration service.

## Design read

An explanatory intro for people keeping and comparing personal lists. Native CSS using actual paper/blue UI tokens; variance5, motion1, density3. Shared information structure with app-specific notebook treatment. Real screenshots accompany a functional, clearly labelled rules sample. No external scientific claim or speculative security promise requires an external citation.

## Verification

- Python standard-library build generates English root and Chinese `zh/`.
- Local link/asset checker:2 pages, zero issues.
- `node --check site/demo.js` and `git diff --check` passed.
- Browser desktop/mobile and sample interaction review completed before parent review; no Lighthouse result is claimed.

- Browser-tested sample checkboxes changing all four comparison buckets and Reset restoring the staged initial marks. EN and Chinese actual390px target viewport both had scrollWidth390 / innerWidth390. Mobile screenshot visually reviewed, per-page override cleared. Hero crop checked against actual paper page. No network or local storage is used by the intro demo.
