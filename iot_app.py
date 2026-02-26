import streamlit as st
from datetime import datetime

# --- 1. CONFIG & RESPONSIVE STYLING ---
st.set_page_config(
    page_title="Secure IoT Hub", 
    layout="wide", # Essential for desktop visibility
    initial_sidebar_state="collapsed" # Better for mobile first-impression
)

# Professional Minimalist CSS for both platforms
st.markdown("""
    <style>
    /* Make metrics look like cards */
    [data-testid="stMetric"] {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #eeeeee;
    }
    /* Increase button height for mobile touch */
    .stButton>button {
        width: 100%;
        height: 3em;
        border-radius: 8px;
    }
    /* Label styling */
    .status-active { color: #2ecc71; font-weight: bold; }
    .status-inactive { color: #e74c3c; font-weight: bold; }
    .timestamp-text { color: #7f8c8d; font-size: 0.75rem; font-family: monospace; }
    
    /* Mobile optimization: Remove extra padding */
    @media (max-width: 640px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE (The 'Django' Logic) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "devices" not in st.session_state:
    st.session_state.devices = {
        "AC_01": {"name": "Living Room AC", "loc": "Zone 1", "temp": 24, "active": True, "sync": datetime.now().strftime("%H:%M:%S")},
        "AC_02": {"name": "Office AC", "loc": "Zone 2", "temp": 22, "active": False, "sync": datetime.now().strftime("%H:%M:%S")},
        "IoT_03": {"name": "Kitchen Hub", "loc": "Zone 3", "temp": 26, "active": True, "sync": datetime.now().strftime("%H:%M:%S")}
    }

# --- 3. AUTHENTICATION GATE ---
if not st.session_state.logged_in:
    st.title("🔐 IoT Secure Login")
    # On mobile, this will span full width; on desktop, it stays centered.
    login_col = st.columns([1, 2, 1])[1] if not st.get_option("browser.gatherUsageStats") else st.container()
    with st.container(border=True):
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Access Dashboard", use_container_width=True):
            if user == "admin" and password == "iot123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Credentials")
    st.stop() 

# --- 4. MAIN DASHBOARD ---
with st.sidebar:
    st.title("👤 Admin")
    if st.button("Logout", type="primary", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

st.title("📟 IoT Control Center")
st.caption(f"Last Global Refresh: {datetime.now().strftime('%H:%M:%S')}")

# --- 5. RESPONSIVE GRID ---
# On Desktop: 3 Columns. On Mobile: Streamlit automatically stacks these to 1 Column.
cols = st.columns(3)

for i, (device_id, info) in enumerate(st.session_state.devices.items()):
    # Select column based on index
    with cols[i % 3]:
        with st.container(border=True):
            # Header
            st.subheader(info['name'])
            st.caption(f"📍 {info['loc']}")
            
            # Status Logic
            s_class = "status-active" if info['active'] else "status-inactive"
            s_label = "● ACTIVE" if info['active'] else "○ INACTIVE"
            st.markdown(f"Status: <span class='{s_class}'>{s_label}</span>", unsafe_allow_html=True)
            
            # Value & Timestamp
            st.metric(label="Temperature", value=f"{info['temp']}°C")
            st.markdown(f"<p class='timestamp-text'>⏱ Sync: {info['sync']}</p>", unsafe_allow_html=True)
            
            # Controls
            # Nested columns for buttons (keeps them side-by-side even on mobile)
            c1, c2 = st.columns(2)
            if c1.button(f"↑", key=f"inc_{device_id}", help="Increase Temperature"):
                st.session_state.devices[device_id]['temp'] += 1
                st.session_state.devices[device_id]['sync'] = datetime.now().strftime("%H:%M:%S")
                st.rerun()

            if c2.button(f"↓", key=f"dec_{device_id}", help="Decrease Temperature"):
                st.session_state.devices[device_id]['temp'] -= 1
                st.session_state.devices[device_id]['sync'] = datetime.now().strftime("%H:%M:%S")
                st.rerun()
            
            st.toggle("Power Switch", value=info['active'], key=f"tog_{device_id}")
            # Update state on toggle
            st.session_state.devices[device_id]['active'] = st.session_state[f"tog_{device_id}"]