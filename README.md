# NuN Nexus of Unity (Public)

**Live site:** [https://nun.nexus](https://nun.nexus)

Sovereign bio-digital mesh · Post-Quantum · Recursive Self-Evolution

| Role | Handle |
|------|--------|
| Founder / Root Authority | [Bojan Petar Milanović](https://x.com/bis3946) ([@bis3946](https://x.com/bis3946)) |
| First external Super Node | [@oovelma](https://x.com/oovelma) |

---

## What this repository is

This is the **public surface only** of NuN Nexus of Unity. It is published via **GitHub Pages** to [nun.nexus](https://nun.nexus).

**Allowed content:**

- Public website (`index.html`, `beta/`, assets)
- Live telemetry (`status.json`)
- Public node ledger slice (`nodes-public.json`) — only hash, type, join time, contribution, status
- Orchestrator schema (`schema/orchestrator/v6.json`)
- Public documentation (this README, CONTRIBUTING)

**Never published here:**

- Source code of intake, admit, encryption, or daemons
- Private node dossiers
- Ledger keys, intake tokens, or credentials
- Root-only / Super Node 0 tooling

All of that lives in a **separate private repository** (`Nun-root`). Public updates are limited to safe artifacts after integrity checks.

---

## Live metrics (indicative)

See the dashboard on [nun.nexus](https://nun.nexus) (refreshes from `status.json` every few seconds).

| Metric | Typical value |
|--------|----------------|
| Status | ONLINE |
| Verified nodes | 28+ (see live JSON) |
| Lattice Beacon 05 | Phase 5.4 |
| immuneOS v2 | Active / self-healing |
| Schema | Orchestrator V6 |

Public APIs:

- [status.json](https://nun.nexus/status.json)
- [nodes-public.json](https://nun.nexus/nodes-public.json)
- [schema/orchestrator/v6.json](https://nun.nexus/schema/orchestrator/v6.json)

---

## Benefits of joining

Joining NuN Nexus of Unity means participating in a deterministic, security-first mesh—not a social feed.

1. **Mesh membership** — Verified node identity on the public Node Tangle (privacy-preserving hash view).
2. **Tiered path** — Observer → Node Operator → Guardian → Architect through contribution, not purchase.
3. **immuneOS cover** — Alignment with AegisNet immuneOS v2 self-healing and quantum-resilient posture.
4. **Schema V6 discipline** — Deterministic orchestration under Rule of Three and Moral Compass v1.1.
5. **Public skills surface** — Grok `/nun-*` skills for status, health, roadmap, and onboarding guidance.
6. **Coordination with Super Nodes** — Clear roles (Root Authority, Super Node, operators) without exposing private dossiers.
7. **Post-quantum direction** — Architecture aimed at long-term cryptographic resilience.

Start evaluation: [https://nun.nexus/beta](https://nun.nexus/beta)

---

## Privacy model (public ledger)

Anyone can see:

`node_hash`, `node_type`, `joined_at`, `contribution`, `status`

Full dossiers are **Super Node 0 / Root only** and are never stored in this repository.

---

## Development policy

1. Develop automation and sensitive logic in **private** `Nun-root` only.
2. Publish to this repo **only** public HTML, schema, and metrics/ledger slices that pass integrity checks.
3. Automation must **merge** new nodes into the existing ledger—never replace a full database with a partial cache.
4. No secrets in git history of this repository.

---

## Contact

- Root Authority: [@bis3946](https://x.com/bis3946)
- Super Node: [@oovelma](https://x.com/oovelma)

**Sigl 3946 active.**
