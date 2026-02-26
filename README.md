# 📟 Secure IoT Device Control Hub (Live Scraper)

A minimalist, responsive, and secure IoT management dashboard built with **Streamlit** and **Python 3.14**. This project simulates a full-stack IoT lifecycle: Data Ingestion (Scraping) → State Management (Mock-Django) → Reactive UI (Frontend).

## 🚀 Features
* **Secure Authentication:** Integrated login gate with session-state persistence.
* **Responsive Design:** Optimized for both Desktop (3-column grid) and Mobile (vertical stacking).
* **Live Telemetry:** Real-time temperature monitoring with millisecond-accurate "Last Sync" timestamps.
* **Remote Control:** Interactive toggles and value adjusters to modify device states.
* **Clean UI:** Minimalist card-based layout using custom CSS injection.

## 🛠️ Technical Concepts Used
* **Web Scraping Logic:** Simulated data ingestion via a modular plugin pattern.
* **State Management:** Utilizing `st.session_state` to mimic a persistent database.
* **Resilient Coding:** Implementation of `.get()` methods to prevent `KeyError` during session updates.
* **Context Managers:** Using Python's `with` statement for clean UI encapsulation.

🔐 Credentials
Username: admin
Password: iot123