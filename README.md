# HaoHorizon

Independent studio website for **HaoHorizon**, operated by **Yuhao Wang** in the United States.

- Intended domain: **https://haohorizon.com**
- Business contact: **hello@haohorizon.com** (confirmed by the operator)
- Primary work: remote sensing data processing and scientific software development
- Public projects: [CoastTideX](https://github.com/wyhao2333/CoastTideX) and [PaperPilot](https://github.com/wyhao2333/zotero-paperpilot)

HaoHorizon is currently unincorporated. The site does not claim an LLC, invented company history, client engagements, revenue, funding or a live Claude integration. The existing open-source projects remain in their own repositories; this website does not change them.

## Source structure

- `public/`: ready-to-serve static website
- `public/work/`: detailed project pages with documentation and release links
- `public/about.html`: founder, working approach and studio status
- `public/privacy.html`: website-specific data handling
- `scripts/prepare-site.py`: regenerates shared pages, original SVG artwork and the structured-data CSP hash
- `scripts/build-preview.py`: creates a base-path-correct GitHub Pages preview artifact
- `wrangler.jsonc`: Cloudflare Worker static-assets configuration

The committed `public/` directory is complete. No installation, build, backend, model access or API credentials are needed to serve it. The local Manrope font is distributed with its SIL Open Font License in `public/assets/fonts/OFL.txt`. The coastal artwork is an illustration, not satellite imagery or scientific model output. PaperPilot artwork is not a fabricated application screenshot.

## Preview locally

```powershell
python -m http.server 8091 --bind 127.0.0.1 --directory public
```

Open **http://127.0.0.1:8091/**. The simple local server does not apply Cloudflare `_headers`.

## Deploy to Cloudflare Workers

Create a **new** Worker for this repository; do not replace the Studio 980463 Worker.

1. Open Cloudflare **Workers & Pages → Create application → Import a repository**.
2. Select **wyhao2333/haohorizon-website**, branch **main**.
3. Worker name: **haohorizon-website**. Repository root: `/`.
4. No build command is required because `public/` is already prepared.
5. Deploy command: **npx wrangler@4.149.0 deploy**. The checked-in configuration selects `public/` as static assets.
6. Verify the generated `*.workers.dev` site.
7. Open the new Worker’s **Domains & Routes / Domains → Add domain**. Select **haohorizon.com**, leave the optional subdomain empty, and add the production domain. Cloudflare will manage the website DNS record and certificate if the zone is in the same account.
8. Optionally add **www.haohorizon.com** as another custom domain or redirect it to the apex domain.
9. Confirm HTTPS and the homepage, both project pages, About and Privacy on the domain.

Keep the existing email MX/TXT records. Do not add a Worker Route as a substitute for its Custom Domain. If there is a conflicting website record, review the specific conflict before replacing it.

Alternatively, after logging into your own Cloudflare account:

```powershell
npx wrangler@4.149.0 login
npx wrangler@4.149.0 deploy
```

Custom domains can then be bound in the dashboard. No Cloudflare credentials are committed to this repository.

References: [Static assets](https://developers.cloudflare.com/workers/static-assets/get-started/), [Worker custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/).

## Alternative: Cloudflare Pages

Create a Pages project connected to this repository. Use **main**, framework **None**, no build command, and **public** as the build output directory. Add the domain through the Pages project’s Custom domains flow after verifying its `*.pages.dev` URL.

## GitHub Pages review URL

The optional workflow publishes a preview at **https://wyhao2333.github.io/haohorizon-website/**. It creates an artifact with project-prefixed asset and navigation paths; the Cloudflare source in `public/` remains configured for `haohorizon.com`. This review URL does not change the custom domain’s DNS or publish the site at `haohorizon.com`.

## Editing

Edit homepage content in `public/index.html`; edit other pages in `scripts/prepare-site.py`, then run it. Edit styling in `public/styles.css` and menu/clipboard behavior in `public/site.js`. Keep facts and maturity statements consistent across the website and any business application.

CoastTideX documentation reports v1.7.1. PaperPilot has a public v1.0.1 release and its tested environment is Zotero 10. Native Claude integration is not claimed for that release. Capabilities were checked against the repositories on October 9, 2026.
