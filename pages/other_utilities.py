import streamlit as st
from pathlib import Path

script_dir = Path(__file__).parent
project_root = script_dir.parent
image = project_root / "assets" / "gas1.png"
image_path_str = image.as_posix()
# --- Fixing radio button preselection ---
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

st.title("Other Utilities")

st.header("1. Jemena Gas Networks (JGN)?")
st.markdown("""
            Jemena owns and operates a diverse portfolio of energy assets across northern Australia and the East Coast, 
            accounting for more than $12.4 billion worth of major utility infrastructure. 
            Apart from the Jemena Electricity Networks (JEN), Jemena also owns and operates a major gas network; Jemena Gas Networks (JGN). 
            
            
            
            """)
st.markdown("""
            Similar to the stages of electricity, the gas network has 4 main stages from production to its eventual usage. View these stages below:
            """)



tab1, tab2, tab3, tab4 = st.tabs(["Production", "Transmission", "Distribution", "Retailer"])

with tab1:
    container = st.container(border=True)
    with container:
        st.image(image_path_str, use_container_width=True)
        st.write('''
                Natural gas is sourced from natural gas wells and processed.
                    ''')

with tab2:
    container = st.container(border=True)
    with container:
        image = project_root / "assets" / "gas2.png"
        image_path_str = image.as_posix()
        st.image(image_path_str, use_container_width=True)
        st.write('''
                The transporting of natural gas over long distances.
                    ''')

with tab3:
    container = st.container(border=True)
    with container:
        image = project_root / "assets" / "gas3.png"
        image_path_str = image.as_posix()
        st.image(image_path_str, use_container_width=True)
        st.write('''
                The transporting of natural gas to customers from major pipelines.
                    ''')

with tab4:
    container = st.container(border=True)
    with container:
        image = project_root / "assets" / "gas4.png"
        image_path_str = image.as_posix()
        st.image(image_path_str, use_container_width=True)
        st.write('''
                The management of customer gas accounts and billing.
                    ''')


st.markdown("""
            As part of these network stages, Jemena is responsible for the :red-background[transmission] and :blue-background[distribution] of gas, offering producers and end-customers a safe and reliable means of transport and supply whilst keeping in mind our customer values.
            """)
    

st.title("2. Transmission")
st.markdown("""
            This network consists of some of Australia’s most important gas transmission pipelines. Jemena wholly owns 8 pipelines operating through the Northern Territory, Queensland, NSW and Victoria. Each pipeline is responsible for the transport of gas from processing plants to distributors. Jemena’s pipeline infrastructure is a cornerstone in creating a cohesive network between different state networks.            
""")
st.markdown('''
            Additionally, Jemena has part ownership of:
            - ActewAGL Gas and Electricity Networks, managing part of the ACT gas network.
            - The United Energy gas network. Jemena owns 34 percent of this 13,000km network that services more than 640,000 homes and businesses in south-east Melbourne and the Mornington Peninsula.
            ''')
image = project_root / "assets" / "JGN_transmission_map.jpg"
image_path_str = image.as_posix()
st.image(image_path_str, use_container_width=True, caption="Jemena Gas Transmission Pipelines")
st.subheader('''
            Jemena Gas Pipelines:
             ''')
expander1 = st.expander("NT")
expander1.write("[Northern Gas Pipeline](https://www.jemena.com.au/gas/pipelines/Northern-Gas-Pipeline/) - Interstate with Queensland")
expander2 = st.expander("QLD")
expander2.write("""
                - [Queensland Gas Pipeline](https://www.jemena.com.au/gas/pipelines/Queensland-Gas-Pipeline/)
                - [Atlas Gas Processing Facility](https://www.jemena.com.au/gas/pipelines/Atlas-Processing-Facility-Pipeline/)
                - [Roma North Processing Facility](https://www.jemena.com.au/gas/pipelines/Roma-North-Gas-Pipeline/)
                - [Darling Downs Pipelines](https://www.jemena.com.au/gas/pipelines/darling-downs-pipeline/)
                 """)
expander3 = st.expander("NSW")
expander3.write("""
                - [Colongra Gas Transmission and Storage Pipeline](https://www.jemena.com.au/gas/pipelines/colongra-pipeline/)
                - [Eastern Gas Pipeline](https://www.jemena.com.au/gas/pipelines/Eastern-Gas-Pipeline/) - Interstate with Victoria
                 """)
expander4 = st.expander("VIC")
expander4.write("""
                - [Vichub](https://www.jemena.com.au/gas/pipelines/Vichub/)
                 """)

st.title("3. Distribution")
st.markdown('''
            Jemena is the largest gas distributor in New South Wales. Jemena’s network is the sole distributor of natural gas to 1.6 million residential businesses and industrial sites in NSW, 
            including both metro and regional areas. Totalling more than 25,000km, Jemena manages this network to ensure safe and reliable access to natural gas. 
            Currently, Jemena Gas Networks (JGN) has 26 retailers and 14 self-contracting users using its services.
            ''')
image = project_root / "assets" / "JGN_distribution_map.jpg"
image_path_str = image.as_posix()
st.image(image_path_str, use_container_width=True, caption="Jemena Gas Distribution Map")

# --- Quiz ---
st.title("4. Quiz")
with st.form("quiz_form"):
    st.subheader("Test Your Knowledge")
    
    # Question 1
    st.write("Which part of the stages of gas does Jemena play a role in?")
    q1_score = 0
    if st.checkbox("Production"):
        st.error("Not quite, Jemena is not involved with natural gas sourcing.")
        if q1_score > 0:
            q1_score-=0.5
    if st.checkbox("Transmission"):
        st.success("Correct!")
        q1_score+=1
    if st.checkbox("Distribution"):
        st.success("Correct!")
        q1_score+=1
    if st.checkbox("Retail"):
        st.error("Not quite, Jemena does not front bills to customers")
        if q1_score > 0:
            q1_score-=0.5
    
    # Question 2
    q2 = st.radio(
        "True or False: Jemena is the largest gas distributor in New South Wales:",
        options=["", "True","False"],
        key="q2"
    )
    
    # Question 3 
    q3 = st.radio(
        " ",
        options=[
            "",
            "",
            "",
            "",
            ""
        ],
        key="q3"
    )
    
    # Submit Button
    submit_button = st.form_submit_button("Submit Answers")
    
    if submit_button:
        st.write("### Results")
        correct_answers = {
            "q2": "True",
            "q3": "To provide financial backing and access to global resources"
        }
        
        score = 0
        if q1_score == 2:
            score += 1
        elif q1_score == 1:
            score+=0.5
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