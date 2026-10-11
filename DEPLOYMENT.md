# Organization website deployment

The data and website source stay in `ghazanPK/Co-Speech-gesture-atlas`.
The organization repository `co-speech-gesture-atlas/co-speech-gesture-atlas.github.io`
hosts the deployment workflow for <https://co-speech-gesture-atlas.github.io/>.

## Configuration

In the website repository, install [deployment/publish-pages.yml](deployment/publish-pages.yml)
as `.github/workflows/publish-pages.yml`. Set Settings → Pages → Source to
**GitHub Actions**. A push of the workflow on `main` triggers the first build;
Actions → Publish atlas from data repository → Run workflow can also deploy it.

The website workflow reads the public source repository's `main` branch every
15 minutes, at minutes 7, 22, 37, and 52 UTC. It compares the source commit with
the published `/deployment.json`, skips unchanged scheduled runs, and validates
and builds changed sources before publishing a Pages artifact. Manual runs
and workflow changes always rebuild. GitHub may delay scheduled runs, so this
is a polling interval rather than a guaranteed delivery deadline.

No deploy key, personal access token, or custom Actions secret is required.
The build job has read-only contents access. The separate deploy job uses
GitHub's short-lived Pages permissions for this website repository.
Organization deploy-key policy does not need to change.

The source workflow `.github/workflows/publish-site.yml` validates and builds
pushes and PRs. It does not publish or request secrets. Merged PRs and monthly
data updates are picked up by the website workflow on its next scheduled run.

Make website changes in the source repository's `docs/` and `scripts/`
directories. The hosting repository needs only its workflow and README; the
built website is deployed as an artifact, without mirroring data or committing
generated files there. Keep its workflow synchronized with the template here
if deployment configuration changes.

The generators produce explorer and application assets. Citation graph assets
in `docs/citations.json` are published as supplied; deployment does not infer
new citation edges. Deployment also does not perform literature searches.
`deployment.json` records a build timestamp and source commit, not a search
cutoff date.

After verifying the new website, update source README links and the repository
About URL. The original project Pages site can remain available during migration.

## Maintenance

GitHub disables scheduled workflows in public repositories after 60 days with
no repository activity. Because this hosting repository rarely changes, check
its Actions status periodically and re-enable the schedule if needed. A manual
workflow run is also available for immediate publication. The data repository's
activity does not itself count as hosting-repository activity.

If validation fails, fix the source records; the previous successful website
stays published. If deployment fails, inspect the hosting repository's Actions
run, Pages source setting, and `github-pages` environment rules.

The initially generated local SSH key is unused by this configuration and has
not been installed in GitHub.

References: [Custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
and [Scheduled workflow behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).
