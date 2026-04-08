import streamlit as st
import math
import random


st.set_page_config(page_title="Pi-Thon Kitchen", page_icon="🎸")

st.title("🎸 WELCOME TO THE PI-THON KITCHEN")
st.subheader("Location: Flavourtown, Earth Surface")


with st.sidebar:
    st.header("Griddle Settings")
    n_fries = st.number_input("How many fries are we dropping?", min_value=1000, max_value=1000000, value=10000, step=1000)
    fry_len = 1.0
    grill_gap = 2.0


if st.button("🔥 FRY THE NEEDLES"):
    crossings = 0
   
    progress_bar = st.progress(0)
    
    for i in range(n_fries):
        dist_to_grill = random.uniform(0, grill_gap/2)
        angle = random.uniform(0, math.pi)
        if dist_to_grill <= (fry_len/2) * math.sin(angle):
            crossings += 1
        
        if i % (n_fries // 10) == 0:
            progress_bar.progress(i / n_fries)
    
    progress_bar.progress(1.0)

    if crossings == 0:
        st.error("Zero hits? That's a culinary disaster. Crank up the heat!")
    else:
        pi_est = n_fries / crossings
        
        col1, col2 = st.columns(2)
        col1.metric("Estimated π", f"{pi_est:.6f}")
        col2.metric("Flavor Error", f"{abs(math.pi - pi_est):.6f}")
        
        st.success(f"Final Count: {crossings} fries crossed the line!")
        st.balloons() 
