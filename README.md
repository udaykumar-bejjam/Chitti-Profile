# Chitti Profile

Static profile pages hosted on GitHub Pages.

## Live Site

**https://udaykumar-bejjam.github.io/Chitti-Profile/**

| Path | Profile |
|------|---------|
| `/` | Jessika Seedarla |
| `/uday-profile/` | Uday Kumar Bejjam |

Uday profile URL: **https://udaykumar-bejjam.github.io/Chitti-Profile/uday-profile/**

### Enable GitHub Pages (required one-time step)

GitHub Actions cannot deploy due to a billing lock on the account. Use branch deployment instead:

1. Open **Settings → Pages**: https://github.com/udaykumar-bejjam/Chitti-Profile/settings/pages
2. Under **Build and deployment → Source**, select **Deploy from a branch**
3. Branch: **`gh-pages`** · Folder: **`/ (root)`**
4. Click **Save** — the site goes live in ~1 minute

## Files

| File / Folder | Description |
|---------------|-------------|
| `index.html` | Jessika animated profile landing page |
| `jessika_resume.pdf` | Jessika resume (downloadable) |
| `jessika_resume.html` | Jessika editable resume source |
| `uday-profile/` | Uday online profile + tech resume |
| `uday-profile/index.html` | Uday profile landing page |
| `uday-profile/uday_resume.html` | Technology-themed resume (HTML) |
| `uday-profile/Uday_Kumar_Bejjam_Tech_Resume.pdf` | Technology-themed resume (PDF download) |

## Local Preview

```bash
python -m http.server 8000
```

Open http://localhost:8000/ or http://localhost:8000/uday-profile/

## Deployment

GitHub Pages is deployed automatically via GitHub Actions on push to `master`.
