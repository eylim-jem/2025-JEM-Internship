import streamlit as st
from pathlib import Path

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Key Concepts of Distribution",
    layout="centered"
)

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

# ---------------------------
# File Paths
# ---------------------------
script_dir = Path(__file__).parent
project_root = script_dir.parent
image_dist_flowchart = project_root / "assets" / "distribution_flowchart.PNG"
image_dist_flowchart_str = image_dist_flowchart.as_posix()

# ---------------------------
# Main Title and Introduction
# ---------------------------
st.title("Key Concepts of Distribution")
st.write(
    """
    Understanding power distribution and its key concepts is essential for maintaining stable 
    and safe electrical systems. Electricity flows from power stations, where it is transformed 
    to high voltage for long-distance transmission. The current is then carried by transmission lines 
    to a substation where the voltage is lowered for distribution to homes and businesses. The retailer 
    then quantifies your usage before sending you the bill.
    """
)
st.image(image_dist_flowchart_str, caption="Distribution Flowchart", use_container_width=True)

# ---------------------------
# Distribution System Components
# ---------------------------
st.subheader("Main Components of the Distribution System")
st.write(
    """
    **Substations:**
    - Control the flow of electricity.
    - Use step-down transformers to reduce voltage for local distribution.
    - Contain switchgear and circuit breakers that protect the grid by isolating faults and preventing outages from spreading.
    
    **Distribution Lines:**
    - Carry low voltage electricity to homes and businesses.
    - May use medium or high voltage for industrial use.
    
    **Transformers:**
    - Step up or step down the voltage for safe transmission and distribution.
    
    **Feeders:**
    - Carry electricity from substations to distribution points (transformers or directly to consumers),
      effectively feeding electrical power to lower-voltage parts of the grid.
    """
)

with st.form("distribution_quiz_form"):
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

    # Question 1: Substations
    st.subheader("1. What is the primary function of substations?")
    q1 = st.radio(
        "Select one:",
        (
            " ",
            "To increase the voltage of electricity for long-distance transmission",
            "To control the flow of electricity and reduce voltage for local distribution",
            "To generate electricity for distribution",
            "To provide backup power during outages"
        ),
        key="q1"
    )

    # Question 2: Transformers
    st.subheader("2. What role do transformers play in the electrical grid?")
    q2 = st.radio(
        "Select one:",
        (
            " ",
            "They help to prevent electrical faults from spreading",
            "They store electrical energy for later use",
            "They step up or step down voltage for safe transmission and distribution",
            "They distribute electricity directly to consumers"
        ),
        key="q2"
    )

    # Question 3: Switchgear & Circuit Breakers
    st.subheader("3. What is the purpose of switchgear and circuit breakers in substations?")
    q3 = st.radio(
        "Select one:",
        (
            " ",
            "To increase the voltage of electricity",
            "To isolate faults and prevent outages from spreading",
            "To generate electricity",
            "To convert electricity into usable power for businesses"
        ),
        key="q3"
    )

    # Question 4: Feeders
    st.subheader("4. What is the primary function of feeders in the electrical grid?")
    q4 = st.radio(
        "Select one:",
        (
            " ",
            "To increase the voltage for long-distance transmission",
            "To carry electricity from substations to transformers or consumers",
            "To distribute electricity to businesses",
            "To store electrical energy for later use"
        ),
        key="q4"
    )

    # Question 5: Voltage in Distribution Lines
    st.subheader("5. What type of voltage do distribution lines generally carry for homes and businesses?")
    q5 = st.radio(
        "Select one:",
        (
            " ",
            "High voltage",
            "Low voltage",
            "Medium voltage",
            "Extra-high voltage"
        ),
        key="q5"
    )

    submitted = st.form_submit_button("Submit Answers")

# Feedback Section
if submitted:
    # Feedback for Question 1
    if q1 == "To control the flow of electricity and reduce voltage for local distribution":
        st.success("Q1: Correct! Substations help control the flow and reduce voltage for local distribution.")
    elif q1 == "To increase the voltage of electricity for long-distance transmission":
        st.error("Q1: Incorrect. Substations reduce voltage for local distribution rather than increasing it.")
    elif q1 == "To generate electricity for distribution":
        st.error("Q1: Incorrect. Substations manage the flow of electricity but do not generate it.")
    elif q1 == "To provide backup power during outages":
        st.error("Q1: Incorrect. Substations manage the grid; they do not provide backup power.")
    
    # Feedback for Question 2
    if q2 == "They step up or step down voltage for safe transmission and distribution":
        st.success("Q2: Correct! Transformers adjust voltage levels for safe transmission and distribution.")
    elif q2 == "They help to prevent electrical faults from spreading":
        st.error("Q2: Incorrect. Transformers change voltage levels, not prevent faults.")
    elif q2 == "They store electrical energy for later use":
        st.error("Q2: Incorrect. Transformers do not store energy.")
    elif q2 == "They distribute electricity directly to consumers":
        st.error("Q2: Incorrect. Transformers are not responsible for directly delivering electricity.")
    
    # Feedback for Question 3
    if q3 == "To isolate faults and prevent outages from spreading":
        st.success("Q3: Correct! Switchgear and circuit breakers isolate faults and prevent the spread of outages.")
    elif q3 == "To increase the voltage of electricity":
        st.error("Q3: Incorrect. They do not increase the voltage.")
    elif q3 == "To generate electricity":
        st.error("Q3: Incorrect. They manage and protect the grid but do not generate electricity.")
    elif q3 == "To convert electricity into usable power for businesses":
        st.error("Q3: Incorrect. Their primary role is grid protection.")
    
    # Feedback for Question 4
    if q4 == "To carry electricity from substations to transformers or consumers":
        st.success("Q4: Correct! Feeders transport electricity to lower-voltage parts of the grid.")
    elif q4 == "To increase the voltage for long-distance transmission":
        st.error("Q4: Incorrect. Feeders carry electricity for distribution, not for increasing voltage.")
    elif q4 == "To distribute electricity to businesses":
        st.error("Q4: Incorrect. Feeders are used throughout the grid and are not specific to businesses.")
    elif q4 == "To store electrical energy for later use":
        st.error("Q4: Incorrect. Feeders do not store energy.")
    
    # Feedback for Question 5
    if q5 == "Low voltage":
        st.success("Q5: Correct! Distribution lines for homes and businesses typically use low voltage.")
    elif q5 == "High voltage":
        st.error("Q5: Incorrect. High voltage is typically reserved for long-distance transmission.")
    elif q5 == "Medium voltage":
        st.error("Q5: Incorrect. Residential areas use low voltage distribution.")
    elif q5 == "Extra-high voltage":
        st.error("Q5: Incorrect. Extra-high voltage is not used for distribution to homes or businesses.")

# Redundancy Explanation
st.subheader("What is Redundancy?")
st.write(
    """
    Redundancy refers to incorporating backup systems, equipment, or infrastructure to ensure a continuous 
    and reliable electricity supply. In case one distribution network fails, there remain alternative paths to supply energy, 
    minimizing outages, maintaining grid stability, and ensuring that customers have a constant power supply.
    In the case of emergency or maintenance, following a "n-1" rule in network planning allows for planned or unexpected failures to have less impact on network stability.
    """
)

# Distribution Network Configurations
st.subheader("Types of Distribution Network Configurations")
st.write(
    """
    - **Radial:** Single direction; cost effective but vulnerable to outages.
    - **Looped:** Multiple paths connect and supply consumers. It creates redundancy—if one path fails, another can deliver power. Reliable but expensive.
    - **Mesh:** Complex and resilient with multiple interconnections between different parts of the system. Particularly reliable in densely populated areas.
    """
)

with st.form("distribution_configurations_quiz"):
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

    # Question 6: Radial Distribution Network
    st.subheader("6. Which of the following is a characteristic of a radial distribution network configuration?")
    q6 = st.radio(
        "Select one:",
        (
            "Select an option",  # Placeholder text to avoid default selection
            "Cost-effective but vulnerable to outages",
            "Creates redundancy and is highly reliable",
            "Expensive but has multiple paths",
            "Highly resilient with multiple interconnections"
        ),
        key="q6"
    )

    # Question 7: Mesh Distribution Network
    st.subheader("7. What is a mesh distribution network configuration?")
    q7 = st.radio(
        "Select one:",
        (
            "Select an option",  # Placeholder text to avoid default selection
            "Simple with single connection paths",
            "Resilient with multiple interconnections, reliable in densely populated areas",
            "Low-cost but prone to failures",
            "Relies on a single power path"
        ),
        key="q7"
    )

    # Question 8: Looped Distribution Network
    st.subheader("8. A looped distribution network creates redundancy and can deliver power if one path fails. (True/False)")
    q8 = st.radio(
        "Select one:",
        (
            "Select an option",  # Placeholder text to avoid default selection
            "True",
            "False"
        ),
        key="q8"
    )

    submitted = st.form_submit_button("Submit Answers")

if submitted:
    # Feedback for Question 6
    if q6 == "Cost-effective but vulnerable to outages":
        st.success("Q6: Correct! Radial networks are cost-effective but vulnerable to outages.")
    elif q6 == "Select an option":
        st.info("Q6: Please select an option.")
    else:
        st.error("Q6: Not quite. Radial networks are cost-effective but vulnerable to outages.")

    # Feedback for Question 7
    if q7 == "Resilient with multiple interconnections, reliable in densely populated areas":
        st.success("Q7: Correct! Mesh networks are complex and highly resilient, especially in densely populated areas.")
    elif q7 == "Select an option":
        st.info("Q7: Please select an option.")
    else:
        st.error("Q7: Not quite. Mesh networks are highly resilient due to their complex interconnections.")

    # Feedback for Question 8
    if q8 == "True":
        st.success("Q8: Correct! Looped networks have multiple paths, providing redundancy and reliability.")
    elif q8 == "Select an option":
        st.info("Q8: Please select an option.")
    else:
        st.error("Q8: Not quite. Looped networks are designed to be reliable and provide redundancy.")

# ---------------------------
# Metering Section
# ---------------------------
st.subheader("What is Metering?")
st.write(
    """
    Metering is the process of measuring and recording the consumption of electricity, gas, water, or other utilities 
    by customers or in industrial settings. There are three main types of meters predominantly used by Jemena:
    
    - **Smart Meters:** Electronic devices that record energy consumption in 30-minute intervals. They communicate 
      information to Jemena, which is then passed to the electricity retailer for billing. Jemena has installed smart 
      meters in more than 99% of homes and businesses.
    - **Digital Meters:** Primarily used to measure gas volumes.
    - **Current Transformer Meters:** Convert high current/voltage to lower values so the meter can accurately read the flow through cables. 
      These are used for electrical capacities above 76 amps per phase up to high voltage supplies.
    """
)

image_smart_meter = project_root / "assets" / "jemena-smart-meter.png"
image_smart_meter_str = image_smart_meter.as_posix()

col1, col2, col3 = st.columns([9, 8, 9])

with col2:
    st.image(
        image_smart_meter_str, caption="Jemena Smart Meter", use_container_width=True)

with st.form("metering_quiz"):
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

    # Question 9: Meter Type
    st.subheader("9. Which of these meters is used to convert high current/voltage to lower values for easy measurement?")
    q9 = st.radio(
        "Select one:",
        [
            "Select an option",
            "Smart meters",
            "Digital meters",
            "Current transformer meters",
            "Analog meters"
        ],
        key="q9"
    )

    # Question 11: Meters Used by Jemena (Checkboxes)
    st.subheader("10. Which of the following meters are used by Jemena? (Select all that apply)")
    q11_option1 = st.checkbox("Smart meters", key="q11_option1")
    q11_option2 = st.checkbox("Digital meters", key="q11_option2")
    q11_option3 = st.checkbox("Current transformer meters", key="q11_option3")
    q11_option4 = st.checkbox("Analog meters", key="q11_option4")
    
    submitted = st.form_submit_button("Submit Answers")

if submitted:
    # Feedback for Question 9
    if q9 == "Select an option":
        st.info("Q9: Please select an option.")
    elif q9 == "Current transformer meters":
        st.success("Q9: Correct! Current transformer meters step down high current/voltage for accurate readings.")
    else:
        st.error("Q9: Not quite. Current transformer meters are used for measuring high electrical capacities.")

    # Collect responses for Question 11
    selected_q11 = []
    if q11_option1:
        selected_q11.append("Smart meters")
    if q11_option2:
        selected_q11.append("Digital meters")
    if q11_option3:
        selected_q11.append("Current transformer meters")
    if q11_option4:
        selected_q11.append("Analog meters")
    
    # Feedback for Question 11
    if not selected_q11:
        st.info("Q10: Please select one or more options.")
    else:
        required_answers = {"Smart meters", "Digital meters", "Current transformer meters"}
        if required_answers.issubset(set(selected_q11)):
            st.success("Q10: Correct! Jemena uses smart, digital, and current transformer meters.")
        else:
            st.error("Q10: Not quite. The correct answers are Smart meters, Digital meters, and Current transformer meters.")

# ---------------------------
# Distribution: Primary vs. Secondary
# ---------------------------
col_primary, col_secondary = st.columns(2)

with col_primary:
    st.subheader("Primary Distribution")
    st.markdown(
        """
        - This stage involves transporting electricity from a substation to local distribution 
          transformers. It uses higher voltage lines to cover long distances efficiently.
        """
    )

with col_secondary:
    st.subheader("Secondary Distribution")
    st.markdown(
        """
        - This stage delivers electricity at lower voltages from local transformers directly 
          to homes and other end users.
        """
    )

with st.form("distribution_types_quiz"):
    st.markdown(
        """
        <style>
            div[role="radiogroup"] label:first-of-type,
            div[data-baseweb="select"] span {
                visibility: hidden;
                height: 0px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Question 12: Secondary Distribution
    st.subheader("11. What is the primary function of secondary distribution?")
    q12 = st.radio(
        "Select one:",
        [
            "Select an option",
            "Transporting electricity from substations to local transformers",
            "Delivering energy at lower voltages to end users",
            "Carrying high voltage across large distances",
            "Converting electricity for industrial use"
        ],
        key="q12"
    )

    # Question 13: Distribution System Comparison
    st.subheader("12. Which distribution system covers larger distances and conducts higher voltages?")
    q13 = st.selectbox(
        "Select one:",
        [
            "Select an option",
            "Primary distribution",
            "Secondary distribution"
        ],
        key="q13"
    )

    submitted = st.form_submit_button("Submit Answers")

if submitted:
    # Feedback for Question 12
    if q12 == "Select an option":
        st.info("Q12: Please select an option.")
    elif q12 == "Delivering energy at lower voltages to end users":
        st.success("Q12: Correct! Secondary distribution delivers energy at lower voltages to homes and businesses.")
    else:
        st.error("Q12: Not quite. Secondary distribution is responsible for delivering energy at lower voltages.")

    # Feedback for Question 13
    if q13 == "Select an option":
        st.info("Q13: Please select an option.")
    elif q13 == "Primary distribution":
        st.success("Q13: Correct! Primary distribution covers larger distances and conducts higher voltages.")
    else:
        st.error("Q13: Not quite. Secondary distribution operates at lower voltages and is closer to end users.")

# ---------------------------
# Conclusion
# ---------------------------
st.write("---")
st.write("### Thank you for learning about the key concepts of Electricty Distribution Networks!")
st.write(
    """
    Feel free to explore more about how power is transmitted and distributed to our homes, businesses, and industries.
    """
)
