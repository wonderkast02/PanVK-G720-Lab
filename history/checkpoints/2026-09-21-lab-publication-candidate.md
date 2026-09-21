# Checkpoint 2026-09-21 — Lab publication candidate

Status: `PREPUBLICATION_CANDIDATE`

This checkpoint records the privacy/licensing/publication preparation stage.
It does not itself make the repository public.

## Source authority

- main repository: `wonderkast02/panvk-g720-kbase-csf`
- landing `main`: `4c3ec5c88360dee2d53ffafe4fb1d86b613d21a0`
- post-GS source authority: `g720-development @ 77832026e87fc39a48d691dd5a46e9908726b0bf`
- frozen public beta source: `3549264275c9663ed73e01d652f4c0d16f21df22`
- public beta: `0.1.0-beta.1.9.4`

## Security / privacy

- LAB-A5 high-confidence secret scan: zero findings.
- technical numeric strings previously matching a phone regex are treated as
  scanner false positives only after contextual classification.
- upstream copyright/license notices are preserved.
- commit author/committer e-mail metadata is sanitized to GitHub noreply in the
  scratch public-history candidate.
- original private history is preserved separately before any future remote
  rewrite.

## Publication boundary

The real Lab remains unchanged by LAB-A6. A later, separately audited stage is
required before replacing private history or changing repository visibility.
