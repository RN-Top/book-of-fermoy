import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Book of Fermoy",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# IIIF base for RIA MS 23 E 29
IIIF_BASE = "https://iiif.isos.dias.ie/iiif/2/RIA%2FRIA_MS_23_E_29%2F"

# Approximate total canvases from the public manifest (boards + pages)
TOTAL_CANVASES = 246  # 001.tif to 246.tif

# Known major sections (from Todd / RIA Catalogue) for quick jumps
CONTENTS = {
    "Outside front board": 1,
    "Inside front board": 2,
    "p. [i]": 3,
    "p. [ii]": 4,
    "p. 1 (Lebor Gabála starts)": 5,
    "p. 17 (core Book of Fermoy)": 21,
    "p. 38 (Betha Sain Seoirsí)": 42,
    "p. 49 (Tochmarc Treblainne)": 53,
    "p. 81–82 (Gearóid Iarla area)": 85,
    "p. 117 (example decorated page)": 121,
    "p. 181 (later tales)": 185,
    "p. 217 (medical fragments)": 221,
    "p. 238": 242,
    "Inside back board": 245,
    "Outside back board": 246,
}

def get_image_url(canvas_num: int, size: str = "full") -> str:
    """Build IIIF JPEG URL. canvas_num is 1-based (001.tif = 1)."""
    filename = f"{canvas_num:03d}.tif"
    # Use a reasonable max width for the app while still being high quality
    if size == "full":
        region = "full/max/0"
    else:
        region = "full/1200,/0"
    return f"{IIIF_BASE}{quote(filename)}/{region}/default.jpg"

def get_label(canvas_num: int) -> str:
    """Approximate human label."""
    if canvas_num == 1:
        return "Outside front board"
    if canvas_num == 2:
        return "Inside front board"
    if canvas_num == 3:
        return "p. [i]"
    if canvas_num == 4:
        return "p. [ii]"
    if 5 <= canvas_num <= 242:
        page = canvas_num - 4
        return f"p. {page}"
    if canvas_num == 243:
        return "p. [239]"
    if canvas_num == 244:
        return "p. [240]"
    if canvas_num == 245:
        return "Inside back board"
    if canvas_num == 246:
        return "Outside back board"
    return f"Canvas {canvas_num}"

# Sidebar
st.sidebar.title("📜 Book of Fermoy")
st.sidebar.caption("RIA MS 23 E 29 · Irish Script on Screen")

st.sidebar.markdown("### Quick jumps")
jump = st.sidebar.selectbox(
    "Go to section",
    options=list(CONTENTS.keys()),
    index=4,  # default to p. 1
)

if "page" not in st.session_state:
    st.session_state.page = CONTENTS[jump]

if st.sidebar.button("Jump"):
    st.session_state.page = CONTENTS[jump]

st.sidebar.markdown("---")
page = st.sidebar.slider(
    "Page / Canvas",
    min_value=1,
    max_value=TOTAL_CANVASES,
    value=st.session_state.page,
    step=1,
)
st.session_state.page = page

st.sidebar.markdown(f"**Current:** {get_label(page)}")
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
**How to use**
- Move the slider or use quick jumps
- Add Irish transcription and English translation below the image
- Notes stay in this browser session (copy them out to save permanently)
- Images load live from the official IIIF server
"""
)
st.sidebar.markdown(
    "[View on ISOS](https://www.isos.dias.ie/RIA/RIA_MS_23_E_29.html)"
)

# Main area
st.title("Book of Fermoy")
st.subheader(get_label(page))

col1, col2 = st.columns([2, 1])

with col1:
    img_url = get_image_url(page)
    st.image(img_url, caption=f"{get_label(page)} — RIA MS 23 E 29", use_container_width=True)
    st.caption(f"Image served from IIIF: `{img_url}`")

with col2:
    st.markdown("### Irish / Gaelic transcription")
    irish_key = f"irish_{page}"
    irish = st.text_area(
        "Transcription",
        value=st.session_state.get(irish_key, ""),
        height=220,
        key=irish_key,
        placeholder="Type or paste the Irish text here…"
    )

    st.markdown("### English translation")
    en_key = f"english_{page}"
    english = st.text_area(
        "Translation",
        value=st.session_state.get(en_key, ""),
        height=220,
        key=en_key,
        placeholder="Write the English translation here…"
    )

    st.markdown("### Notes")
    notes_key = f"notes_{page}"
    notes = st.text_area(
        "Notes",
        value=st.session_state.get(notes_key, ""),
        height=120,
        key=notes_key,
        placeholder="Scribe, damage, variants, references…"
    )

# Bottom bar with download of current page notes
st.markdown("---")
if st.button("📋 Copy current page data as text"):
    data = f"""# {get_label(page)}
## Irish
{irish}

## English
{english}

## Notes
{notes}
"""
    st.code(data, language=None)
    st.success("Text block generated above — select and copy it.")

st.markdown(
    """
---
**Book of Fermoy** (RIA MS 23 E 29) · Images © Royal Irish Academy / Irish Script on Screen  
This app is a personal working tool for transcription and translation.  
All manuscript images remain under the original rights holders.
"""
)
