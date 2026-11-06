## connexion manuelle, ouverture automatisée

1. Ferme tous les Chrome ouverts, puis lance Chrome avec le port de débogage. Sous Windows (Invite de commandes ou Win+R) :

bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome-debug"

Le --user-data-dir est obligatoire : depuis Chrome 136, le port de débogage est ignoré si tu utilises ton profil par défaut. Ce profil C:\chrome-debug est un profil vierge, donc tu devras t’y reconnecter. Ensuite, il garde ta session.

2. Vérifie que le port répond. Dans un navigateur, ouvre http://localhost:9222/json/version. Tu dois voir un petit texte JSON. Sinon, Chrome n’a pas été lancé correctement (ou une autre fenêtre Chrome utilise déjà ce profil).

3. Dans cette fenêtre Chrome, connecte-toi à wiki-masters.com et laisse-la ouverte.

4. Lance ton script depuis un terminal (python mon_script.py) avec l’environnement activé.
