from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/zeeslag')
def zeeslag():
    return render_template('zeeslag.html')

@app.route('/tank-game')
def tank_game():
    return render_template('tank_game.html')

@app.route('/tetris')
def tetris():
    return render_template('tetris.html')

@app.route('/boter-kaas-eieren')
def boter_kaas_eieren():
    return render_template('boter_kaas_eieren.html')

@app.route('/space-invaders')
def space_invaders():
    return render_template('space_invaders.html')

@app.route('/cookiebeleid')
def cookiebeleid():
    return render_template('cookiebeleid.html')

@app.route('/sitemap.xml')
def sitemap():
    pages = [
        ('/', '2026-07-05', '1.0'),
        ('/zeeslag', '2026-07-05', '0.9'),
        ('/tank-game', '2026-07-05', '0.9'),
        ('/tetris', '2026-07-05', '0.9'),
        ('/boter-kaas-eieren', '2026-07-05', '0.9'),
        ('/space-invaders', '2026-07-07', '0.9'),
        ('/cookiebeleid', '2026-07-05', '0.5'),
    ]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for loc, lastmod, priority in pages:
        xml += f'  <url>\n    <loc>https://gamesfromai.com{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'
    xml += '</urlset>'
    return Response(xml, mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    txt = 'User-agent: *\n'
    txt += 'Allow: /\n'
    txt += 'Sitemap: https://gamesfromai.com/sitemap.xml\n'
    return Response(txt, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)