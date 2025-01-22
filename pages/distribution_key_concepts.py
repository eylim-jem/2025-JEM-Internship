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

# ---------------------------
# Distribution System Components
# ---------------------------
st.subheader("Main Components of the Distribution System")

st.write(
    """
    Understanding power distribution and its key concepts is essential for maintaining stable 
    and safe electrical systems.
    """
)


feeders = project_root / "assets" / "feeders.webp"
feeders_str = feeders.as_posix()


substation = project_root / "assets" / "substation.jpg"
substation_str = substation.as_posix()

transformer = project_root / "assets" / "transformer.jpg"
transformer_str = transformer.as_posix()


protection_relay = project_root / "assets" / "protection_relay.jpeg"
protection_relay_str = protection_relay.as_posix()

power_lines = project_root / "assets" / "power_lines.webp"
power_lines_str = power_lines.as_posix()

# Tab Navigation Setup
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Substations", "Transformers", "Protection", "Feeders", "Distribution Lines"])

# ---------------------------
# Substations Tab
# ---------------------------
with tab1:
    st.header("Substations")
    container = st.container(border=True)


    st.write(
        """
        - A zone substation is an important site of electrical power transformation and transfer. Zone substations receive high-voltage electricity from larger sub-transmission networks and step it down in to a lower voltage that is suitable for distribution to consumers. In the Jemena network, zone substations often step down voltages, working with 66kV, 22kV, 11kV and 6.6kV voltages, via transformers.  

        - This reduced voltage travels along feeder lines to distribution substations, which are then able to lower the voltage to the standard 400 or 230 volts used in homes and household appliances. 

        - As of June 2024, JEN owns 27 substations around the north-west of Metropolitan Melbourne with a combined capacity of 1,863 MVA of power. Additionally, JEN substations connect to 54 subtransmission lines running at 66 kV and 22 kV, and 232 feeder lines outputting voltages of 22kV, 11kV and 6.6kV. 
        
        """
    )

    st.image( substation_str, caption="substation", use_container_width=True)

    with st.form("substations_form"):
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
        
        # Submit button for the form
        submitted_substations = st.form_submit_button("Submit Substations Answer")

# ---------------------------
# Transformers Tab
# ---------------------------
with tab2:
    st.header("Transformers")
    container = st.container(border=True)
    st.write(
        """
       - Transformers at electrical substations play a crucial role in adjusting the voltage of electricity as it is transmitted from power plants to homes and businesses. Their primary function is to either step up or step down the voltage to make it suitable for long-distance transmission or local distribution. 

        - Step-up transformers increase the voltage for efficient long-distance transmission over high-voltage power lines, which reduces energy loss during transport. 

       -  Step-down transformers reduce the voltage to a safer, usable level for consumers once the electricity reaches local distribution networks. 

 
        """
    )
    
    st.image( transformer_str, caption="Transformer", use_container_width=True)

    with st.form("transformers_form"):
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
        
        # Submit button for the form
        submitted_transformers = st.form_submit_button("Submit Transformers Answer")

# ---------------------------
# Protection tab
# ---------------------------
with tab3:
    st.header("Protection")
    container = st.container(border=True)
    st.write(
        """
        - Protection and control equipment within a zone substation is used to detect the presence of a network fault and/or other 
        abnormal operating conditions and then to automatically initiate action to either isolate the network fault or correct the 
        abnormal condition by some pre-defined control sequence. 
        """)

    st.image( protection_relay_str, caption="Protection relay", use_container_width=True)

    with st.form("switchgear_form"):
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
        
        # Submit button for the form
        submitted_switchgear = st.form_submit_button("Submit Switchgear Answer")

# ---------------------------
# Feeders Tab
# ---------------------------
with tab4:
    st.header("Feeders")
    container = st.container(border=True)
    st.write(
        """
        - Carry electricity from substations to distribution points (transformers or directly to consumers),
            effectively feeding electrical power to lower-voltage parts of the grid.
        """)
    
    st.image( feeders_str, caption="Feeders", use_container_width=True)

    with st.form("feeders_form"):
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
        
        # Submit button for the form
        submitted_feed = st.form_submit_button("Submit Feeders Answer")

# ---------------------------
# Distribution Lines Tab
# ---------------------------
with tab5:
    st.header("Distribution Lines")
    st.write(
        """
        - Carry low voltage electricity to homes and businesses.
        - May use medium or high voltage for industrial use.
        - The network comprises over 700 kilometres of electricity distribution lines and cables, delivering approximately 4,321 GWh of energy to over 384,000 homes and businesses for several energy retailers
        - Poles are utilised to support the overhead electricity network and for public lighting where an underground electricity network is installed. These assets are located across the entire network and are manufactured from various materials, including wood, concrete and steel constructions.
        - Distribution equipment consists of HV and LV assets that are utilised in the distribution of electricity. This category consists of distribution transformers and their switches including HV switches, HV isolators, LV switchgear, LV isolators  and kiosks.
         """
    )

    st.image( power_lines_str, caption="power lines", use_container_width=True)


    with st.form("distribution_form"):
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
        
        # Submit button for the form
        submitted_distribution = st.form_submit_button("Submit Distribution Answer")

# ---------------------------
# Feedback Section
# ---------------------------
if submitted_substations:
    # Feedback for Question 1 (Substations)
    if q1 == "To control the flow of electricity and reduce voltage for local distribution":
        st.success("Q1: Correct! Substations help control the flow and reduce voltage for local distribution.")
    elif q1 == "To increase the voltage of electricity for long-distance transmission":
        st.error("Q1: Incorrect. Substations reduce voltage for local distribution rather than increasing it.")
    elif q1 == "To generate electricity for distribution":
        st.error("Q1: Incorrect. Substations manage the flow of electricity but do not generate it.")
    elif q1 == "To provide backup power during outages":
        st.error("Q1: Incorrect. Substations manage the grid; they do not provide backup power.")

if submitted_transformers:
    # Feedback for Question 2 (Transformers)
    if q2 == "They step up or step down voltage for safe transmission and distribution":
        st.success("Q2: Correct! Transformers adjust voltage levels for safe transmission and distribution.")
    elif q2 == "They help to prevent electrical faults from spreading":
        st.error("Q2: Incorrect. Transformers change voltage levels, not prevent faults.")
    elif q2 == "They store electrical energy for later use":
        st.error("Q2: Incorrect. Transformers do not store energy.")
    elif q2 == "They distribute electricity directly to consumers":
        st.error("Q2: Incorrect. Transformers are not responsible for directly delivering electricity.")

if submitted_switchgear:
    # Feedback for Question 3 (Switchgear & Circuit Breakers)
    if q3 == "To isolate faults and prevent outages from spreading":
        st.success("Q3: Correct! Switchgear and circuit breakers isolate faults and prevent the spread of outages.")
    elif q3 == "To increase the voltage of electricity":
        st.error("Q3: Incorrect. They do not increase the voltage.")
    elif q3 == "To generate electricity":
        st.error("Q3: Incorrect. They manage and protect the grid but do not generate electricity.")
    elif q3 == "To convert electricity into usable power for businesses":
        st.error("Q3: Incorrect. Their primary role is grid protection.")

if submitted_feed:
    # Feedback for Question 4 (Feeders)
    if q4 == "To carry electricity from substations to transformers or consumers":
        st.success("Q4: Correct! Feeders transport electricity to lower-voltage parts of the grid.")
    elif q4 == "To increase the voltage for long-distance transmission":
        st.error("Q4: Incorrect. Feeders carry electricity for distribution, not for increasing voltage.")
    elif q4 == "To distribute electricity to businesses":
        st.error("Q4: Incorrect. Feeders are used throughout the grid and are not specific to businesses.")
    elif q4 == "To store electrical energy for later use":
        st.error("Q4: Incorrect. Feeders do not store energy.")

if submitted_distribution:
    # Feedback for Question 5 (Distribution Lines)
    if q5 == "Low voltage":
        st.success("Q5: Correct! Distribution lines for homes and businesses typically use low voltage.")
    elif q5 == "High voltage":
        st.error("Q5: Incorrect. High voltage is typically reserved for long-distance transmission.")
    elif q5 == "Medium voltage":
        st.error("Q5: Incorrect. Residential areas use low voltage distribution.")
    elif q5 == "Extra-high voltage":
        st.error("Q5: Incorrect. Extra-high voltage is not used for distribution to homes or businesses.")


network_summary = project_root / "assets" / "network summary.PNG"
network_summary_str = network_summary.as_posix()

st.image(network_summary_str, caption="Network summary", use_container_width=True)


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

with st.expander("What is n-1?"):
    st.write('''
            A n-1 redundancy system in the context of the electricity network is one in which there is a backup route of electricity delivery should one component in a network line fail.
            Without it, a single component failure could result in widespread outages. 
             ''')

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
# Distribution: Primary vs. Secondary
# ---------------------------
col_primary, col_secondary = st.columns(2)



with col_primary:
    st.subheader("Primary Distribution")
    st.markdown(
        """
        - This stage involves transporting electricity from a substation to local distribution 
          transformers. It uses higher voltage lines to cover long distances efficiently.
        - Primary equipment: 1) Standalone Voltage Transformers (VT) and Current Transformers (CT) 
        """
    )

with col_secondary:
    st.subheader("Secondary Distribution")
    st.markdown(
        """
        - This stage delivers electricity at lower voltages from local transformers directly 
          to homes and other end users.
        - This includes lower value, faster turnover items that are required in larger quantities such as distribution lines and relays. Coils are also a part of secondary.
        - Secondary equipment: protection relays, coils
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

    # Question 9: Secondary Distribution
    st.subheader("9. What is the primary function of secondary distribution?")
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

    # Question 10: Distribution System Comparison
    st.subheader("10. Which distribution system covers larger distances and conducts higher voltages?")
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
    st.subheader("11. Which of these meters is used to convert high current/voltage to lower values for easy measurement?")
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
    st.subheader("12. Which of the following meters are used by Jemena? (Select all that apply)")
    q11_option1 = st.checkbox("Smart meters", key="q11_option1")
    q11_option2 = st.checkbox("Digital meters", key="q11_option2")
    q11_option3 = st.checkbox("Current transformer meters", key="q11_option3")
    q11_option4 = st.checkbox("Analog meters", key="q11_option4")
    
    submitted = st.form_submit_button("Submit Answers")

if submitted:
    # Feedback for Question 9
    if q9 == "Select an option":
        st.info("Q11: Please select an option.")
    elif q9 == "Current transformer meters":
        st.success("Q11: Correct! Current transformer meters step down high current/voltage for accurate readings.")
    else:
        st.error("Q11: Not quite. Current transformer meters are used for measuring high electrical capacities.")

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
        st.info("Q12: Please select one or more options.")
    else:
        required_answers = {"Smart meters", "Digital meters", "Current transformer meters"}
        if required_answers.issubset(set(selected_q11)):
            st.success("Q12: Correct! Jemena uses smart, digital, and current transformer meters.")
        else:
            st.error("Q12: Not quite. The correct answers are Smart meters, Digital meters, and Current transformer meters.")



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

