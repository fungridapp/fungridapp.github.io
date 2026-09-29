"""Builds the per-app privacy policy pages for fungridapp.github.io.

Same sections and wording as the Dots and Boxes Mini policy; each app gets its own facts (read
from its code) and its own look (read from its colors.xml and fonts).
"""
import html, os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "29 September 2026"

APPS = {
  "xomini": dict(
    name="XO Mini", package="com.fungrid.xomini", icon="xomini.png",
    play="https://play.google.com/store/apps/details?id=com.fungrid.xomini",
    theme=dict(
      fonts="family=Roboto:wght@400;500;700;900",
      display="900 {size} Roboto, system-ui, sans-serif", body='Roboto, system-ui, sans-serif',
      theme_color="#DFE4F2",
      # XO's menu: the cool bg_app wash with its indigo (X) and orange (O) blooms.
      bg="radial-gradient(70% 45% at 8% 0%, rgba(91,110,245,.20), transparent 70%),"
         "radial-gradient(60% 45% at 100% 100%, rgba(255,138,61,.18), transparent 70%),"
         "linear-gradient(#E6EAF6, #DFE4F2)",
      ink="#2E3355", body_ink="#575B79", muted="#6B6F8C", card="#FFFFFF", hair="rgba(46,51,85,.10)",
      accent="#5B6EF5", link="#3A54AD", marker="#FF8A3D",
      tint="#E7EAFD", tint_ink="#3444B0",
      lead="linear-gradient(145deg, #6B7CF7, #4457E8)", lead_shadow="rgba(68,87,232,.30)",
      c1="#5B6EF5", c2="#FF8A3D", c3="#8B5BF5", wordmark_sub="#FF8A3D"),
    stored=[
      ("Player names", "the names you type for X and O in 2 Player mode",
       "So the game can fill them in next time and label the leaderboard.",
       "Change them before a game, or clear the app's storage."),
      ("Leaderboard", "for each finished round: the player's name, who they played (another name or the AI "
       "and its level), the result, the mode (Classic, Misère or Vanish), the board size and when it was played",
       "To rank players by wins in each mode.", "Clear the app's storage, or uninstall the app."),
      ("Settings and preferences", "background music and game sounds on or off, their volumes, your last board "
       "size and difficulty, whether you've seen How to Play", "So the app sounds and starts the way you left it.",
       "Clear the app's storage, or uninstall the app."),
      ("Ad consent choice", "stored by Google's consent library", "To remember your answer and not ask again.",
       "Change it under Settings → Ad Privacy Options."),
    ],
    name_note=True,
    ads_where="at the bottom of the main menu, the game setup screen and the game screen",
    ads_extra="There are no full-screen or video ads, and nothing interrupts a round.",
    consent="Settings → Ad Privacy Options",
    haptics="The small taps you feel as you play.",
    offline="The game itself, including the AI on every difficulty, runs on your phone and works fully offline.",
    delete="The app has no in-app reset. To remove everything it stores, clear its storage "
           "(Android Settings → Apps → XO Mini → Storage → Clear storage) or uninstall it.",
    children="XO Mini is a game suitable for all ages",
  ),
  "connect4mini": dict(
    name="Connect 4 Mini", package="com.fungrid.connect4mini", icon="connect4mini.png", play=None,
    theme=dict(
      fonts="family=Poppins:wght@600;700&family=Nunito:wght@400;600;700",
      display="700 {size} Poppins, system-ui, sans-serif", body='Nunito, system-ui, sans-serif',
      theme_color="#F4F7FB",
      # Connect 4's light "wall" (wall_top to card_bottom) under a faint grid of disc holes.
      bg="radial-gradient(rgba(28,34,43,.07) 5px, transparent 5.5px) 0 0 / 30px 30px,"
         "linear-gradient(#F4F7FB, #E9EDF4)",
      ink="#1C222B", body_ink="#4A5262", muted="#6B7383", card="#FFFFFF", hair="rgba(28,34,43,.10)",
      accent="#CA8A00", link="#8A5E00", marker="#CA8A00",
      tint="#FBF3DF", tint_ink="#7A5200",
      # The navy of the icon and the game's hero, with the gold disc's glow.
      lead="radial-gradient(120% 90% at 100% 0%, rgba(245,196,66,.20), transparent 55%), linear-gradient(160deg, #26303F, #151A22)",
      lead_shadow="rgba(21,26,34,.35)",
      c1="#E8B21E", c2="#B6BEC9", c3="#1C222B", wordmark_sub="#CA8A00"),
    stored=[
      ("Player names", "the names you give Player 1 and Player 2",
       "So the game can greet you and label your stats.", "Rename them in the game, or clear the app's storage."),
      ("Stats", "games played, wins for each player, draws, current and best win streak and who holds it, "
       "average moves, longest game, and a short list of recent games with the mode, result and number of moves",
       "The Stats page: your streaks and win record.", "Tap Reset all stats on the Stats page."),
      ("Settings and preferences", "theme, game sounds and background music on or off and their volumes, "
       "difficulty and game mode (Classic, Reverse or Pop-Out)", "So the app looks, sounds and starts the way you left it.",
       "Clear the app's storage, or uninstall the app."),
      ("Ad consent choice", "stored by Google's consent library", "To remember your answer and not ask again.",
       "Change it under Settings → Privacy → Ad privacy choices."),
    ],
    name_note=True,
    ads_where="at the bottom of the main menu and the game screen",
    ads_extra="There are no full-screen or video ads, and nothing interrupts a game.",
    consent="Settings → Privacy → Ad privacy choices",
    haptics="The small taps you feel when a disc drops.",
    offline="The game itself, including the AI, runs on your phone and works fully offline.",
    delete="Tap Reset all stats on the Stats page to clear your record. To remove everything the app stores, "
           "clear its storage (Android Settings → Apps → Connect 4 Mini → Storage → Clear storage) or uninstall it.",
    children="Connect 4 Mini is a game suitable for all ages",
  ),
  "worldofwords": dict(
    name="World of Words", package="com.fungrid.worldofwordsmini", icon="worldofwords.png", play=None,
    theme=dict(
      fonts="family=Outfit:wght@400;600;700&family=Instrument+Serif:ital@0;1",
      display="700 {size} Outfit, system-ui, sans-serif", body='Outfit, system-ui, sans-serif',
      theme_color="#99E3FF",
      # The game's grad-sky: sky blue down to meadow green.
      bg="linear-gradient(178deg, #99E3FF 0%, #AAEFF7 30%, #BFF4C9 65%, #D8E89B 100%)",
      ink="#022710", body_ink="#4D6453", muted="#5F7465", card="#FAFDF7", hair="#DBE4DB",
      accent="#007591", link="#A83876", marker="#CD5394",
      tint="#AAE3EF", tint_ink="#005468",
      lead="linear-gradient(150deg, #0A8FA8, #007591 55%, #005F76)", lead_shadow="rgba(0,95,118,.30)",
      c1="#CAE763", c2="#40BEFD", c3="#FB83BF", wordmark_sub="#CD5394"),
    stored=[
      ("Player names", "the two names you type for Pass & Play",
       "So the game can fill them in next time and label the leaderboard.", "Change them before a game, or clear the app's storage."),
      ("Journey progress", "where you are on the map, and for each board you've played: its stars, time, "
       "score and the words you found", "So you can pick up your journey and replay boards.",
       "Clear the app's storage, or uninstall the app."),
      ("Leaderboard", "your best Quick Play runs and their points, and Pass & Play standings: player names, "
       "games won and points", "To show your best runs and who's ahead.", "Clear the app's storage, or uninstall the app."),
      ("Settings", "sound, music and haptics on or off and their volumes", "So the app sounds the way you set it.",
       "Clear the app's storage, or uninstall the app."),
      ("Ad consent choice", "stored by Google's consent library", "To remember your answer and not ask again.",
       "Change it under Settings → Ad privacy options."),
    ],
    name_note=True,
    ads_where="at the bottom of the main menu and the journey map",
    ads_extra=("You can also choose to watch a <b>rewarded video ad</b> to earn an extra hint, or an extra minute "
               "and a hint to keep a board going. These only play when you tap to watch one; the game never "
               "shows them on its own, and nothing interrupts a board."),
    consent="Settings → Ad privacy options",
    haptics="The small taps you feel as you trace a word. Turn it off with Settings → Haptics.",
    offline="The game itself, including its word list, is on your phone and works fully offline; "
            "only ads need a connection.",
    delete="The app has no in-app reset. To remove everything it stores, clear its storage "
           "(Android Settings → Apps → World of Words → Storage → Clear storage) or uninstall it.",
    children="World of Words is a word game suitable for all ages",
  ),
}

CSS = """
  :root {{
    color-scheme: light;
    --ink: {ink}; --body: {body_ink}; --muted: {muted}; --card: {card}; --hair: {hair};
    --accent: {accent}; --link: {link}; --marker: {marker}; --tint: {tint}; --tint-ink: {tint_ink};
    --shadow: 0 3px 14px rgba(20,24,40,.07), 0 1px 2px rgba(20,24,40,.05);
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; color: var(--ink); min-height: 100vh; background: {bg};
    font-family: {body_font}; line-height: 1.6;
    display: flex; justify-content: center; padding: 28px 16px 56px;
  }}
  main {{ width: 100%; max-width: 720px; }}
  a {{ color: var(--link); text-underline-offset: 3px; }}
  .brand {{ display: flex; align-items: center; gap: 14px; }}
  .mark {{ width: 58px; height: 58px; flex: none; border-radius: 16px; overflow: hidden; box-shadow: var(--shadow); }}
  .mark img {{ display: block; width: 100%; height: 100%; }}
  .word {{ font: {display_28}; letter-spacing: -.01em; line-height: 1.05; }}
  .sub {{ font-weight: 700; font-size: 12px; letter-spacing: .28em; color: {wordmark_sub}; text-transform: uppercase; margin-top: 4px; }}
  .eyebrow {{ display: inline-block; font-weight: 700; font-size: 11px; letter-spacing: .18em;
    text-transform: uppercase; color: var(--tint-ink); background: var(--tint); padding: 5px 11px; border-radius: 99px; }}
  h1 {{ margin: 12px 0 0; font: {display_h1}; line-height: 1.1; letter-spacing: -.02em; }}
  h2 {{ margin: 0 0 10px; font: {display_22}; letter-spacing: -.01em; }}
  h3 {{ margin: 22px 0 6px; font-size: 15px; font-weight: 700; }}
  p, li {{ color: var(--body); }}
  p {{ margin: 0 0 12px; }}
  ul {{ margin: 0 0 12px; padding-left: 20px; }}
  li {{ margin-bottom: 7px; }}
  li::marker {{ color: var(--marker); }}
  b, strong {{ color: var(--ink); }}
  .card {{ background: var(--card); border-radius: 18px; padding: 22px; margin-top: 16px; box-shadow: var(--shadow); }}
  .card.lead {{ background: {lead}; box-shadow: 0 10px 24px {lead_shadow}, inset 0 1px 0 rgba(255,255,255,.3); }}
  .card.lead h2, .card.lead b {{ color: #fff; }}
  .card.lead p, .card.lead li {{ color: rgba(255,255,255,.88); }}
  .card.lead li::marker {{ color: rgba(255,255,255,.7); }}
  .glance {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 16px; }}
  .glance div {{ background: var(--card); border-radius: 15px; padding: 14px 16px 14px 18px; box-shadow: var(--shadow); border-left: 5px solid var(--c); }}
  .glance div:nth-child(1) {{ --c: {c1}; }} .glance div:nth-child(2) {{ --c: {c2}; }} .glance div:nth-child(3) {{ --c: {c3}; }}
  .glance b {{ display: block; font-size: 15px; margin-bottom: 3px; }}
  .glance span {{ font-size: 13px; color: var(--body); }}
  nav.toc {{ margin-top: 16px; display: flex; flex-wrap: wrap; gap: 8px; }}
  nav.toc a {{ font-weight: 700; font-size: 12px; text-decoration: none; color: var(--ink);
    border-radius: 99px; padding: 7px 13px; background: var(--card); box-shadow: 0 2px 6px rgba(20,24,40,.10); }}
  nav.toc a:hover {{ background: var(--tint); color: var(--tint-ink); }}
  table {{ width: 100%; border-collapse: collapse; margin: 10px 0 14px; font-size: 14px; }}
  th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid var(--hair); vertical-align: top; }}
  th {{ font-weight: 700; font-size: 11px; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); }}
  td {{ color: var(--body); }}
  td b {{ color: var(--ink); }}
  /* Narrow screens: a table row becomes a small labelled block instead of squeezed columns. */
  @media (max-width: 560px) {{
    table, tbody, tr, td {{ display: block; width: 100%; }}
    thead {{ display: none; }}
    tr {{ border-bottom: 1px solid var(--hair); padding: 12px 0; }}
    tr:last-child {{ border-bottom: 0; }}
    td {{ border: 0; padding: 0 0 6px; }}
    td:last-child {{ padding-bottom: 0; }}
    td::before {{ content: attr(data-label); display: block; font-weight: 700; font-size: 11px;
      letter-spacing: .12em; text-transform: uppercase; color: var(--muted); margin-bottom: 2px; }}
  }}
  .stamp {{ font-size: 12px; font-weight: 500; color: var(--muted); margin-top: 10px; }}
  footer {{ margin-top: 30px; font-size: 13px; color: var(--muted); text-align: center; }}
  footer a {{ margin: 0 8px; color: var(--body); }}
"""

def page(slug, a):
    t = a["theme"]; name = a["name"]; e = html.escape
    css = CSS.format(bg=t["bg"], body_font=t["body"], ink=t["ink"], body_ink=t["body_ink"], muted=t["muted"],
        card=t["card"], hair=t["hair"], accent=t["accent"], link=t["link"], marker=t["marker"], tint=t["tint"],
        tint_ink=t["tint_ink"], lead=t["lead"], lead_shadow=t["lead_shadow"], c1=t["c1"], c2=t["c2"], c3=t["c3"],
        wordmark_sub=t["wordmark_sub"], display_28=t["display"].format(size="28px"),
        display_h1=t["display"].format(size="clamp(30px, 8vw, 44px)"), display_22=t["display"].format(size="22px"))
    rows = "\n".join(
        f'      <tr><td data-label="What"><b>{e(w)}</b><br>{e(d)}</td>\n'
        f'        <td data-label="Why">{e(why)}</td>\n        <td data-label="Remove">{e(rm)}</td></tr>'
        for w, d, why, rm in a["stored"])
    word = name.replace(" Mini", "")
    sub = "mini" if name.endswith("Mini") else "a fungrid game"
    play = (f'<a href="{a["play"]}">{e(name)} on Google Play</a> · ' if a["play"] else "")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(name)} · Privacy Policy</title>
<meta name="description" content="How {e(name)} handles your data: names, scores and settings stay on your phone, and ads come from Google AdMob.">
<meta property="og:title" content="{e(name)} · Privacy Policy">
<meta property="og:description" content="Everything you play stays on your phone. No accounts, no analytics.">
<meta property="og:type" content="website">
<meta name="theme-color" content="{t['theme_color']}">
<meta name="color-scheme" content="light">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{t['fonts']}&display=swap" rel="stylesheet">
<style>
  /* {e(name)}'s own look, from the app's colors.xml and fonts. Light only, like the app.
     Generated with the other policies; edit the generator's copy, not just this page. */{css}</style>
</head>
<body>
<main>
  <div class="brand">
    <span class="mark"><img src="../../games/{a['icon']}" width="58" height="58" alt=""></span>
    <div><div class="word">{e(word)}</div><div class="sub">{e(sub)}</div></div>
  </div>

  <div class="eyebrow" style="margin-top:30px">Privacy policy</div>
  <h1>Your game stays on your phone</h1>
  <div class="stamp">Last updated {DATE} · applies to {e(name)} for Android ({a['package']})</div>

  <div class="card lead">
    <h2>The short version</h2>
    <ul>
      <li><b>No account, no sign-in.</b> We never ask who you are.</li>
      <li><b>We collect nothing.</b> The names you type, your scores and your settings are saved on your phone and never sent to us.</li>
      <li><b>Ads are the one exception.</b> Google AdMob shows the ads and processes data for them, under Google's own policy.</li>
      <li><b>You stay in control.</b> Change your ad choices in Settings, clear the app's storage, or uninstall to erase everything.</li>
    </ul>
  </div>

  <div class="glance">
    <div><b>No sign-in</b><span>No email, contacts or location. Player names never leave your phone.</span></div>
    <div><b>No analytics</b><span>No tracking of how you play.</span></div>
    <div><b>Ads by Google</b><span>AdMob, with a consent choice where required.</span></div>
  </div>

  <nav class="toc">
    <a href="#who">Who we are</a>
    <a href="#device">Stored on your phone</a>
    <a href="#collect">What we collect</a>
    <a href="#ads">Ads</a>
    <a href="#site">This website</a>
    <a href="#permissions">Permissions</a>
    <a href="#children">Children</a>
    <a href="#rights">Your choices</a>
    <a href="#contact">Contact</a>
  </nav>

  <div class="card" id="who">
    <h2>Who we are</h2>
    <p>{e(name)} is made by <b>fungrid</b>, an independent app developer. In this policy, "we" and "us"
      mean fungrid, and "the app" means {e(name)} for Android. We are the data controller for the
      limited processing described here.</p>
    <p>Questions about privacy: <a href="mailto:fungridapp@gmail.com">fungridapp@gmail.com</a>.</p>
  </div>

  <div class="card" id="device">
    <h2>What the app stores on your phone</h2>
    <p>All of this is kept in the app's private storage on your device. It never leaves your phone,
      and nobody — including us — can read it from anywhere else.</p>
    <table>
      <thead><tr><th>What</th><th>Why</th><th>How to remove it</th></tr></thead>
{rows}
    </table>
    <p>A name is only a label for the game. You can type a nickname or anything you like; it is
      never checked, uploaded or shared.</p>
    <p>If Android Backup is switched on for your phone, Android may include the app's saved settings
      and progress in your own Google account backup. That backup belongs to you and is governed by
      Google's privacy policy; we cannot read it.</p>
  </div>

  <div class="card" id="collect">
    <h2>What we collect</h2>
    <p><b>Nothing.</b> The app has no servers, no accounts and no analytics. We do not collect your
      name, email address, phone number, contacts, photos, location or device identifiers, and we do
      not build a profile of you. We receive no reports about how you play.</p>
    <p>Two things sit outside that, and both are handled by Google rather than by us:</p>
    <ul>
      <li><b>Ads</b>, described below.</li>
      <li><b>Google Play</b> may give us anonymous, aggregated statistics about installs, uninstalls,
        ratings and crashes for the app as a whole, if your Android settings allow it. These are
        counts and technical reports, not information about you, and we cannot identify anyone from them.</li>
    </ul>
  </div>

  <div class="card" id="ads">
    <h2>Ads</h2>
    <p>The app is free and shows <b>banner ads</b> through <b>Google AdMob</b>, {a['ads_where']}.
      {a['ads_extra']}</p>
    <p>To serve those ads, Google may process data such as your <b>advertising ID</b>, IP address
      (which gives approximate, city-level location), device model and operating system version,
      the app you are using, and your interactions with the ad. Google acts as an independent
      controller for this. What Google does with it is set out in
      <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google's Privacy Policy</a>
      and in <a href="https://business.safety.google/privacy/" target="_blank" rel="noopener">how Google uses data from sites and apps that use its services</a>.</p>
    <h3>Your consent</h3>
    <p>Where the law requires it — in the European Economic Area, the United Kingdom and Switzerland —
      the app shows Google's consent form the first time you open it, and asks whether ads may be
      personalised. Your answer is remembered, and you can change it at any time under
      <b>{e(a['consent'])}</b> inside the app. If you decline, ads still appear, but they
      are not personalised.</p>
    <h3>Opting out on your device</h3>
    <ul>
      <li>Android: <b>Settings → Privacy → Ads</b>, where you can delete or reset your advertising ID
        and turn off ad personalisation for every app.</li>
      <li>Google account holders: <a href="https://myadcenter.google.com" target="_blank" rel="noopener">My Ad Center</a>.</li>
    </ul>
  </div>

  <div class="card" id="site">
    <h2>This website</h2>
    <p>These pages are static and hosted on <b>GitHub Pages</b>. There are no cookies, no analytics
      and no trackers.</p>
    <ul>
      <li>GitHub serves the pages and, like any web host, may log technical details such as your IP
        address and browser for security and abuse prevention. See the
        <a href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" target="_blank" rel="noopener">GitHub Privacy Statement</a>.</li>
      <li>The pages load fonts from <b>Google Fonts</b>, so your browser contacts Google's servers and
        Google receives your IP address in doing so.</li>
    </ul>
  </div>

  <div class="card" id="permissions">
    <h2>Permissions the app requests</h2>
    <table>
      <thead><tr><th>Permission</th><th>What it's for</th></tr></thead>
      <tr><td data-label="Permission"><b>Internet</b>, <b>network state</b></td><td data-label="What for">Loading ads. {e(a['offline'])}</td></tr>
      <tr><td data-label="Permission"><b>Vibrate</b></td><td data-label="What for">{e(a['haptics'])}</td></tr>
      <tr><td data-label="Permission"><b>Advertising ID</b> and related ad services</td><td data-label="What for">Added by Google's ads library so ads can be shown and measured.</td></tr>
    </table>
    <p>The app asks for no runtime permissions at all: no camera, microphone, location, contacts,
      photos or files.</p>
  </div>

  <div class="card" id="children">
    <h2>Children</h2>
    <p>{e(a['children'])}, but it is not directed at children under 13,
      and we do not knowingly collect any personal information from children. Because the app shows
      ads, a parent or guardian should decide whether it is appropriate for their child. If you
      believe a child has provided personal information through the app, write to us and we will help;
      in practice any name typed into the app stays on that phone and never reaches us.</p>
  </div>

  <div class="card" id="rights">
    <h2>Your choices and rights</h2>
    <ul>
      <li><b>Delete your data.</b> {e(a['delete'])}</li>
      <li><b>Change your ad choices</b> at any time under {e(a['consent'])}.</li>
      <li><b>Play without ads loading</b> by switching off your connection; the game works offline.</li>
      <li><b>Access, correction, deletion, portability and objection.</b> Under laws such as the GDPR and
        the CCPA/CPRA you have rights over personal data held about you. We hold none, so there is
        nothing for us to hand over or delete. For data processed by Google for ads, use the Google
        links above or contact Google directly.</li>
      <li><b>We do not sell or share your personal information</b>, and never have.</li>
    </ul>
    <p>Data is kept only on your device, for as long as you keep the app installed. We run no servers
      and hold no backups of your data.</p>
  </div>

  <div class="card" id="contact">
    <h2>Changes and contact</h2>
    <p>If this policy changes, the updated version appears on this page with a new date at the top.
      Significant changes will also be noted in the app's store listing.</p>
    <p>Questions, requests or concerns: <a href="mailto:fungridapp@gmail.com">fungridapp@gmail.com</a>.
      We aim to reply within a few days.</p>
  </div>

  <footer>
    <a href="../../">fungrid</a> · {play}<a href="../../privacy/">All privacy policies</a><br>
    <span style="opacity:.7">© 2026 fungrid</span>
  </footer>
</main>
</body>
</html>
"""

for slug, a in APPS.items():
    d = f"{SITE}/{slug}/privacypolicy"; os.makedirs(d, exist_ok=True)
    open(f"{d}/index.html", "w").write(page(slug, a))
    print("wrote", f"{slug}/privacypolicy/index.html")
