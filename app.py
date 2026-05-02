from __future__ import annotations

from flask import Flask, Response

app = Flask(__name__)


@app.get("/")
def index() -> Response:
    html = """<!doctype html>
<html lang=\"ru\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>Emoji</title>
    <style>
      html, body {
        margin: 0;
        padding: 0;
      }
      body {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: #ffffff;
      }
      .smiley {
        width: 120px;
        height: 120px;
        flex-shrink: 0;
      }
    </style>
  </head>
  <body>
    <svg
      class="smiley"
      viewBox="0 0 200 200"
      role="img"
      aria-label="smiley"
      xmlns="http://www.w3.org/2000/svg"
    >
      <defs>
        <radialGradient id="faceGradient" cx="40%" cy="40%">
          <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#FFA500;stop-opacity:1" />
        </radialGradient>
        <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
          <feDropShadow dx="0" dy="8" stdDeviation="6" flood-opacity="0.3" />
        </filter>
      </defs>
      <!-- Face -->
      <circle cx="100" cy="100" r="92" fill="url(#faceGradient)" filter="url(#shadow)" />
      <!-- Left eye -->
      <circle cx="70" cy="75" r="14" fill="#000" />
      <circle cx="72" cy="70" r="5" fill="#fff" opacity="0.6" />
      <!-- Right eye -->
      <circle cx="130" cy="75" r="14" fill="#000" />
      <circle cx="132" cy="70" r="5" fill="#fff" opacity="0.6" />
      <!-- Mouth -->
      <path d="M 65 125 Q 100 155 135 125" fill="none" stroke="#000" stroke-width="8" stroke-linecap="round" />
    </svg>
  </body>
</html>"""
    return Response(html, mimetype="text/html; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
