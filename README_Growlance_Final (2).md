
# 🌱 Growlance – Beta Finanzplaner mit Paketlogik

Growlance ist eine Web-App für junge Menschen zur Strukturierung ihrer Finanzen.  
Diese Beta-Version beinhaltet:

- Nutzer-Login über Supabase (E-Mail-basiert)
- Sparziel, Einnahmen, Ausgaben + Fortschrittsanzeige
- Unterschiedliche Funktionsstufen: **Basic, Pro, Family**
- Steuerplaner & KI-Challenges in Pro/Family
- DSGVO-freundlich, keine Bankverknüpfung nötig

---

## 🚀 Startanleitung

### 📁 Projektstruktur

```
growlance/
├── growlance_beta_app.py            # Haupt-App
├── requirements_growlance.txt       # Abhängigkeiten
├── .streamlit/
│   └── config.toml                  # App-Styling
└── README.md
```

---

## ☁️ Streamlit Cloud starten

1. Forke dieses Repository oder kopiere alle Dateien
2. Gehe auf [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Melde dich mit GitHub an
4. Wähle dein Repo, Datei: `growlance_beta_app.py`
5. ✅ Deploy starten – fertig!

---

## 🧩 Funktionen je nach Paket

| Funktion              | Basic | Pro | Family |
|-----------------------|:-----:|:---:|:------:|
| 1 Konto speichern     | ✅    | ✅ (bis 3) | ✅ (bis 7) |
| CSV-Export            | ✅    | ✅   | ✅       |
| Steuerplaner          | ❌    | ✅   | ✅       |
| KI-Challenges         | ❌    | ✅   | ✅       |

---

## 🔐 Supabase Setup

1. Erstelle ein Projekt unter [https://supabase.com](https://supabase.com)
2. Ersetze im Code:
   ```python
   url = "https://DEIN.supabase.co"
   key = "DEIN-ANON-KEY"
   ```
3. Lege eine Tabelle `finanzdaten` mit Feldern an:  
   `email (text), ziel (int), einnahmen (int), ausgaben (int), bisher (int), paket (text)`

---

## 💬 Feedback

Diese Beta ist für Testzwecke – Feedback & Bugs gerne an den Entwickler senden!

