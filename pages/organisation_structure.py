import streamlit as st
from pathlib import Path

script_dir = Path(__file__).parent
project_root = script_dir.parent
image = project_root / "assets" / "org_structure.png"
image_path_str = image.as_posix()

st.markdown(
    """
    <style>
        div[role="radiogroup"] label:first-of-type {
            visibility: hidden;
            height: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and Introduction
st.title("Jemena's Organisation Structure")

st.write("---")

# Overview of SGSPAA
st.header("1. SGSPAA Overview")
st.markdown("""
- **Ownership:** SGSPAA is owned by **State Grid of China (60%)** and **Singapore Power (40%)** through their international subsidiaries.
    - **State Grid Corporation of China:**
        - World’s largest electricity supply company with **$545 billion annual revenue**.
        - Known for technological leadership in the energy sector.
    - **Singapore Power Group:**
        - Major energy utility in Asia Pacific, operating networks in Singapore and Australia.
- **Businesses:** SGSPAA operates two main businesses: 
  1. **Jemena:** Focused on managing and operating energy assets.
  2. **Zinfra:** Provides construction and operational services, including overhead work, underground work, and maintenance.
""")
st.image(image_path_str, caption="Company Strcture", use_container_width=True)
st.markdown("""
- **Highlights of SGSPAA:**
  - Provides energy services to over **1.7 million Australian customers**.
  - Over **100 years of experience** in the utilities sector.
  - Backed by global leaders in energy technology.
""")

st.header("Quiz")

with st.form("quiz_form"):
    st.subheader("Test Your Knowledge")
    
    # Question 1
    q1 = st.radio(
        "What percentage of SGSPAA is owned by Singapore Power?",
        options=["", "40%", "50%", "60%", "None of the above"],
        key="q1"
    )
    
    # Question 2
    q2 = st.radio(
        "Which company provides operational and construction services for SGSPAA?",
        options=["", "Jemena", "Zinfra", "State Grid Corporation", "Singapore Power"],
        key="q2"
    )
    
    # Question 3 (New Harder Question)
    q3 = st.radio(
        "What is the primary purpose of having a parent company structure for SGSPAA?",
        options=[
            "",
            "To provide financial backing and access to global resources",
            "To reduce operational costs of Jemena and Zinfra",
            "To increase the number of customers served directly by the parent company",
            "To eliminate the need for regulatory approvals in Australia"
        ],
        key="q3"
    )
    
    # Submit Button
    submit_button = st.form_submit_button("Submit Answers")
    
    if submit_button:
        st.write("### Results")
        correct_answers = {
            "q1": "40%",
            "q2": "Zinfra",
            "q3": "To provide financial backing and access to global resources"
        }
        
        score = 0
        if q1 == correct_answers["q1"]:
            score += 1
        if q2 == correct_answers["q2"]:
            score += 1
        if q3 == correct_answers["q3"]:
            score += 1
        
        st.write(f"You scored {score}/3.")
        if score == 3:
            st.success("Great job! You know SGSPAA well.")
        elif score == 2:
            st.info("Good effort! Review the information and try again.")
        else:
            st.warning("Keep learning! You can do better next time.")

## Include image

st.write("---")

# Jemena Section
st.header("2. Jemena")

st.markdown("""
Jemena focuses on electricity (distribution) and gas (distribution and transmission) networks.  
It manages **over $11 billion worth of energy assets** and is structured into the following five main branches:
""")

st.markdown("""
1. **Gas Markets**  
2. **Digital**  
3. **Finance**  
4. **Group Strategy**  
5. **Networks**  
""")

st.markdown("""
### Key Groups within the Network branch
""")

with st.expander("**a. Assets & Operations (Electricty):**"):
    st.markdown("""
        - **Network Assets:**
            - Distribution Team
            - Primary Assets Team
            - Secondary Assets Team
            - Metering Team
        - **Future Network & Planning:**
            - Network Planning Team
            - Network Reliability and Intelligence Team
            - Future Network Team
        - **Network Operations:**
            - Network Information and Outage Planning Team
            - Control and Dispatch Electricity Team
        - **Business Improvement and Innovation** 
        - **Network Investment & Delivery** """)
    
with st.expander("**b. Assets & Operations (Gas):**"):
    st.markdown("""
        - **Engineering and Network control:**
            - Pipeline Team
            - Asset Protection Team
            - Gas Distribution Team
        - **Network Operations:**
            - Renewable Gas Engineers
            - Risk and Assurance Specialists
        - **Planning and optimisation:** 
            - Metering Team
        	- Pipeline Team
        	- Distribution & Capacity Team
            - Facilities Team
        - **Investment and Portfolio**
     """)

st.write("---")
st.header("3. Obtaining your Org Chart")
st.subheader("Step 1")
image = project_root / "assets" / "step1.png"
image_path_str = image.as_posix()
st.image(image_path_str, caption="Jemena's Group intranet", use_container_width=True)

st.subheader("Step 2")
image = project_root / "assets" / "step2.png"
image_path_str = image.as_posix()

col1, col2, col3 = st.columns([2, 10, 2])

with col2:
    st.image(
        image_path_str, caption="Success Factors Homepage"
    )

st.subheader("Step 3")
st.markdown("Explore the interactive chart:")
image = project_root / "assets" / "step3.png"
image_path_str = image.as_posix()
st.image(image_path_str, caption="Example Organisation Chart", use_container_width=True)

# ---------------------------
# Conclusion
# ---------------------------
st.write("---")
st.write("### Thank you for learning about Jemena's organisation structure!")
st.write(
    """
    Feel free to explore more about how power is transmitted and distributed to our homes, businesses, and industries.
    """
)
