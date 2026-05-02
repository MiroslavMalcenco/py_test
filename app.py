from __future__ import annotations

from flask import Flask, Response

app = Flask(__name__)


@app.get("/")
def index() -> Response:
    emoji = "🐍"
    html = f"""<!doctype html>
<html lang=\"ru\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>Emoji</title>
    <style>
      html, body {{
        height: 100%;
        margin: 0;
      }}
      body {{
        display: grid;
        place-items: center;
        background: #ffffff;
      }}
      .emoji {{
        font-size: min(60vmin, 360px);
        line-height: 1;
        user-select: none;
      }}
    </style>
  </head>
  <body>
    <div class=\"emoji\" aria-label=\"emoji\">{emoji}</div>
  </body>
</html>"""
    return Response(html, mimetype="text/html; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
