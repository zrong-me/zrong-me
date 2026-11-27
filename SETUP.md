# ZRONG — Sakura Edition GitHub Profile Setup

A more detailed GitHub profile README with a soft sakura theme, animated falling petals, project cards, learning map, stats, activity, and contribution visuals. It uses your own project links and does not copy another creator's identity or personal content.

## 1. Upload to the profile repository

Your special profile repository must be named exactly `zrong-me`: https://github.com/zrong-me/zrong-me

1. Download and extract this ZIP.
2. Open the extracted `ZRONG-Full-GitHub-Profile` folder.
3. Upload **the contents inside that folder** to the root of `zrong-me` (README.md, assets, .github, scripts, etc.).
4. Commit the files. Your profile page should then display the README.

Keep the `assets/sakura/petals.gif` file in the same path: the animated sakura decoration is a local GIF in your repository. GitHub README supports GIF images, but it does not run custom JavaScript or CSS animations.

## 2. Enable GitHub Actions

1. Open repository **Settings → Actions → General**.
2. Under Workflow permissions, choose **Read and write permissions** and save.
3. Open **Actions** and enable workflows if GitHub asks.

## 3. Run the included workflows

In the Actions tab, run these workflows manually:
- `Update profile activity` — updates the recent public activity section.
- `Generate contribution snake` — publishes the contribution animation to the `output` branch.
- `Generate 3D contribution profile` — publishes a 3D contribution graphic to the `profile-3d` branch.

The activity workflow uses GitHub's built-in `GITHUB_TOKEN`; no personal access token is needed.

## 4. Contribution snake

The README points to `https://raw.githubusercontent.com/zrong-me/zrong-me/output/github-snake-dark.svg`. This should work after the snake workflow succeeds and publishes the file to the `output` branch. If the filename differs, open that branch and update the image URL to match the actual file.

## 5. Optional 3D contribution image

The 3D workflow publishes to `profile-3d`. Once it succeeds, inspect that branch for the generated PNG and add its raw URL to the README if you want to display it. File names can vary by action version.

## 6. Personalize safely

Review the project links and descriptions before publishing. Remove anything you do not want public. The technology icons represent tools you use, learn, or explore — they do not claim expert-level proficiency.

## Included

- Sakura-pink hero banner and animated falling-petal GIF
- About section and technology toolkit
- Learning map, goals checklist, and creative workflow
- Four featured projects with links
- GitHub stats, top languages, streak, and activity graph
- Automatically updated recent public activity section
- Contribution snake and optional 3D contribution workflow
- Guestbook issue template

## Notes

- GitHub README does not execute JavaScript or custom CSS. The falling sakura effect is a GIF animation instead.
- External stats, typing, and icon services may occasionally be unavailable.
- GitHub Actions run on GitHub-hosted runners, not your personal computer.
- The workflows have been included in the ZIP but have not been run against your GitHub repository.
