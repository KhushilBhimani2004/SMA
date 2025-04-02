import streamlit as st

def main():
    st.set_page_config(page_title="Landing Page", page_icon="🚀", layout="centered")
    
    st.markdown("""
        <style>
            body {
                background-color: #e8f5e9;
            }
            .title {
                text-align: center;
                color: #2E7D32;
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                font-size: 20px;
                color: #1B5E20;
                margin-bottom: 30px;
            }
            .big-button {
                width: 100%;
                padding: 15px;
                font-size: 18px;
                border-radius: 10px;
                background: linear-gradient(135deg, #4CAF50, #2E7D32);
                color: white;
                border: none;
                cursor: pointer;
                text-align: center;
                display: block;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
                margin: 10px 0;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .big-button:hover {
                background: linear-gradient(135deg, #388E3C, #1B5E20);
                transform: scale(1.05);
            }
            .button-container {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='title'>Welcome to Our Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Select an option below:</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='button-container'><a href='https://climatesmaproj.streamlit.app/' target='_blank' class='big-button'>🔗 Climate Change</a></div>", unsafe_allow_html=True)
        st.markdown("<div class='button-container'><a href='https://wastesmaproj.streamlit.app/' target='_blank' class='big-button'>📊 Waste Management</a></div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='button-container'><a href='https://co2smaproj.streamlit.app/' target='_blank' class='big-button'>🤖 CO2 Emission</a></div>", unsafe_allow_html=True)
        st.markdown("<div class='button-container'><a href='https://aqismaproj.streamlit.app/' target='_blank' class='big-button'>🌍 AQI Pollution Data</a></div>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
