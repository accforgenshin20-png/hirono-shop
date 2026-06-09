import os
import pandas as pd
import streamlit as st
import urllib.parse

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="HIRONO GALLERY",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CONFIG
# ==========================================
FILE_DATA = "data_hirono1.csv"

# Nomor WhatsApp Customer Service
ADMIN_WA = "6285961576154"

# ==========================================
# FORMAT RUPIAH
# ==========================================
def rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

# ==========================================
# CYBERPUNK CSS — HIRONO STYLE
# ==========================================
st.markdown("""
<style>

/* IMPORT FONT */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800&family=Rajdhani:wght@400;600;700&display=swap');

/* BACKGROUND */
.stApp{
    background:
    radial-gradient(circle at top left, #3A3A3A22 0%, transparent 30%),
    radial-gradient(circle at bottom right, #8A8A8A11 0%, transparent 30%),
    linear-gradient(
        135deg,
        #0A0A0A 0%,
        #111111 30%,
        #1B1B1B 70%,
        #262626 100%
    );

    color:white;
}

/* SCROLLBAR */
::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-track{
    background:#111;
}

::-webkit-scrollbar-thumb{
    background:#666;
    border-radius:10px;
}

/* HEADER */
.hirono-header{
    font-family:'Orbitron', sans-serif;
    font-size:5rem;
    font-weight:800;
    letter-spacing:14px;
    text-align:center;
    color:#F5F5F5;
    margin-top:25px;
    margin-bottom:0px;
    text-shadow:
        0px 0px 10px rgba(255,255,255,0.08),
        0px 0px 25px rgba(180,180,180,0.08);
    position:relative;
}

/* LINE */
.hirono-header::after{
    content:"";
    position:absolute;
    left:50%;
    transform:translateX(-50%);
    bottom:-12px;
    width:180px;
    height:2px;
    background:
    linear-gradient(
        90deg,
        transparent,
        #BDBDBD,
        transparent
    );
}

/* SUBTITLE */
.hirono-sub{
    text-align:center;
    font-family:'Rajdhani', sans-serif;
    color:#AFAFAF;
    letter-spacing:6px;
    font-size:1rem;
    margin-top:18px;
    margin-bottom:10px;
    text-transform:uppercase;
}

/* CONTACT */
.contact-text{
    text-align:center;
    color:#BDBDBD;
    font-family:'Rajdhani', sans-serif;
    letter-spacing:2px;
    margin-bottom:35px;
    font-size:0.95rem;
}

/* SEARCH BAR */
input{
    background: rgba(20,20,20,0.95) !important;
    border: 1px solid #555 !important;
    color:white !important;
    border-radius:18px !important;
    padding:14px !important;
    font-family:'Rajdhani', sans-serif !important;
    transition:0.3s ease !important;
}

input:focus{
    border: 1px solid #AFAFAF !important;
    box-shadow: 0px 0px 15px rgba(255,255,255,0.08) !important;
}

/* PRODUCT CARD */
.product-card{
    background:
    linear-gradient(
        180deg,
        rgba(35,35,35,0.98),
        rgba(18,18,18,0.98)
    );
    border: 1px solid #3A3A3A;
    border-radius:24px;
    padding:22px;
    margin-bottom: 15px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    box-shadow: 0px 12px 35px rgba(0,0,0,0.6);
    backdrop-filter:blur(10px);
    transition:0.35s ease;
}

/* HOVER */
.product-card:hover{
    transform: translateY(-5px) scale(1.01);
    border: 1px solid #8F8F8F;
    box-shadow: 0px 18px 45px rgba(255,255,255,0.08);
}

/* BADGE */
.badge{
    background:
    linear-gradient(
        135deg,
        #4A4A4A,
        #2A2A2A
    );
    border: 1px solid #6A6A6A;
    color:#F2F2F2;
    padding:6px 13px;
    border-radius:14px;
    font-size:0.72rem;
    font-family:'Rajdhani', sans-serif;
    letter-spacing:1px;
    font-weight:700;
}

/* BUTTON */
.stButton > button{
    width:100%;
    border-radius:18px !important;
    background:
    linear-gradient(
        135deg,
        #F2F2F2,
        #BDBDBD
    ) !important;
    color:#111 !important;
    border:none !important;
    padding:13px !important;
    font-family:'Orbitron', sans-serif !important;
    font-size:0.85rem !important;
    letter-spacing:2px !important;
    font-weight:700 !important;
    transition:0.3s ease !important;
    box-shadow: 0px 5px 20px rgba(255,255,255,0.06) !important;
}

/* BUTTON HOVER */
.stButton > button:hover{
    transform:translateY(-2px);
    background:
    linear-gradient(
        135deg,
        #8A8A8A,
        #DADADA
    ) !important;
    color:black !important;
    box-shadow: 0px 8px 25px rgba(255,255,255,0.12) !important;
}

/* DISABLED */
.stButton > button:disabled{
    background:#252525 !important;
    color:#666 !important;
    box-shadow:none !important;
}

/* DIALOG */
[data-testid="stDialog"]{
    background:
    linear-gradient(
        180deg,
        #1A1A1A,
        #101010
    ) !important;
    border: 1px solid #555 !important;
    border-radius:24px !important;
}

/* DIVIDER */
hr{
    border-color:#333 !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================
st.markdown(
    '<div class="hirono-header">HIRONO</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hirono-sub">Art Toys • Designer Collection • Limited Figures</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="contact-text">
CUSTOMER SERVICE<br>
+62 859-6157-6154
</div>
""", unsafe_allow_html=True)

# ==========================================
# SEARCH BAR
# ==========================================
col1, col2, col3 = st.columns([1,2,1])

with col2:
    search_query = st.text_input(
        "",
        placeholder="Search Hirono Collection..."
    )

st.divider()

# ==========================================
# LOAD CSV
# ==========================================
try:
    if not os.path.exists(FILE_DATA):
        st.error("CSV data tidak ditemukan.")
        st.stop()

    with st.spinner("Loading Hirono Collection..."):
        df = pd.read_csv(FILE_DATA)

    # VALIDASI CSV
    required_cols = ["nama", "kategori", "harga", "stok", "foto", "status"]
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        st.error(f"Kolom CSV kurang: {missing_cols}")
        st.stop()

    # SEARCH FILTER
    if search_query:
        df = df[df["nama"].str.contains(search_query, case=False, na=False)]

    # ==========================================
    # POPUP ORDER
    # ==========================================
    @st.dialog("🖤 HIRONO CHECKOUT")
    def order_popup(item):
        st.subheader(item["nama"])

        if os.path.exists(str(item["foto"])):
            st.image(item["foto"], use_container_width=True)
        else:
            st.warning("Gambar produk tidak ditemukan.")

        st.markdown(f"## {rupiah(item['harga'])}")

        nama = st.text_input("Collector Name")
        alamat = st.text_area("Shipping Address")
        qty = st.number_input(
            "Quantity",
            min_value=1,
            max_value=max(1, int(item["stok"])),
            value=1
        )

        total = qty * int(item["harga"])
        st.markdown(f"### Total : {rupiah(total)}")

        if st.button("CONFIRM ORDER"):
            if not nama or not alamat:
                st.error("Lengkapi nama dan alamat.")
            else:
                pesan = f'''🖤 HIRONO GALLERY ORDER

ITEM : {item["nama"]}
CATEGORY : {item["kategori"]}
QTY : {qty}

TOTAL : {rupiah(total)}

CUSTOMER : {nama}

ADDRESS :
{alamat}'''

                encoded = urllib.parse.quote(pesan)
                link = f"https://wa.me/{ADMIN_WA}?text={encoded}"
                st.success("Order berhasil dibuat.")
                st.link_button("Checkout via WhatsApp", link, use_container_width=True)

    # ==========================================
    # DISPLAY PRODUCTS
    # ==========================================
    cols = st.columns(3)

    for idx, row in df.iterrows():
        with cols[idx % 3]:
            # IMAGE
            if os.path.exists(str(row["foto"])):
                st.image(row["foto"], use_container_width=True)
            else:
                st.warning(f"Gambar '{row['foto']}' tidak ditemukan")

            # STATUS & BUTTON LOGIC
            status = str(row["status"]).strip()
            if status.lower() == "tersedia":
                tombol = "BUY NOW"
                disabled = False
            elif status.lower() in ["terbatas", "stok terbatas"]:
                tombol = "LIMITED STOCK"
                disabled = False
            else:
                tombol = "SOLD OUT"
                disabled = True

            # CARD & BUTTON CONTAINER
            with st.container():
                st.markdown(f"""
                <div class="product-card">
                    <div>
                        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
                            <span class="badge">{row['kategori']}</span>
                            <span class="badge">{status}</span>
                        </div>
                        <h3 style="color:white; font-family:'Orbitron', sans-serif; letter-spacing:1px; margin-bottom:5px;">
                            {row['nama']}
                        </h3>
                        <h2 style="color:#D9D9D9; font-family:'Rajdhani', sans-serif; margin-top:0px;">
                            {rupiah(row['harga'])}
                        </h2>
                    </div>
                    <div style="color:#9E9E9E; font-size:0.9rem; font-family:'Rajdhani', sans-serif;">
                        Remaining Stock : <b>{row['stok']}</b>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button(tombol, key=f"btn_{idx}", disabled=disabled, use_container_width=True):
                    order_popup(row)

    # EMPTY SEARCH
    if df.empty:
        st.warning("Produk Hirono yang kamu cari tidak ditemukan.")

except Exception as e:
    st.error(f"Error : {e}")

# ==========================================
# FOOTER
# ==========================================
st.divider()

st.markdown("""
<p style="text-align:center; color:#7A7A7A; font-size:0.8rem; letter-spacing:2px; font-family:'Rajdhani', sans-serif;">
HIRONO GALLERY ©️ 2026
</p>
""", unsafe_allow_html=True)