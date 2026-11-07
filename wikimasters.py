import os
from datetime import datetime
from playwright.sync_api import sync_playwright

URL_LOGIN = "https://www.wiki-masters.com/login"      # à adapter
URL_PAGE = "https://www.wiki-masters.com/pulls"
URL_OPEN = "https://www.wiki-masters.com/api/packs/open"
ATTENTE = 3600 + 30          # marge de 30 s au cas où le délai serait de 1 h pile
PROFIL = os.path.abspath("profil_playwright")

USER = os.environ.get("USER")
MDP = os.environ.get("MDP")


def log(*args):
    print(datetime.now().strftime("%d/%m %H:%M:%S"), *args, flush=True)


def se_connecter(page):
    """À adapter après inspection de ta page de login."""
    page.goto(URL_LOGIN)
    page.fill("input[type='email']", USER)
    page.fill("input[type='password']", MDP)
    page.click("button[type='submit']")
    page.wait_for_url("**/pulls**", timeout=30000)    # URL attendue après connexion
    log("Connexion effectuée")


def ouvrir_paquet(page):
    page.goto(URL_PAGE)
    page.wait_for_timeout(3000)
    r = page.request.post(URL_OPEN)
    if r.status == 401:                       # session expirée -> on se reconnecte et on réessaie
        log("401 : session expirée, reconnexion")
        se_connecter(page)
        page.goto(URL_PAGE)
        page.wait_for_timeout(3000)
        r = page.request.post(URL_OPEN)
    log(r.status, r.text()[:300])
    return r


with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=PROFIL,
        channel="chrome",          # utilise ton Chrome installé ; retire cette ligne pour utiliser Chromium
        headless=False,
    )
    page = ctx.pages[0] if ctx.pages else ctx.new_page()

    while True:
        try:
            ouvrir_paquet(page)
        except Exception as e:
            log("Erreur :", e)
        page.wait_for_timeout(ATTENTE * 1000)   # attente compatible avec Playwright