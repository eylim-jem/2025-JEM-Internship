import streamlit as st
from pathlib import Path

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Jemena's Business Model",
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
# File Paths (example images, you can customize as needed)
# ---------------------------
script_dir = Path(__file__).parent
project_root = script_dir.parent



people = project_root / "assets" / "people.jpg"
people_str = people.as_posix()


innovation = project_root / "assets" / "innovation.jpg"
innovation_str = innovation.as_posix()

powerplant = project_root / "assets" / "power_plant.jpg"
powerplant_str = powerplant.as_posix()


renewables = project_root / "assets" / "renewables.jpg"
renewables_str = renewables.as_posix()


# ---------------------------
# Main Title and Introduction
# ---------------------------
st.title("Jemena's Business Model")
st.write(
    """
    Jemena's business model revolves around providing energy solutions that are customer-centric, 
    transparent, and aligned with sustainability goals. This approach focuses on both social and financial aspects 
    to drive long-term value for customers, stakeholders, and the community.
    """
)


# Define the root project path
project_root = Path(__file__).parent

# ---------------------------
# Tab Navigation Setup (inside the page itself)
# ---------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Social Aspects", "Technology & Innovation", "Regulation and Compliance", "Sustainability Goals"])

# ---------------------------
# Social Aspects Tab
# ---------------------------


with tab1:
    container = st.container(border=True)
    
    with container:
        st.header("Social Aspects")

        # Customer-Centric Approach
        st.subheader("Customer-Centric Approach")
        st.write(
            """
            Jemena ensures its business model is customer-centric by focusing on understanding and meeting the evolving 
            needs of its customers. This includes delivering safe, reliable, and affordable energy, as well as fostering 
            enduring relationships through transparency and collaboration.
            """
        )
        
        st.image( people_str, caption="The Jemena Community", use_container_width=True)
    

        with st.form("social_quiz_form"):
            st.subheader("1. How does Jemena ensure its business model is centered around customer needs?")
            q1 = st.radio(
                "Select one:",
                [
                    "Select an option",  
                    "By focusing on energy efficiency and cost reduction",
                    "By delivering energy safely, reliably, and affordably",
                    "By maximizing profits without considering customer needs",
                    "By offering a wide range of energy products"
                ],
                key="q1"
            )

            st.subheader("2. What strategies does Jemena employ to build enduring relationships with customers?")
            q2 = st.radio(
                "Select one:",
                [
                    "Select an option",
                    "Investing in customer service and engagement",
                    "By cutting costs to provide cheaper prices",
                    "Focusing solely on technology innovation",
                    "Ignoring customer feedback"
                ],
                key="q2_social"  
            )

            st.subheader("3. How does Jemena support the energy transition to Net Zero?")
            q3 = st.radio(
                "Select one:",
                [
                    "Select an option",
                    "By focusing on fossil fuels and traditional energy sources",
                    "By supporting the adoption of clean and renewable energy technologies",
                    "By reducing energy consumption across all operations",
                    "By discontinuing energy production to reduce emissions"
                ],
                key="q3"
            )

            submitted = st.form_submit_button("Submit Answers")

        if submitted:
            if q1 == "By delivering energy safely, reliably, and affordably":
                st.success("Q1: Correct! Jemena focuses on ensuring that energy is delivered safely, reliably, and affordably.")
            else:
                st.error("Q1: Incorrect. Jemena's customer focus is primarily on delivering safe, reliable, and affordable energy.")

            if q2 == "Investing in customer service and engagement":
                st.success("Q2: Correct! Jemena builds relationships by investing in customer service and engagement.")
            else:
                st.error("Q2: Incorrect. The correct answer is investing in customer service and engagement.")

            if q3 == "By supporting the adoption of clean and renewable energy technologies":
                st.success("Q3: Correct! Jemena is supporting the energy transition to Net Zero by promoting clean and renewable energy.")
            else:
                st.error("Q3: Incorrect. Jemena is focusing on clean and renewable technologies to support the energy transition.")

# ---------------------------
# Technology & Innovation Tab
# ---------------------------
with tab2:
    container = st.container(border=True)
    with container:
        st.header("Technology & Innovation")

        st.subheader("Leveraging Technology")
        st.write(
            """
            Jemena invests heavily in innovative technologies to improve efficiency, reduce operational costs, 
            and provide cleaner energy solutions. This includes utilizing smart meters, grid management technologies, 
            and data analytics to optimize energy delivery.
            """
        )

        st.image( innovation_str, caption="Innovative technologies", use_container_width=True)

        with st.form("technology_innovation_quiz_form"):
            st.subheader("1. Which technology is Jemena implementing to improve energy management?")
            q1_radio = st.radio(
                "Select one:",
                [" ", "Wind Turbines", "Energy Storage Systems", "Smart Meters", "Electric Vehicles"],
                key="q1_radio"
            )

            st.subheader("2. Which of the following technologies is NOT currently used by Jemena?")
            q2_checkbox1 = st.checkbox("Smart Meters", key="q2_checkbox1")
            q2_checkbox2 = st.checkbox("Energy Storage Systems", key="q2_checkbox2")
            q2_checkbox3 = st.checkbox("Nuclear Energy", key="q2_checkbox3")

            st.subheader("3. What type of energy storage solutions is Jemena focusing on?")
            q3_dropdown = st.selectbox(
                "Select storage solution:",
                ["Battery Storage", "Pumped Hydro", "Compressed Air", "Flywheel Storage"],
                key="q3_dropdown"
            )

            submitted = st.form_submit_button("Submit Answers")

        if submitted:
            if q1_radio == "Smart Meters":
                st.success("Q1: Correct! Jemena is leveraging smart meters for better energy management.")
            else:
                st.error("Q1: Incorrect. Jemena is focusing on smart meters for improved energy management.")

            if q2_checkbox3:
                st.success("Q2: Correct! Jemena does not currently use nuclear energy.")
            else:
                st.error("Q2: Incorrect. Nuclear energy is not used by Jemena at the moment.")

            if q3_dropdown == "Battery Storage":
                st.success("Q3: Correct! Jemena is focusing on battery storage as part of its energy solutions.")
            else:
                st.error("Q3: Incorrect. Battery storage is a primary focus for Jemena.")

# ---------------------------
# Regulation and Compliance Tab
# ---------------------------
with tab3:
    container = st.container(border=True)
    with container:
        st.header("Regulation and Compliance")

        st.subheader("Regulatory Framework")
        st.write(
            """
            Jemena operates within a highly regulated environment to ensure that its operations are compliant with industry standards 
            and regulations. This helps maintain reliability, security, and consumer protection across its service areas.
            """
        )

        st.image( powerplant_str, caption="Jemena power plant", use_container_width=True)
    

        with st.form("regulation_quiz_form"):
            st.subheader("1. Which regulatory body oversees Jemena’s operations in Australia?")
            q1_radio = st.radio(
                "Select one:",
                [" ","Australian Energy Regulator (AER)", "Clean Energy Council", "Australian Energy Market Operator (AEMO)", "National Energy Market (NEM)"],
                key="q1_radio_unique"
            )

            st.subheader("2. What is the primary goal of Jemena’s regulatory compliance efforts?")
            q2_dropdown = st.selectbox(
                "Select one:",
                ["Ensuring safe and reliable energy delivery", "Maximizing profits", "Reducing operational costs", "Expanding energy markets"],
                key="q2_dropdown_unique"
            )

            st.subheader("3. Which of the following are Jemena’s primary compliance obligations?")
            q3_checkbox1 = st.checkbox("Environmental Sustainability", key="q3_checkbox1_unique")
            q3_checkbox2 = st.checkbox("Customer Safety and Satisfaction", key="q3_checkbox2_unique")
            q3_checkbox3 = st.checkbox("Technological Innovation", key="q3_checkbox3_unique")

            submitted = st.form_submit_button("Submit Answers")

        if submitted:
            if q1_radio == "Australian Energy Regulator (AER)":
                st.success("Q1: Correct! Jemena is regulated by the Australian Energy Regulator (AER).")
            else:
                st.error("Q1: Incorrect. The AER oversees Jemena’s operations in Australia.")

            if q2_dropdown == "Ensuring safe and reliable energy delivery":
                st.success("Q2: Correct! The primary goal of regulatory compliance is to ensure safe, reliable energy delivery.")
            else:
                st.error("Q2: Incorrect. The main goal of regulation is ensuring the safe and reliable delivery of energy.")

            if q3_checkbox1 and q3_checkbox2:
                st.success("Q3: Correct! Environmental sustainability and customer safety are key compliance obligations for Jemena.")
            else:
                st.error("Q3: Incorrect. Jemena's primary obligations include environmental sustainability and customer safety.")

# ---------------------------
# Sustainability Goals Tab
# ---------------------------
with tab4:
    container = st.container(border=True)
    with container:
        st.header("Sustainability Goals")

        st.subheader("Jemena’s Sustainability Vision")

        st.write(
            """
            Jemena is committed to reducing its environmental footprint and accelerating the adoption of renewable energy solutions through ambitious sustainability goals. 
            These include reducing carbon emissions, investing in renewable energy, and promoting energy efficiency in all operations. 
            Jemena's Net Zero goals and reducing overall carbon emissions in the energy sector.
            """
        )
        st.image( renewables_str, caption="Renewable energy farms", use_container_width=True)

        with st.form("sustainability_quiz_form"):
            st.subheader("1. How much does Jemena aim to reduce its carbon emissions by 2030?")
            q1_slider = st.slider(
                "Carbon Emission Reduction Goal (%)",
                min_value=0, max_value=100, value=50, step=5,
                key="q1_slider"
            )

            st.subheader("2. Which sustainability goal is most aligned with Jemena’s future vision?")
            q2_radio = st.radio(
                "Select one:",
                [" ", "Achieving Net Zero by 2050", "Reducing energy prices for consumers", "Expanding fossil fuel usage", "Investing in non-renewable technologies"],
                key="q2_radio"
            )

            st.subheader("3. Which renewable energy source is Jemena most focused on?")
            q3_dropdown = st.selectbox(
                "Select renewable energy source:",
                ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
                key="q3_renewable"
            )

            submitted = st.form_submit_button("Submit Answers")

        if submitted:
            if q1_slider == 50:
                st.success("Q1: Correct! Jemena aims to reduce carbon emissions by 50% by 2030.")
            else:
                st.error(f"Q1: Incorrect. Jemena's target is to reduce emissions by 50% by 2030, but you selected {q1_slider}%.")
            
            if q2_radio == "Achieving Net Zero by 2050":
                st.success("Q2: Correct! Jemena is focused on achieving Net Zero emissions by 2050.")
            else:
                st.error("Q2: Incorrect. Achieving Net Zero by 2050 is Jemena's sustainability goal.")
            
            if q3_dropdown == "Solar":
                st.success("Q3: Correct! Jemena has a strong focus on solar energy projects.")
            else:
                st.error("Q3: Incorrect. Jemena has a primary focus on solar energy solutions.")


# ---------------------------
# Conclusion Section
# ---------------------------
st.write("---")
st.write("### Thank you for exploring Jemena's business model!")
st.write(
    """
    Jemena’s approach ensures that they meet the needs of customers while also investing in sustainable 
    practices for the future. Feel free to explore more about their customer-centric approach, 
    innovative energy solutions, and financial strategies.
    """
)

