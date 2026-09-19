# Board links — the website

Sudoku Mini shares a board as a link: `https://<your-github-name>.github.io/sudoku/?b=<code>`.
The whole board travels inside `<code>` (see `app/.../engine/ShareCode.kt`), so the site is just
three static files and needs no server.

- **App installed:** Android opens the link straight in Sudoku Mini. That only happens once the site
  proves it belongs with the app, through `.well-known/assetlinks.json`.
- **App not installed:** the link opens `sudoku/index.html`, which draws the board and links to
  Google Play.

## Publish it (once)

1. On GitHub, create a repository named exactly **`<your-github-name>.github.io`**.
   It has to be this user-site repository, not a project page like `…github.io/sudoku-site`:
   Android only looks for `/.well-known/assetlinks.json` at the root of the domain.
2. Copy everything in this `web/` folder into the repository root, including the hidden
   `.well-known/` folder and the `.nojekyll` file. Without `.nojekyll`, GitHub Pages skips folders
   whose names start with a dot. Commit and push.
3. In the repository, go to **Settings → Pages** and publish from the `main` branch, `/ (root)`.
4. Check that both of these open in a browser:
   - `https://<your-github-name>.github.io/.well-known/assetlinks.json`
   - `https://<your-github-name>.github.io/sudoku/`, which shows "This link doesn't hold a board"
     because there is no code in it.
5. In the app project's `local.properties` (which git ignores), add:
   ```
   shareHost=<your-github-name>.github.io
   ```
   Then rebuild. The share buttons appear only once this is set.
6. On a phone with the new build installed, check Android verified the site:
   ```
   adb shell pm get-app-links com.fungrid.sudokumini
   ```
   The host should show as `verified`. If it's still `none` right after installing, run
   `adb shell pm verify-app-links --re-verify com.fungrid.sudokumini` and check again.

## Signing keys in `assetlinks.json`

The file lists the SHA-256 fingerprint of every key that signs a build that should open links:

- **Debug key** (already in the file): builds run from Android Studio.
- **Your upload key:** once a release keystore is set up, get its fingerprint with
  `keytool -list -v -keystore <release.jks> -alias <alias>` and add the `SHA256:` value.
- **Play App Signing key:** after the first upload, Play Console → *Test and release → App integrity
  → App signing* shows it. Play re-signs the app with this key, so without it, links won't open
  the app for people who install from Play.

Add each fingerprint as another string in `sha256_cert_fingerprints`, then push again.
