# book-of-fermoy
English translation 
# Book of Fermoy — Gaelic Viewer & Translator

Streamlit app for browsing **all pages** of RIA MS 23 E 29 (The Book of Fermoy) with high-resolution images, plus spaces for Irish transcription and English translation.

## Deploy (iPhone-friendly)
1. Create a new public GitHub repo named `book-of-fermoy`.
2. Upload or paste these three files into the root:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. Go to [share.streamlit.io](https://share.streamlit.io), connect the repo, and set the main file to `app.py`.
4. Deploy. The app loads every page image directly from the official IIIF server.

## Features
- All ~240 pages + boards (images served live from ISOS)
- Page slider / dropdown navigation
- Zoomable high-res image
- Irish transcription box + English translation box (session state)
- Known contents outline in the sidebar
- Mobile-friendly layout

## Sources
Images © Royal Irish Academy via [Irish Script on Screen](https://www.isos.dias.ie/RIA/RIA_MS_23_E_29.html).  
IIIF base: `https://iiif.isos.dias.ie/iiif/2/RIA%2FRIA_MS_23_E_29%2F`

Your own notes/translations can be licensed however you like (suggested: CC BY 4.0).
