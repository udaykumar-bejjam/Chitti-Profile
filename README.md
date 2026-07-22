# Jessika Seedarla — Profile

Animated portfolio page and resume for Jessika Seedarla, M.Sc. Biotechnology Gold Medalist.

## Live Site

**https://udaykumar-bejjam.github.io/Chitti-Profile/**

### Enable GitHub Pages (required one-time step)

GitHub Actions cannot deploy due to a billing lock on the account. Use branch deployment instead:

1. Open **Settings → Pages**: https://github.com/udaykumar-bejjam/Chitti-Profile/settings/pages
2. Under **Build and deployment → Source**, select **Deploy from a branch**
3. Branch: **`gh-pages`** · Folder: **`/ (root)`**
4. Click **Save** — the site goes live in ~1 minute

## Files

| File | Description |
|------|-------------|
| `index.html` | Animated profile landing page |
| `jessika_resume.pdf` | 2-page resume (downloadable) |
| `jessika_resume.html` | Editable resume source |

## Local Preview

```bash
python -m http.server 8000
```

Open http://localhost:8000/

## Deployment

GitHub Pages is deployed automatically via GitHub Actions on push to `master`.
