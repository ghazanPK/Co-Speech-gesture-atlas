# Organization website deployment

The data and website source stay in `ghazanPK/Co-Speech-gesture-atlas`.
The organization repository `co-speech-gesture-atlas/co-speech-gesture-atlas.github.io`
hosts <https://co-speech-gesture-atlas.github.io/>.

## How publication works

A push to the source repository's `main` (including a merged PR) runs validation
and a trial build. After those succeed, the source workflow dispatches the
website repository's deployment workflow. That workflow checks out the public
source `main`, validates and builds it, and publishes a GitHub Pages artifact.
PRs are validated without publishing or accessing the deployment token.
There are no scheduled checks. Literature searches remain manual.

The website workflow can also be run manually from Actions → Publish atlas
from data repository → Run workflow. Changing its workflow on `main` also
triggers a deployment.

## Configuration

Install [deployment/publish-pages.yml](deployment/publish-pages.yml) in the
website repository as `.github/workflows/publish-pages.yml`. Set Settings →
Pages → Source to **GitHub Actions**.

Create a fine-grained personal access token with:

- Resource owner: `co-speech-gesture-atlas`.
- Repository access: only `co-speech-gesture-atlas.github.io`.
- Repository permission: **Actions: Read and write** (Metadata read is automatic).
- An expiration date; renew the token before it expires.

Store it in the **source** repository under Settings → Secrets and variables →
Actions as the repository secret `ATLAS_PAGES_TOKEN`. Do not commit it or paste
it into chat. The token allows workflow dispatch in the website repository;
it does not require Contents write, an SSH deploy key, or an organization policy
change. Organization approval may be required for a token, depending on policy.

The installed `Atlas Pages deployment` token expires on **October 13, 2027**.
Before that date, renew it with the same scope and replace `ATLAS_PAGES_TOKEN`.

The source workflow `.github/workflows/publish-site.yml` uses that secret only
in its publish job after validation on `main`. If the token is missing, expired,
or revoked, publication fails visibly and the existing website stays live.

Make website changes in the source repository's `docs/` and `scripts/`.
The hosting repository needs only its workflow and README; generated files are
published as an artifact. Keep the hosting workflow synchronized with the
source template when deployment configuration changes.

## Maintenance

`deployment.json` records the published source commit and build timestamp,
not the literature search cutoff date. Citation graph assets in
`docs/citations.json` are published as supplied; deployment does not infer new
citation edges. There is no inactivity timeout from a scheduled workflow,
because scheduling is disabled.

If validation fails, fix the source records. If dispatch fails, check
`ATLAS_PAGES_TOKEN` and its expiration, repository scope, and Actions permission.
If deployment fails, inspect the hosting repository's Actions run, Pages source,
and `github-pages` environment rules. The previous successful site stays live.

The initially generated local SSH key is unused and has not been installed.

References: [Custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
and [Workflow dispatch permissions](https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event).
