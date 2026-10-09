"""Build the small static site’s shared pages and original SVG artwork."""
from pathlib import Path
import hashlib
import base64
import math
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
HOME = (PUBLIC / "index.html").read_text(encoding="utf-8")
HEADER = re.search(r"  <header class=\"site-header\">.*?</header>", HOME, re.S).group()
HEADER = HEADER.replace('href="#work"', 'href="/#work"').replace('href="#services"', 'href="/#services"').replace('href="#contact"', 'href="/#contact"')
FOOTER = re.search(r"  <footer class=\"site-footer\">.*?</footer>", HOME, re.S).group()


def page(path, title, description, body):
    destination = PUBLIC / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — HaoHorizon</title><meta name="description" content="{description}">
<meta name="theme-color" content="#f6f5ef"><link rel="canonical" href="https://haohorizon.com/{path}">
<meta property="og:title" content="{title} — HaoHorizon"><meta property="og:description" content="{description}"><meta property="og:type" content="website"><meta property="og:image" content="https://haohorizon.com/assets/social-card.png">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/styles.css"><script src="/site.js" defer></script>
</head><body><a class="skip-link" href="#main">Skip to content</a>
{HEADER}
<main id="main">{body}</main>
{FOOTER}
</body></html>''', encoding="utf-8")


def sidebar(links):
    return '<aside class="article-sidebar" aria-label="On this page"><strong>On this page</strong>' + ''.join(f'<a href="#{anchor}">{label}</a>' for anchor, label in links) + '</aside>'


coast = '''
<section class="page-hero container"><div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/#work">Selected work</a><span>/</span><span>CoastTideX</span></div>
<div class="page-status"><span class="eyebrow">Geospatial software</span><span class="status">Open-source toolkit</span></div>
<h1>Coastal data.<br><span class="serif">A consistent reference.</span></h1>
<p class="lead">CoastTideX brings astronomical tide simulation, elevation reference conversion and coastal raster processing into one scientific toolkit.</p>
<div class="page-actions"><a class="button button-dark" href="https://github.com/wyhao2333/CoastTideX">Explore the source <span aria-hidden="true">↗</span></a><a class="text-link" href="https://github.com/wyhao2333/CoastTideX/blob/main/README_EN.md">Read the documentation <span aria-hidden="true">↗</span></a></div></section>
<div class="container"><figure class="project-banner"><img src="/assets/coastal-study.svg" width="900" height="760" alt="Conceptual coastal terrain with contours and an outlined study area."><figcaption class="banner-caption">Coastal terrain illustration · not a CoastTideX output or accuracy claim</figcaption></figure>
<div class="project-meta"><div><span>Developer</span><strong>Yuhao Wang</strong></div><div><span>Current documentation</span><strong>v1.7.1</strong></div><div><span>Interface</span><strong>Desktop GUI + CLI</strong></div><div><span>Source license</span><strong>MIT</strong></div></div></div>
<div class="container article-grid">SIDEBAR<div class="article-body">
<section id="question"><h2>The research question.</h2><p>Coastal analyses often combine tide levels, elevation rasters and observations with different vertical references. Comparing them without understanding those references can produce misleading results.</p><p>CoastTideX is developed for coastal and intertidal workflows that need a clear relationship between tide simulation and elevation data. It provides a practical toolchain for configuring, running and inspecting those steps.</p></section>
<section id="capabilities"><h2>What the toolkit does.</h2><table class="feature-table"><tbody><tr><th scope="row">Tide simulation</th><td>Astronomical tide simulation using the FES2022b model and its native unstructured mesh.</td></tr><tr><th scope="row">Height references</th><td>Workflows linking mean sea level, EGM2008 and WGS84 elevation references, with documented MDT and geoid assumptions.</td></tr><tr><th scope="row">Coastal raster workflows</th><td>Tools for DEM preparation, tidal inundation and exposure analyses under the configured scientific assumptions.</td></tr><tr><th scope="row">Batch processing</th><td>A batch DEM conversion workflow with resume support and processing manifests.</td></tr><tr><th scope="row">Usable interfaces</th><td>Desktop GUI and command-line entry points, with documentation and automated tests in the public repository.</td></tr></tbody></table><p>Refer to the <a href="https://github.com/wyhao2333/CoastTideX/blob/main/README_EN.md">current project documentation</a> for model data requirements, setup, supported workflows and limitations. External model datasets have their own access and licensing terms.</p></section>
<section id="evidence"><h2>Code you can inspect.</h2><p>The public repository contains the implementation, usage documentation and testing workflow. Numerical outputs depend on the selected model, reference data, input quality and local conditions; software tests do not establish a single accuracy guarantee for every coastline.</p><ul><li><a href="https://github.com/wyhao2333/CoastTideX">Source repository</a></li><li><a href="https://github.com/wyhao2333/CoastTideX/blob/main/README_EN.md">English documentation</a></li><li><a href="https://github.com/wyhao2333/CoastTideX/actions">Automated workflow history</a></li><li><a href="https://github.com/wyhao2333/CoastTideX/blob/main/LICENSE">MIT source license</a></li></ul></section>
<section id="next"><h2>The next application.</h2><p>HaoHorizon is planning an AI-assisted interface around bounded coastal workflows. The intended role of Claude is to help turn requests into reviewable configurations, explain logs and draft reports grounded in processing settings and outputs.</p><p>The scientific tools would perform the calculations, with approval before execution. <strong>The Claude API integration is in planning and evaluation; it is not a currently available feature.</strong></p><div class="note-panel"><h3>Working on a related data problem?</h3><p>We can discuss a focused remote sensing or scientific software task, using a representative sample and a clearly defined deliverable. <a href="mailto:hello@haohorizon.com?subject=Coastal%20workflow%20inquiry">Tell us about your project ↗</a></p></div></section>
</div></div>
<div class="container project-next"><div><p class="eyebrow">Next project</p><a href="/work/paperpilot.html">PaperPilot <span aria-hidden="true">↗</span></a></div><a href="/#work">All selected work ↑</a></div>
'''
page("work/coasttidex.html", "CoastTideX", "Open-source coastal tide simulation and vertical-datum workflows by Yuhao Wang. Explore the capabilities, source and planned AI integration.", coast.replace('SIDEBAR', sidebar([('question','The question'),('capabilities','Capabilities'),('evidence','Public evidence'),('next','Next application')])))

paper = '''
<section class="page-hero container"><div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/#work">Selected work</a><span>/</span><span>PaperPilot</span></div>
<div class="page-status"><span class="eyebrow">Research application</span><span class="status">Released · v1.0.1</span></div>
<h1>Stay with the paper.<br><span class="serif">Make room for the ideas.</span></h1><p class="lead">PaperPilot is an open-source academic reading assistant inside Zotero 10. Translate selections, ask contextual questions and turn reading sessions into useful notes.</p>
<div class="page-actions"><a class="button button-dark" href="https://github.com/wyhao2333/zotero-paperpilot/releases/tag/v1.0.1">Get the Zotero add-on <span aria-hidden="true">↗</span></a><a class="text-link" href="https://github.com/wyhao2333/zotero-paperpilot">Explore the source <span aria-hidden="true">↗</span></a></div></section>
<div class="container"><div class="project-banner paper-visual"><span class="banner-wordmark">PAPERPILOT / RESEARCH TOOLS</span><div class="paper-stack" aria-hidden="true"><div class="paper-sheet sheet-back"></div><div class="paper-sheet sheet-front"><span class="paper-wordmark">P<span>→</span></span><span class="paper-rule"></span><span class="paper-rule short"></span><span class="paper-mini-label">Read · Ask · Understand</span><div class="paper-pill">PaperPilot <span>↗</span></div></div><span class="note-chip">Ideas into notes.</span></div><p class="banner-caption">Project artwork · not a screenshot of the Zotero interface</p></div>
<div class="project-meta"><div><span>Developer</span><strong>Yuhao Wang</strong></div><div><span>Published package</span><strong>v1.0.1 · September 2026</strong></div><div><span>Tested environment</span><strong>Zotero 10</strong></div><div><span>Source license</span><strong>MIT</strong></div></div></div>
<div class="container article-grid">SIDEBAR<div class="article-body">
<section id="purpose"><h2>A companion to the reading workflow.</h2><p>Reading scientific literature involves moving between the source text, technical terminology, questions and notes. PaperPilot brings several of those steps into Zotero’s PDF reader instead of treating every excerpt as an isolated conversation.</p><p>The public plugin supports configured translation services and AI providers. Its outputs remain aids to reading: important interpretations should be checked against the paper.</p></section>
<section id="features"><h2>What is in the current release.</h2><table class="feature-table"><tbody><tr><th scope="row">Selection translation</th><td>Translate selected PDF text, with AI translation and local paragraph context when configured.</td></tr><tr><th scope="row">Contextual questions</th><td>Ask about an excerpt or use the reader sidebar to discuss paper content with a configured model.</td></tr><tr><th scope="row">Paper digests</th><td>Generate structured reading summaries, using single-pass or chunked processing as appropriate.</td></tr><tr><th scope="row">Separate reading sessions</th><td>Keep multiple local conversations for each PDF, with options to create, rename and switch sessions.</td></tr><tr><th scope="row">Note export</th><td>Export a reading conversation to a Zotero note; render common mathematical expressions in the sidebar.</td></tr></tbody></table></section>
<section id="install"><h2>Install and configure.</h2><ol><li>Open the <a href="https://github.com/wyhao2333/zotero-paperpilot/releases/tag/v1.0.1">v1.0.1 release</a> and download <strong>paperpilot-1.0.1.xpi</strong>.</li><li>In Zotero 10, open <strong>Tools → Add-ons</strong>, then choose <strong>Install Add-on From File</strong> from the gear menu.</li><li>Select the package and follow Zotero’s installation prompts.</li><li>Choose your translation service and AI provider in PaperPilot settings. AI features require your own configured provider access.</li></ol><p>The current release has been tested in Zotero 10; other versions are not verified. See the <a href="https://github.com/wyhao2333/zotero-paperpilot">repository README</a> for configuration, troubleshooting, privacy details and limitations.</p></section>
<section id="data"><h2>Where data goes.</h2><p>Chat history is stored locally by the plugin. When using online AI or translation services, relevant text is sent to the configured providers; full-paper analysis may send a substantial portion of the extracted paper text. Translation fallback can involve another translation provider.</p><p>Review the repository’s data-handling information and your institution’s policies before processing sensitive or unpublished material. This website does not accept PDF uploads or run the plugin.</p><div class="note-panel"><h3>Claude integration status</h3><p>PaperPilot v1.0.1 uses compatible configured model endpoints. Native Anthropic API support is not represented as an existing feature. HaoHorizon is evaluating future Claude-powered research workflows.</p></div></section>
<section id="source"><h2>Explore the implementation.</h2><ul><li><a href="https://github.com/wyhao2333/zotero-paperpilot">Source and documentation</a></li><li><a href="https://github.com/wyhao2333/zotero-paperpilot/releases/tag/v1.0.1">Release package and checksum file</a></li><li><a href="https://github.com/wyhao2333/zotero-paperpilot/blob/main/CHANGELOG.md">Changelog</a></li><li><a href="https://github.com/wyhao2333/zotero-paperpilot/blob/main/LICENSE">MIT source license</a></li></ul><p>Have a research tool or document workflow to develop? <a href="mailto:hello@haohorizon.com?subject=Research%20software%20inquiry">Discuss a project with HaoHorizon ↗</a></p></section>
</div></div>
<div class="container project-next"><div><p class="eyebrow">Explore another project</p><a href="/work/coasttidex.html">CoastTideX <span aria-hidden="true">↗</span></a></div><a href="/#work">All selected work ↑</a></div>
'''
page("work/paperpilot.html", "PaperPilot for Zotero", "An open-source Zotero 10 reading assistant by Yuhao Wang, with contextual AI questions, translation, paper digests and note export.", paper.replace('SIDEBAR', sidebar([('purpose','The purpose'),('features','Current release'),('install','Installation'),('data','Data handling'),('source','Source & release')])))

about = '''
<section class="page-hero container"><div class="breadcrumb"><a href="/">Home</a><span>/</span><span>About</span></div><p class="eyebrow">About HaoHorizon</p><h1>Research-minded.<br><span class="serif">Built by hand.</span></h1><p class="lead">An independent studio for remote sensing data processing, scientific software and practical research applications.</p></section>
<div class="container article-grid">SIDEBAR<div class="article-body">
<section id="studio"><h2>A focused technical practice.</h2><p>HaoHorizon is the working name of Yuhao Wang’s independent studio, operated in the United States. Its focus is helping researchers and small teams turn data and methods into repeatable workflows and usable software.</p><p>The intended business includes scoped remote sensing data-processing work, scientific software development and research application prototypes. Project requirements, deliverables and terms are agreed directly before an engagement begins.</p></section>
<section id="founder"><h2>The person behind the work.</h2><div class="founder-card"><div class="founder-monogram" aria-hidden="true">YW</div><div><h3>Yuhao Wang</h3><p>Founder & software developer</p><div class="founder-links"><a href="https://github.com/wyhao2333">GitHub ↗</a><a href="https://www.linkedin.com/in/%E5%AE%87%E6%B5%A9-%E7%8E%8B-a584a4435/">LinkedIn ↗</a></div></div></div><p>Yuhao develops <a href="/work/coasttidex.html">CoastTideX</a>, a coastal tide and vertical-datum toolkit, and <a href="/work/paperpilot.html">PaperPilot</a>, a Zotero reading assistant. Their public repositories provide a view of the code, documentation and development work.</p><p>HaoHorizon brings this geospatial and software practice under a straightforward studio identity. Initial priorities are remote sensing data processing and scientific software development.</p></section>
<section id="approach"><h2>How the work is approached.</h2><ul><li><strong>Define the inputs and assumptions.</strong> Coordinate references, height references, data quality and study boundaries should be explicit.</li><li><strong>Start with a representative sample.</strong> Check the method on a bounded example before committing to a larger run.</li><li><strong>Keep the workflow inspectable.</strong> Prefer understandable code, useful tests and documentation that helps the next person.</li><li><strong>Evaluate AI in context.</strong> Use models for bounded assistance and review their outputs against the original documents or scientific tools.</li></ul></section>
<section id="status"><h2>Studio and product status.</h2><p>HaoHorizon is currently an <strong>unincorporated independent studio</strong> operated by Yuhao Wang. Its public technical work includes CoastTideX and PaperPilot, both available under the MIT source license.</p><p>Claude API integration is in planning and evaluation. It is a proposed development direction, rather than an available feature of the current PaperPilot release.</p><p>Studio 980463 and HaoHorizon are working names used by the same developer, Yuhao Wang. HaoHorizon focuses the public presentation on remote sensing services and scientific software development.</p></section>
<section id="contact"><h2>Start a conversation.</h2><p>For project inquiries, contact <a href="mailto:hello@haohorizon.com">hello@haohorizon.com</a>. Include the problem you want to solve, a description of the data and the deliverable you have in mind. Technical issues with an open-source project can also be reported in its GitHub repository.</p><a class="button button-dark" href="/#contact">Discuss your project <span aria-hidden="true">↗</span></a></section>
</div></div>
'''
page("about.html", "About the studio", "Meet Yuhao Wang and HaoHorizon, an independent studio focused on remote sensing data processing and scientific software development.", about.replace('SIDEBAR', sidebar([('studio','The studio'),('founder','Yuhao Wang'),('approach','Approach'),('status','Studio status'),('contact','Get in touch')])))

privacy = '''
<article class="container simple-article"><p class="eyebrow">Last updated · October 9, 2026</p><h1>Privacy notice.</h1><p>This notice describes the informational website at <strong>haohorizon.com</strong>, operated by Yuhao Wang under the HaoHorizon studio name.</p>
<h2>Browsing this website</h2><p>The website does not provide account registration, PDF uploads, a contact form or live AI functionality. The website’s own code does not set analytics or advertising cookies, and it does not include third-party tracking scripts.</p><p>The hosting and security provider, Cloudflare, may process request information such as IP addresses, browser details, requested paths and timestamps to deliver and protect the website. Provider security features may use cookies or similar mechanisms. Their handling is described in <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare’s privacy policy</a>.</p>
<h2>Getting in touch</h2><p>Email links open your email application. If you send an inquiry, the operator and the email service involved will process your contact information and message to respond and discuss your project. Please do not include sensitive datasets or credentials in an initial inquiry.</p><p>Project-specific data processing, access, retention and confidentiality requirements are agreed separately before data is shared for an engagement.</p>
<h2>Small browser interactions</h2><p>The navigation menu works within the page. The “Copy email” button requests clipboard access only when clicked and writes the displayed business email address. It does not read your clipboard or store copied information.</p>
<h2>Links and open-source tools</h2><p>Links to GitHub, LinkedIn and other external websites take you to services with their own policies. CoastTideX and PaperPilot run separately from this website. See their repository documentation for tool-specific data handling. In particular, PaperPilot’s configured online AI and translation services can receive document text.</p>
<h2>Questions</h2><p>Contact <a href="mailto:hello@haohorizon.com">hello@haohorizon.com</a> with questions about this website or its privacy notice.</p><p><a href="/">Return to HaoHorizon ↗</a></p></article>
'''
page("privacy.html", "Privacy", "How the HaoHorizon informational website handles browsing and project inquiries, and where to find privacy information for its open-source tools.", privacy)
page("404.html", "Page not found", "This page could not be found. Return to HaoHorizon’s remote sensing and scientific software studio website.", '<section class="container error-page"><p class="eyebrow">A little off the map</p><h1>404</h1><p>This page could not be found.<br>Let’s get you back to familiar ground.</p><a class="button button-dark" href="/">Back to HaoHorizon <span aria-hidden="true">↗</span></a></section>')

# Build an original, explicitly illustrative coastal map in SVG.
assets = PUBLIC / "assets"
assets.mkdir(exist_ok=True)
land = 'M380,-50 C420,50 320,90 410,170 C510,250 370,300 450,355 C550,400 470,460 550,490 C650,520 530,590 655,640 C760,690 660,750 800,810 L950,810 L950,-50 Z'
parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 760" role="img" aria-labelledby="title desc">', '<title id="title">Coastal terrain study</title><desc id="desc">Original illustrative map, not satellite imagery or model output.</desc>', '<defs><clipPath id="land"><path d="'+land+'"/></clipPath><pattern id="grid" width="90" height="76" patternUnits="userSpaceOnUse"><path d="M90 0H0V76" fill="none" stroke="#c4d1c1" stroke-opacity=".16" stroke-width=".6"/></pattern><filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".32" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="linear" slope=".1"/></feComponentTransfer><feBlend in="SourceGraphic" mode="soft-light"/></filter></defs>', '<rect width="900" height="760" fill="#294b48"/>']
for i in range(28):
    points = []
    for x in range(-90, 951, 15):
        y = i*30 + 29*math.sin(x/190+i*.19) + 12*math.sin(x/82+i*.31)
        points.append(f'{x},{y:.1f}')
    parts.append('<polyline points="'+' '.join(points)+'" fill="none" stroke="#658982" stroke-opacity=".34" stroke-width=".75"/>')
parts.append('<path d="'+land+'" fill="#a5b6a0"/>')
parts.append('<g clip-path="url(#land)">')
for i in range(55):
    points = []
    for x in range(280, 966, 10):
        y = i*16-20+58*math.sin(x/140+i*.12)+20*math.sin(x/48+i*.23)+11*math.sin(x/28+i*.07)
        points.append(f'{x},{y:.1f}')
    color = '#405f43' if i%4==0 else '#52754d'
    parts.append('<polyline points="'+' '.join(points)+'" fill="none" stroke="'+color+'" stroke-opacity=".47" stroke-width="'+('1.4' if i%4==0 else '.7')+'"/>')
parts.extend(['<path d="M408 169 C490 186 525 222 610 210 S680 170 782 226 S825 202 930 244 M450 354 C520 360 545 401 640 365 S723 374 825 349 M550 489 C629 479 612 520 730 471 S808 501 920 470" fill="none" stroke="#d1dcc6" stroke-width="4" stroke-linecap="round"/>', '<path d="M610 210 C641 266 690 267 723 315 M640 365 C617 319 650 296 675 281 M730 471 C757 445 749 417 788 403" fill="none" stroke="#d1dcc6" stroke-width="2" stroke-linecap="round"/>', '</g>', '<path d="'+land+'" fill="none" stroke="#d9e1ca" stroke-opacity=".7" stroke-width="1.2"/>', '<rect width="900" height="760" fill="url(#grid)"/>', '<rect width="900" height="760" fill="#608a66" opacity=".25" filter="url(#grain)"/>', '<g fill="none" stroke="#e2a775" stroke-width="1.5"><rect x="342" y="287" width="231" height="191" stroke-dasharray="5 7"/><path d="M336 287h13m-7-7v14 M567 287h13m-7-7v14 M336 478h13m-7-7v14 M567 478h13m-7-7v14"/></g>', '<g fill="#e4eadb" font-family="Arial,sans-serif" font-size="10" letter-spacing="2"><text x="350" y="272">STUDY EXTENT</text><text x="35" y="683">COAST / TERRAIN / REFERENCE</text></g>', '<g stroke="#e4eadb" stroke-width="1.3" fill="none"><path d="M766 65V35m-5 9 5-9 5 9"/><path d="M40 701h150m-150-4v8m75-8v8m75-8v8"/></g>', '<text x="762" y="24" fill="#e4eadb" font-family="Arial,sans-serif" font-size="11">N</text>', '</svg>'])
(assets / 'coastal-study.svg').write_text('\n'.join(parts), encoding='utf-8')

# Allow only the exact structured-data block, keeping executable scripts local.
structured = re.search(r'<script type="application/ld\+json">(.*?)</script>', HOME, re.S).group(1)
digest = base64.b64encode(hashlib.sha256(structured.encode()).digest()).decode()
headers_path = PUBLIC / '_headers'
headers = headers_path.read_text(encoding='utf-8')
headers = re.sub(r"'sha256-[^']+'", f"'sha256-{digest}'", headers)
headers_path.write_text(headers, encoding='utf-8')
print('Prepared 5 pages, original coastal SVG, and structured-data CSP hash.')
