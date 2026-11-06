from playwright.sync_api import sync_playwright
from datetime import datetime
import time

URL_PAGE = "https://www.wiki-masters.com/pulls"
URL_OPEN = "https://www.wiki-masters.com/api/packs/open"
ATTENTE = 3600  # secondes entre deux ouvertures

with sync_playwright() as p:
    navigateur = p.chromium.connect_over_cdp("http://localhost:9222")
    ctx = navigateur.contexts[0]
    page = ctx.new_page()

    while True:
        try:
            page.goto(URL_PAGE)            # recharge la page : le site renouvelle la connexion
            page.wait_for_timeout(3000)
            r = page.request.post(URL_OPEN)
            print(datetime.now().strftime("%H:%M:%S"), r.status, r.text()[:500])
        except Exception as e:
            print(datetime.now().strftime("%H:%M:%S"), "Erreur :", e)
        time.sleep(ATTENTE)





"""

curl --url 'https://www.wiki-masters.com/api/packs/open' \
  -X 'POST' \
  -H 'accept: */*' \
  -H 'accept-language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'content-length: 0' \
  -b 'sb-cyrxjeppjqsxxjayfrur-auth-token.0=base64-eyJhY2Nlc3NfdG9rZW4iOiJleUpoYkdjaU9pSkZVekkxTmlJc0ltdHBaQ0k2SWpSak16UTNOVEEwTFdRNVlUVXROR0V3TVMxaU56Qm1MV1E0TXpGaFlUWTBOalF3WkNJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaFlXd2lPaUpoWVd3eElpd2lZVzF5SWpwYmV5SnRaWFJvYjJRaU9pSnZkSEFpTENKMGFXMWxjM1JoYlhBaU9qRTNPVFF3TURJNE9EZDlYU3dpWVhCd1gyMWxkR0ZrWVhSaElqcDdJbkJ5YjNacFpHVnlJam9pWlcxaGFXd2lMQ0p3Y205MmFXUmxjbk1pT2xzaVpXMWhhV3dpWFgwc0ltRjFaQ0k2SW1GMWRHaGxiblJwWTJGMFpXUWlMQ0psYldGcGJDSTZJbWR2Ym5SeVlXNWtkV04wYVdKc1pVQm5iV0ZwYkM1amIyMGlMQ0psZUhBaU9qRTNPVFF3TURZME9EY3NJbWxoZENJNk1UYzVOREF3TWpnNE55d2lhWE5mWVc1dmJubHRiM1Z6SWpwbVlXeHpaU3dpYVhOZmNISnZJanBtWVd4elpTd2lhWE56SWpvaWFIUjBjSE02THk5amVYSjRhbVZ3Y0dweGMzaDRhbUY1Wm5KMWNpNXpkWEJoWW1GelpTNWpieTloZFhSb0wzWXhJaXdpY0dodmJtVWlPaUlpTENKeWIyeGxJam9pWVhWMGFHVnVkR2xqWVhSbFpDSXNJbk5sYzNOcGIyNWZhV1FpT2lJeU1URXdOMkkyTWkwMllUSXpMVFEwTjJZdFlUWTRaQzFpWXpReVl6Tm1ZakExWlRNaUxDSnpkV0lpT2lJNU1UazNNemxpWkMxa1pHSTBMVFEyTm1NdE9EY3hNaTB4TVRnelpXWTBZakJtTTJZaUxDSjFjMlZ5WDIxbGRHRmtZWFJoSWpwN0ltVnRZV2xzSWpvaVoyOXVkSEpoYm1SMVkzUnBZbXhsUUdkdFlXbHNMbU52YlNJc0ltVnRZV2xzWDNabGNtbG1hV1ZrSWpwMGNuVmxMQ0p1YzJaM1gyTnZiblJsYm5SZllXTnJJanAwY25WbExDSnZkbVZ5WHpFNFgyRmpheUk2ZEhKMVpTd2ljR2h2Ym1WZmRtVnlhV1pwWldRaU9tWmhiSE5sTENKeWRXeGxjMTloWTJzaU9uUnlkV1VzSW5OMVlpSTZJamt4T1Rjek9XSmtMV1JrWWpRdE5EWTJZeTA0TnpFeUxURXhPRE5sWmpSaU1HWXpaaUlzSW5SbGNtMXpYMkZqYXlJNmRISjFaU3dpZFhObGNtNWhiV1VpT2lKM2FXdHBaVzV3WlhSaGNtUWlmWDAuYmlHVlNnZWVxQ0Q3MVBWdm5FX0M3M0dqa0xaMjN0OERub3IzeWxvMWdmQzlESFNhU2FPUHNrNXBHWHhJN1BSWjZ2d3FhZnpzOGtzeWExMVJ2NG03Y3ciLCJ0b2tlbl90eXBlIjoiYmVhcmVyIiwiZXhwaXJlc19pbiI6MzYwMCwiZXhwaXJlc19hdCI6MTc5NDAwNjQ4NywicmVmcmVzaF90b2tlbiI6ImQ2cXhpNWRheG4zaCIsInVzZXIiOnsiaWQiOiI5MTk3MzliZC1kZGI0LTQ2NmMtODcxMi0xMTgzZWY0YjBmM2YiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJlbWFpbCI6ImdvbnRyYW5kdWN0aWJsZUBnbWFpbC5jb20iLCJlbWFpbF9jb25maXJtZWRfYXQiOiIyMDI2LTEwLTA3VDA3OjA3OjAzLjIxNzU3M1oiLCJwaG9uZSI6IiIsImNvbmZpcm1lZF9hdCI6IjIwMjYtMTAtMDdUMDc6MDc6MDMuMjE3NTczWiIsImxhc3Rfc2lnbl9pbl9hdCI6IjIwMjYtMTEtMDZUMjI6MDg6MDcuODI1MDhaIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJnb250cmFuZHVjdGlibGVAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5zZndfY29udGVudF9hY2siOnRydWUsIm92ZXJfMThfYWNrIjp0cnVlLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInJ1bGVzX2FjayI6dHJ1ZSwic3ViIjoiOTE5NzM5YmQtZGRiNC00NjZjLTg3MTItMTE4M2VmNGIwZjNmIiwidGVybXNfYWNrIjp0cnVlLCJ1c2VybmFtZSI6Indpa2llbnBldGFyZCJ9LCJpZGVudGl0aWVzIjpbeyJpZGVudGl0eV9pZCI6IjAyMzEzNGI4LTZhNTctNDVkZC05OWI4LTFmZmFkODQ5YmEzMSIsImlkIjoiOTE5NzM5YmQtZGRiNC00NjZjLTg3MTItMTE4M2VmNGIwZjNmIiwidXNlcl9pZCI6IjkxOTczOWJkLWRkYjQtNDY2Yy04NzEyLTExODNlZjRiMGYzZiIsImlkZW50aXR5X2RhdGEiOnsiZW1haWwiOiJnb250cmFuZHVjdGlibGVAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5zZndfY29udGVudF9hY2siOnRydWUsIm92ZXJfMThfYWNrIjp0cnVlLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInJ1bGVzX2FjayI6dHJ1ZSwic3ViIjoiOTE5NzM5YmQtZGRiNC00NjZjLTg3MTItMTE4M2VmNGIwZjNmIiwidGVybXNfYWNrIjp0cnVlLCJ1c2VybmFtZSI6Indpa2llbnBldGFyZCJ9LCJwcm92aWRlciI6ImVtYWlsIiwibGFzdF9zaWduX2luX2F0IjoiMjAyNi0xMC0wN1QwNzowNjozNi41MDU5OFoiLCJjcmVhdGVkX2F0IjoiMjAyNi0xMC0wN1QwNzowNjozNi41MDYwMjNaIiwidXBkYXRlZF9hdCI6IjIwMjYtMTAtMDdUMDc6MDY6MzYuNTA2MDIzWiIsImVtYWlsIjoiZ29udHJhbmR1Y; sb-cyrxjeppjqsxxjayfrur-auth-token.1=3RpYmxlQGdtYWlsLmNvbSJ9XSwiY3JlYXRlZF9hdCI6IjIwMjYtMTAtMDdUMDc6MDY6MzYuNDk5Mjk0WiIsInVwZGF0ZWRfYXQiOiIyMDI2LTExLTA2VDIyOjA4OjA4LjE3MjEyMVoiLCJpc19hbm9ueW1vdXMiOmZhbHNlfX0' \
  -H 'origin: https://www.wiki-masters.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.wiki-masters.com/pulls' \
  -H 'sec-ch-ua: "Not:A-Brand";v="8", "Chromium";v="156", "Google Chrome";v="156"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36'


curl --url 'https://www.etc...' \
  -X 'POST' \
  -H 'accept: */*' \
  -H 'accept-language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'content-length: 0' \
  -b 'sb-nombres_et_chiffres-auth-token.0=nombres_et_chiffres-; sb-nombres_et_chiffres-auth-token.1=nombres_et_chiffres' \
  -H 'origin: https://www.etc....com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.etc....com/une_action' \
  -H 'sec-ch-ua: "Not:A-Brand";v="8", "Chromium";v="156", "Google Chrome";v="156"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36'


"""


