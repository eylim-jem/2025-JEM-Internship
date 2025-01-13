import streamlit as st
# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Distribution in the Modern Grid",
    layout="centered"
)

# ---------------------------
# Main Title
# ---------------------------
st.title("Distribution in the Modern Grid")

st.markdown("""
    **Distribution networks** play a pivotal role in supporting the functionality and advancement of the modern electrical grid, ensuring that power is delivered efficiently, sustainably, and reliably to meet the evolving needs of society.
    """)

try:
    st.image(r"C:\Users\bpoort\OneDrive - onlineeportal\Desktop\Internship-2025-main\assets\smart_grid.png", caption="The Future of Electricity!", use_container_width=True)
except FileNotFoundError:
    st.warning("Please ensure the image is in the same directory as the app.")

# 1. Role of Distribution Networks in the Modern Grid
st.header("1. Role of Distribution Networks in the Modern Grid")

# a. Smart Grids & Automation
with st.expander("a. Smart Grids"):
        st.subheader("Smart Grids")
        st.markdown("""
        - **Definition**: Advanced electricity networks that use digital technology, sensors, and automation to monitor and manage the production, distribution, and use of electricity efficiently.
        """)

        st.subheader("Relevance in a Distribution Network")
        st.markdown("""
        - **Overview**: Smart grids enhance reliability and efficiency, enable real-time monitoring and management, facilitate the integration of renewable energy sources, improve demand response capabilities, and support better fault detection and maintenance within the distribution system."""
        )
        st.subheader("Examples")

        st.markdown("""
        - **Automated Fault Detection Systems:**
            - Quickly identify and isolate faults
            - Minimise outage durations
        - **Self-Healing Mechanisms:**
            - Automatically reroute power during disruptions
            - Maintain service continuity
        - **Adaptive Load Management:**
            - Dynamically adjust electricity usage
            - Balance demand and supply conditions""")
        
# b. Integration of Distributed Energy Resources (DERs)
with st.expander("b. Integration of Distributed Energy Resources (DERs)"):
        st.subheader("Overview of DERs")
        st.markdown("""
        - **Definition**: Small-scale units of local generation connected to the grid at the distribution level, such as solar panels, wind turbines, and energy storage systems.
        - In 2024, more than **65,000** of Jemena's customers (around 18 percent) have solar installed and this is expected to increase to over **100,000** customers by 2035.
        - DER units are classified according to their size:
                    
                    """)
        
        try:
            st.image(r"C:\Users\bpoort\OneDrive - onlineeportal\Desktop\Internship-2025-main\assets\DER.png", caption="DER Clasifications from AEMC (The Australian Energy Market Commission)", use_container_width=True)
        except FileNotFoundError:
            st.warning("Please ensure the image is in the same directory as the app.")

        st.subheader("Impact on Distribution Networks")
        st.markdown("""
        - **Challenges**: Managing bidirectional power flows, ensuring voltage stability, and maintaining grid reliability.
        - **Opportunities**: Increased resilience, reduced transmission losses, and enhanced support for renewable energy integration.
        """)

# c. Electrification and Its Effects on Distribution
with st.expander("c. Electrification and Its Effects on Distribution"):
        st.subheader("Electrification Trends")
        st.markdown("""
        - **Definition**: The shift towards using electricity for various applications previously reliant on fossil fuels, such as electric vehicles (EVs) and electric heating.
        """)

        st.subheader("Impact on Distribution Networks")
        st.markdown("""
        - **Increased Load Demand**: Necessitates infrastructure upgrades to handle higher electricity consumption.
        - **Smart Charging Infrastructure**: Implementation of intelligent EV charging stations to manage peak loads and distribute demand effectively.
        """)

# d. Demand Growth in Specific Sectors: Data Centers 
with st.expander("d. Demand Growth in Specific Sectors: Data Centers (DCs)"):
        st.subheader("Current Trends in Data Centers")
        st.markdown("""
        - The exponential growth of cloud computing and digital services has significantly increased the electricity demand of data centers.
        """)

        try:
            st.image(r"C:\Users\bpoort\OneDrive - onlineeportal\Desktop\Internship-2025-main\assets\dc.png", caption="Forecasted Growth of Data Centers", use_container_width=True)
        except FileNotFoundError:
            st.warning("dc.png not found. Please ensure the image is in the same directory as the app.")

        st.subheader("Impact on Distribution Networks")
        st.markdown("""
        - **High Power Demand**: Data centers require consistent and substantial power supply, necessitating robust distribution infrastructure.
        - **Power Quality Requirements**: Ensuring stable voltage and frequency to support sensitive IT equipment.
        - **Redundancy and Reliability**: Implementation of backup power systems and redundant distribution paths to prevent downtime.
        """)

# Quiz Section
st.subheader("Test Your Understanding")

st.markdown("""
    **Answer the following questions to check your understanding of the modern electrical grid.**
    """)

with st.form("quiz_form"):
        # Question 1: Multiple-Choice
        st.subheader("1. Which of the following is a key benefit of implementing automation in smart grids?")
        q1 = st.radio(
            "Select one:",
            (
                "Increases manual interventions during outages.",
                "Minimises outages and optimises electricity flow.",
                "Eliminates the need for any control systems.",
                "Decreases the efficiency of electricity services."
            ),
            key="q1"
        )

        # Question 2: Multiple-Select (Checkboxes)
        st.subheader("2. Which of the following are considered Distributed Energy Resources (DERs)? (Select all that apply)")
        q2_option1 = st.checkbox("Solar panels", key="q2_option1")
        q2_option2 = st.checkbox("Coal-fired power plants", key="q2_option2")
        q2_option3 = st.checkbox("Wind turbines", key="q2_option3")
        q2_option4 = st.checkbox("Energy storage systems", key="q2_option4")
        q2_option5 = st.checkbox("Diesel generators", key="q2_option5")

        # Question 3: Short Answer
        st.subheader("3. What term describes the increasing use of electricity across various sectors/replacing fossil fuels with electric alternatives?")
        q3 = st.text_input("Your answer:", key="q3")

        # Submit Button
        submitted = st.form_submit_button("Submit Answers")

if submitted:
        score = 0
        total = 3

        # Process Question 1
        if q1 == "Minimises outages and optimises electricity flow.":
            score += 1

        # Process Question 2
        correct_answers_q2 = {"Solar panels", "Wind turbines", "Energy storage systems"}
        user_answers_q2 = set()
        if q2_option1:
            user_answers_q2.add("Solar panels")
        if q2_option2:
            user_answers_q2.add("Coal-fired power plants")
        if q2_option3:
            user_answers_q2.add("Wind turbines")
        if q2_option4:
            user_answers_q2.add("Energy storage systems")
        if q2_option5:
            user_answers_q2.add("Diesel generators")

        if user_answers_q2 == correct_answers_q2:
            score += 1

        # Process Question 3
        q3_correct_answer = "Electrification"
        if q3.strip().lower() == q3_correct_answer.lower():
            score += 1

        # Display Score
        st.markdown("---")
        st.success(f"You scored {score} out of {total}.")

        # Overall Feedback
        if score == total:
            st.balloons()
    
st.header("2. Jemena's Initiatives")

# a. FLISR
with st.expander("a. FLISR"):
    st.subheader("**FLISR** (Fault Location, Isolation and Service Restoration)")
    st.markdown("""
    **Function:**
    - Utilises power flow analysis to pinpoint the exact location of an electrical fault.
    - Remote-control switches automatically open on either side of the fault to minimise the number of customers affected.
    
    **Benefits:**
    - **Improved Reliability:** Manual switching can take hours (as fieldworkers must physically travel to each fault location). Hence, by automatically isolating faults within seconds of their detection there is a considerable reducation in outage durations. 
    - **Cost Reduction:** Number of customers impacted and duration of outage is decreased; this lowers penalties associated with STPIS. 
    - **Customer Satisfaction:** Minimises the impact of outages, helping to build build public 
        trust and a strong relationship between Jemena and its customers.
    """)

# b. VVC
with st.expander("b. VVC"):
    st.subheader("**VVC** (Volt-Var Control) System")
    st.markdown("""
    **Function:**
    - Can dynamically and automatically adjust network voltages to maintain compliance with the required range. VVC can also push voltages down to reduce carbon emissions and energy consumption. 
    - Protects the power quality of the network.
    
    **Relevance:**
    - Trial successfully concluded in August 2024.
    - Addresses voltage fluctuations caused by the exponential growth of customers installing solar panels.
    
    **Benefits:**
    - **Enhanced Power Quality:** Maintains stable voltage levels despite increasing distributed generation.
    - **Increased Solar Adoption:** Facilitates the integration of more solar installations by mitigating potential voltage-related constraints.
    - **Grid Stability:** Supports the grid in handling higher levels of renewable energy sources efficiently.
    """)
# ---------------------------
# Conclusion / Thank You
# ---------------------------
st.write("---")
st.write("### Thank you for learning about Electricity Distribution Networks in the Modern Grid!")
st.write(
    """
    Feel free to explore more about how power is transmitted and distributed 
    to our homes, businesses, and industries. 
    """
)
