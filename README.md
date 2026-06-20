# BigQuery Release Notes Hub

A premium, modern web dashboard to fetch, search, filter, and draft tweets from Google Cloud BigQuery release notes. 

Built with **Python Flask** on the server side and **Vanilla HTML/CSS/JS** on the client side, this application parses the official Google Cloud BigQuery release notes Atom feed and transforms the raw HTML updates into categorized, searchable cards. It also features a built-in tweet composer to help you share critical Google Cloud updates to X (formerly Twitter) with a single click.

---

## 🌟 Key Features

- **Live XML Feed Fetcher:** Fetches and parses the official BigQuery Release Notes feed in real-time.
- **Categorization & Labeling:** Automatically classifies release entries into distinct types:
  - `Feature` (New capabilities)
  - `Announcement` (General announcements)
  - `Issue` (Known issues or bug reports)
  - `Breaking` (Critical breaking changes)
  - `Change` (General modifications or updates)
- **Instant Search & Filter:** Filter updates by type or search through contents in real-time via client-side indexing.
- **Auto-Draft Tweet Composer:** Select any update card, and the composer will instantly generate a formatted tweet draft within the 280-character limit, complete with links and hashtags.
- **Elegant Dark-Mode UI:** Premium dark-themed dashboard using a glassmorphic (frosted glass) design system with Outfit typography.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, `xml.etree.ElementTree` (Standard XML library)
- **Frontend:** Vanilla HTML5, Vanilla CSS3 (Custom design tokens, Flexbox/CSS Grid), Vanilla JS (ES6+, DOMParser, Fetch API)
- **Deployment & Source Control:** Git, GitHub

---

## 📂 File Structure

```text
bigquery_notes_app/
├── app.py                 # Flask server & XML parsing engine
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
└── templates/
    └── index.html         # Frontend structure, styling, and application logic
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed.

### Installation

1. Clone the repository (or copy the project directory):
   ```bash
   git clone https://github.com/lin-hans/lin-hans-event-talks-app.git
   cd lin-hans-event-talks-app
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install Flask:
   ```bash
   pip install flask
   ```

### Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will start locally. Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```

---

## 🔄 How It Works

1. **Request Feed:** When you open the web app or click **Refresh Notes**, the client triggers a `GET` request to `/api/releases`.
2. **Fetch and Parse XML:** The Flask server fetches the raw RSS/Atom XML from Google Cloud, parses it with `ElementTree`, extracts the key details (`id`, `title`, `content`, `link`), and returns it to the client as a clean JSON payload.
3. **Parse HTML Content:** The frontend uses `DOMParser` to parse the HTML inside each entry, separating the update items by `<h3>` tags and identifying the update type.
4. **Draft Tweets:** Clicking any card extracts the text, trims it to fit the 280-character limit, prepends the date and type metadata, and appends the source link with default hashtags. Clicking **Tweet** opens a new tab directed to the official Twitter/X tweet compiler page.
