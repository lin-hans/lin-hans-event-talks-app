import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
from flask import Flask, jsonify, render_template

app = Flask(__name__)

FEED_URL = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"

def fetch_and_parse_feed():
    try:
        # Fetch XML from URL
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(FEED_URL, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
        
        # Parse XML
        root = ET.fromstring(xml_data)
        
        # Define namespace map for Atom
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entries = []
        for entry_elem in root.findall('atom:entry', ns):
            title_elem = entry_elem.find('atom:title', ns)
            id_elem = entry_elem.find('atom:id', ns)
            updated_elem = entry_elem.find('atom:updated', ns)
            content_elem = entry_elem.find('atom:content', ns)
            link_elem = entry_elem.find("atom:link[@rel='alternate']", ns)
            if link_elem is None:
                link_elem = entry_elem.find("atom:link", ns)
                
            title = title_elem.text if title_elem is not None else ""
            entry_id = id_elem.text if id_elem is not None else ""
            updated = updated_elem.text if updated_elem is not None else ""
            content = content_elem.text if content_elem is not None else ""
            link = link_elem.attrib.get('href', '') if link_elem is not None else ""
            
            entries.append({
                'id': entry_id,
                'title': title,
                'updated': updated,
                'link': link,
                'content': content
            })
            
        return entries, None
    except urllib.error.URLError as e:
        return None, f"Failed to fetch feed: {str(e)}"
    except ET.ParseError as e:
        return None, f"Failed to parse XML: {str(e)}"
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/releases')
def releases():
    entries, error = fetch_and_parse_feed()
    if error:
        return jsonify({'success': False, 'error': error}), 500
    return jsonify({'success': True, 'entries': entries})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
