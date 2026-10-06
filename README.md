# IvyHacks: Beat Muse — send kit

Everything a club lead needs to put this in front of their list, in under a minute.
Register link: https://luma.com/d60fjmjy

## If you got this as an email

**Just forward it.** Gmail, Outlook and Apple Mail keep the cover, the facts and the button when you forward.
Delete the "Fwd:" header lines if you want it to look native, add one line on top in your own words, send.

## If you want to send it fresh from your own account

1. Open the page: https://hmm76.github.io/ivyhacks-beat-muse-kit/
2. Click **Copy email**.
3. Paste into a new message in Gmail / Apple Mail / Outlook.
4. Subject: `Beat Muse. Win $4K. Oct 10–11 at Penn`
5. Send to your list.

The page is editable: click into the text and add your club's name before copying if you like.

## If your listserv strips HTML (Penn Mailman lists, some Google Groups)

Click **Plain text (listservs)** on the page, copy, paste. Attach `cover.jpg` so it still has a visual.

## Slack / GroupMe / Discord / Instagram

Post `cover.jpg` (1200×1200, the Luma cover) with the plain-text version as the caption.

## Files

- `index.html` — the email, both versions, with the Copy button
- `cover.jpg` — the Luma cover at 1200×1200, served from this repo so it loads in every inbox

## Why it is built this way

Email clients strip `<style>` blocks, classes, web fonts and flex/grid. Everything here is inline CSS inside tables,
with the image hosted at a public URL, which is the only combination that survives paste, forward, and re-paste.
