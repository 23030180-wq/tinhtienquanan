import streamlit as st
import pandas as pd

# ==========================
# CẤU HÌNH
# ==========================

st.set_page_config(
    page_title="🍽️ Order Nhà Hàng",
    page_icon="🍽️",
    layout="wide"
)

st.markdown(
"""
# 🍽️ HỆ THỐNG ORDER NHÀ HÀNG
---
"""
)

# ==========================
# MENU
# ==========================

menu = {

    "Đồ ăn":{

        "Pizza Hải Sản":150000,
        "Pizza Bò":160000,
        "Bò Lúc Lắc":180000,
        "Bít Tết":220000,
        "Cơm Chiên Hải Sản":90000,
        "Mì Ý Bò Bằm":95000,
        "Cánh Gà Chiên":85000,
        "Gà Nướng":180000,
        "Lẩu Thái":350000,
        "Lẩu Kim Chi":360000

    },

    "Thức uống":{

        "Coca":20000,
        "Pepsi":20000,
        "7Up":20000,
        "Trà Đào":35000,
        "Cafe Sữa":30000,
        "Cafe Đen":25000,
        "Nước Suối":10000,
        "Nước Cam":40000,
        "Sinh Tố":50000,
        "Bia Heineken":30000

    }

}

# ==========================
# SESSION
# ==========================

if "tables" not in st.session_state:

    st.session
