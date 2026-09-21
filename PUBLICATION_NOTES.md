# Publication notes


## Prepared split


The Drive staging area is divided into:


- `00_REPO`: files intended for the Git repository
- `10_RELEASE_ASSETS`: large immutable packages intended for GitHub Releases and/or persistent archival storage
- `20_ZENODO`: former Zenodo deposit staging; retained internally but not part of the current publication workflow
- `90_SCAN_REPORTS`: security/integrity scan documentation


## Security scan


Publication candidates were downloaded from Drive and recursively inspected.


Scope completed so far:
- 28 standalone ZIP archives
- one large E-004 implementation freeze reconstructed from three split parts and scanned as the original ZIP
- two Gzip JSONL runs


Checks included common API/token/private-key signatures, generic password/secret assignments, e-mail addresses, user-specific Windows/macOS/Linux absolute paths, suspicious credential filenames, archive path traversal and nested ZIPs.


Result: no credential candidates, e-mail addresses, user-specific personal paths or suspicious credential filenames were detected. One reproducibility archive contains the execution-environment path `/home/oai/.cache/pip` in `offline_install_test.log`; it is retained because changing the historical freeze would invalidate its hash.


The three deeply nested E-003 packages were rescanned to nesting depth 8 with no remaining scan issues.


The reconstructed E-004 implementation freeze matches its manifest SHA-256:
`94333bf132a3fb2b97b694f8b2b197bad29341a8724e777f3ccf79d48d177f6b`.


The two preserved Social-Memory JSONL.GZ files are byte-identical:
`cd0063f95076b12e75997ed42e01145e3e4d8c68070989cb59c0fb6ad137f118`.


## Scan limitation


This is a strong heuristic publication scan, not a formal security audit. Third-party CPython/Numba wheelhouse binaries are treated as external dependencies, not authored project source. Before the final public push, run one final secret scanner over the exact exported repository tree.


## Exclusions


Do not publish in Git history:
- `.venv`
- `__pycache__`
- closed holdout content or unlock material
- redundant backup ZIPs
- third-party wheel binaries


Large research packages may be published as release or external archival assets.


## Provenance wording


Historical “external review” documents used a separate model as a checking instance. Public-facing documentation should say “model-based external check/review” where necessary to avoid implying human peer review.


Files marked `REKONSTRUIERT` retain that marker.