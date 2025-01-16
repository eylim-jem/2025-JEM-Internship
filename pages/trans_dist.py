import streamlit as st
from pathlib import Path

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Electricity Distribution Network",
    layout="centered"
)

col1, col2, col3 = st.columns([9, 11, 11])
script_dir = Path(__file__).parent
project_root = script_dir.parent 
image_path = project_root / "assets" / "Jemena_BrandMark_RGB_000.png"
image_path_str = image_path.as_posix() # Convert the path to a POSIX-style string (with forward slashes)

# ---------------------------
# Jemena Image 
# ---------------------------

with col2:
    st.image(
        image_path_str
    )

# ---------------------------
# Main Title
# ---------------------------
st.title("What is an Electricity Distribution Network?")

st.write(
    """
    **Distribution** is the third stage of the electricity network, coming after the [Generation](https://www.aemc.gov.au/energy-system/electricity/changing-generation-mix/victoria) and [Transmission](https://www.ausnetservices.com.au/electricity/transmission-network) stages.
    An **electricity distribution network** is the portion of the power delivery system 
    that carries electricity from higher-voltage transmission lines to homes, businesses, 
    and other end users at a lower voltage level.
    """
)

# ---------------------------
# Transmission vs. Distribution Section
# ---------------------------
st.header("1. Transmission vs. Distribution")

# Two columns to compare Transmission and Distribution side-by-side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Transmission")
    st.markdown("""
    - Transfers **high-voltage** electricity (typically tens or hundreds of kilovolts) over long distances.
    - Connects power plants (generation sources) to substations in populated or industrial areas.
    - Infrastructure: High-voltage transmission lines (often on tall towers), designed to move large quantities of electricity efficiently over distances.
    """)

with col2:
    st.subheader("Distribution")
    st.markdown("""
    - Steps down the high transmission voltage to lower voltages suitable for end users.
    - Delivers electricity from local substations directly to residential, commercial, and industrial customers.
    - Infrastructure: Usually consists of medium-voltage (e.g., 4 kV to 35 kV) and low-voltage lines (230V to Jemena customers), often on street poles or underground in urban settings.
    """)

col1, col2, col3 = st.columns([0.1, 50, 0.1])  # Proportions for centering the image

image_path = project_root / "assets" / "supplychain.png"
image_path_str = image_path.as_posix() # Convert the path to a POSIX-style string (with forward slashes)

with col2:
    st.image(image_path_str, width=1000)

st.header("2. What Role Does Jemena Play?")
st.write(
    """
    Distribution is Jemena’s position in the supply chain (a **DNSP** or Distribution Network Service Provider). In Victoria, Jemena covers the electricity needs of a variety of different types of customers. 
    This includes residential and industrial areas, small businesses and even Melbourne International Airport. To do so, Jemena owns and operates important infrastructure such as these terminal stations, 
    transmission lines and many different types of transformers. Distribution involves carrying electricity locally from terminal stations to businesses and homes. 
    This electricity is transported via overhead power lines, and is stepped down again via smaller transformers before being sent into customers’ homes as the commonly used 230V standard.
    """
)

image_path = project_root / "assets" / "JEM_facts.png"
image_path_str = image_path.as_posix() # Convert the path to a POSIX-style string (with forward slashes)

with st.expander("Did you know?"):
    # st.write('''
    #     Jemena maintains more than 107,000 poles and their wires, with approximately 78,500 public lights under our service.
    #          ''')
    st.image(image_path_str)
st.write(
    """
    As a distribution network service provider (DNSP), Jemena is responsible for building, maintaining and operating its distribution network. To ensure the quality of service, Jemena is responsible for following the:
    - [National Electricity Rules](https://www.aemc.gov.au/regulation/energy-rules/national-electricity-rules)
    - [Victorian Electricity System Code](https://www.esc.vic.gov.au/sites/default/files/documents/3d1fc9fd-18e0-4e10-a87a-e68ba2151a1a.pdf)
    - [Victoria Electricity Distribution Code](https://www.esc.vic.gov.au/electricity-and-gas/codes-guidelines-and-policies/electricity-distribution-code)
    - [JEN's Electricity Distribution Licence](https://www.esc.vic.gov.au/sites/default/files/documents/323f2265-cbe0-4664-be1d-326d2e8f920f.pdf)
    """ 
)
st.write(
    """
    Additionally, as a distribution network, Jemena is required to meet reliability standards to manage network limitations:

    - **Thermal**: asset utilisation must be managed in order to ensure that there are no overloads (potential asset failures or electrical safety clearance violations)
    - **Voltage**: Excessively high or low voltages result in accelerated loss of life in customer appliances or other safety issues
    - **Fault level**: prevent switchgear replacement, conductor and cable sizes must be adequately selected to withstand fault level requirements
    - **Redundancy**: In the case of emergency or maintenance, following a "n-1" rule in network planning allows for planned or unexpected failures to have less impact on network stability.
    """
)
with st.expander("What is n-1?"):
    st.write('''
            A n-1 redundancy system in the context of the electricity network is one in which there is a backup route of electricity delivery should one component in a network line fail.
            Without it, a single component failure could result in widespread outages. 
             ''')
st.write(
    """
    Combined, these reliability and quality standards ensure that the grid is resilient enough to manage the load and support current and potentially forecasted customer demands.

    """
)
st.write(
    '''
    As Australia's power landscape is changing, Jemena has an increasing responsibility for recognising and adapting to changes to electricity networks from:
    - Customers generating their own power (PV installations)
    - Injection of renewables into the grid (wind and solar farms)
    - Accelerating development of power hungry data centres
    '''
)

image_path = project_root / "assets" / "JEM_network.jpg"
image_path_str = image_path.as_posix() # Convert the path to a POSIX-style string (with forward slashes)

st.header("3. Where does Jemena service?")
st.write('''
        Jemena's disribution area extends over the North-West of Melbourne. This distribution area covers a mix of industrial, commercial and residential customers,
        some major transport routes as well as the Melbourne International Airport. Semi-rural areas (though rapidly developing) exist around Sydenham, Sunbury and Coolaroo.
        The Jemena Network environment is bordered by the Yarra river in the East and Port Phillip Bay in the south.
        ''')
st.image(image_path_str, caption="The Jemena Electricity Network")
# ---------------------------
# Interactive Quiz / Elements
# ---------------------------
st.subheader("Test Your Understanding")
st.markdown("""
    **Answer the following questions to check your understanding of Jemena's role as a DNSP.**
    """)

with st.form("quiz_q1"):
    # 1. Checkbox-based question
    st.write("**Q1: Which part of the grid handles the highest voltage?**")
    if st.checkbox("Transmission"):
        st.success("Correct! Transmission lines handle the highest voltages.")
    if st.checkbox("Distribution"):
        st.error("Distribution lines carry electricity at lower voltages to the end users.")

    image_path = project_root / "assets" / "JEN_customers.png"
    image_path_str = image_path.as_posix() # Convert the path to a POSIX-style string (with forward slashes)
    submitted = st.form_submit_button("Submit")

with st.form("quiz_q2"):
    st.write("**Q2: Approximately how many customers do you think Jemena services?**")
    answer_q2 = st.radio(
        "",
        [" ","100,000", "200,000", "300,000", "400,000"]
    )
    st.markdown(
            """
        <style>
            div[role=radiogroup] label:first-of-type {
                visibility: hidden;
                height: 0px;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
    if answer_q2==("100,000"):
        st.error("Jemena services more customers than this!")
    elif answer_q2==("200,000"):
        st.error("Jemena services more customers than this!")
    elif answer_q2 == ("300,000"):
        st.error("Jemena services more customers than this!")
    elif answer_q2==("400,000"):
        st.success("Correct! Jemena services more than 387,000 customers for their electricity needs!")
        st.image(image_path_str, caption="The Jemena Customer Breakdown")
    submitted2 = st.form_submit_button("Submit")

with st.form("quiz_q3"):
    # 2. Buttons question
    st.write("**Q3: Which segment of the network typically operates at 120 V or 240 V for homes?**")
    answer_q3 = st.radio(
        "",
        [" ", "Transmission Network", "Distribution Network"]
    )
    if answer_q3 == "Transmission Network":
        st.error("Not quite. Transmission lines operate at much higher voltages.")
    elif answer_q3 == "Distribution Network":
        st.success("Correct! Distribution lines usually serve customers at these lower voltage levels.")
    submitted3 = st.form_submit_button("Submit")

with st.form("quiz_q4"):
    # 4. Slider to guess typical medium voltage range
    st.write("**Q4: Guess the typical medium-voltage range (in kV) used in distribution.**")
    medium_voltage_guess = st.slider("Select kV range", min_value=1, max_value=50, value=5, key = "q4_slider")
    # if 4 <= medium_voltage_guess <= 35:
    #     st.success("You're correct! Medium-voltage lines are often between 4 kV and 35 kV.")
    # else:
    #     st.info("Typically, medium-voltage lines range from about 4 kV to 35 kV.")

    submitted4= st.form_submit_button("Submit")
    if submitted4:
        if 4 <= medium_voltage_guess <= 35:
            st.success("You're correct! Medium-voltage lines are often between 4 kV and 35 kV.")
        else:
            st.info("Not quite, typically, medium-voltage lines range from about 4 kV to 35 kV.")


# ---------------------------
# Conclusion / Thank You
# ---------------------------
st.write("---")
st.write("### Thank you for learning about Electricity Distribution Networks!")
st.write(
    """
    Feel free to explore more about how power is transmitted and distributed 
    to our homes, businesses, and industries. 
    """
)


