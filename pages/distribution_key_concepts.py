import streamlit as st

# Page Config
# ---------------------------
st.set_page_config(
    page_title="Electricity Distribution Network",
    layout="centered"
)

col1, col2, col3 = st.columns([9, 11, 11])

# ---------------------------
# Jemena Image 
# ---------------------------
with col2:
    st.image(
        r"C:\Users\kzammit\OneDrive - onlineeportal\Documents\GitHub\Internship-2025\Jemena_BrandMark_RGB_000.png"
        # r"C:\Users\bpoort\OneDrive - onlineeportal\Desktop\web_app\images\Jemena_BrandMark_RGB_000.png"
    )

# ---------------------------
# Main Title
# ---------------------------
st.title("Key concepts of Distribution")

st.write(
    """
   Understanding power distribution and its key concepts is essential for maintaining stable and 
   safe electrical systems. Electricity flows from the power stations, then the current is sent through transformers that 
   increase voltage so power can e pushed over long distances. The charge is then carried by transmission lines to a substation 
   where the voltage is lowered so it can be sent on smaller power lines to your honme. The retailer then quantifies your usage before you are sent the bill.
    """
)


st.image(
        r"C:\Users\kzammit\OneDrive - onlineeportal\Documents\GitHub\Internship-2025\distribution_flowchart.PNG",caption = "Distribution Flowchart", use_container_width=True)
        # r"C:\Users\bpoort\OneDrive - onlineeportal\Desktop\web_app\images\Jemena_BrandMark_RGB_000.png"


st.subheader("Main components of the distribution system")
st.write(
    """
    Substations:
    - Control the flow of electricity through  
    - Use step-down transformers to reduce voltage for local distribution
    - Use Switchgear and circuit breakers help to protect the grid by isolating faults and prevent expansion of the outage by disconnecting affected area. 
   
    Distribution lines:
    - low voltage for homes and buisnesses 
    - Medium/high voltage for industry

    Transformers:
     Transformers are used to either step up or step down the voltage of electricity, they also ensure safe transmission and distribution across the grid 

    Feeders: 
     Feeders carry electricity form substations to various distribution points such as trasformers directly to consumers. Thus, feed electrical power to lower-voltage parts of the grid. 
     
    """
)


# Question 1
st.write("**Q1: What is the primary function of substations?**")
answer_q1 = st.radio(
    "",
    ["To increase the voltage of electricity for long-distance transmission", 
     "To control the flow of electricity and reduce voltage for local distribution", 
     "To generate electricity for distribution", 
     "To provide backup power during outages"]
)
if answer_q1 == "To increase the voltage of electricity for long-distance transmission":
    st.error("Not quite. Substations control the flow and reduce voltage, not increase it.")
elif answer_q1 == "To control the flow of electricity and reduce voltage for local distribution":
    st.success("Correct! Substations help control the flow and reduce voltage for local distribution.")
elif answer_q1 == "To generate electricity for distribution":
    st.error("Not quite. Substations control electricity flow, but don't generate it.")
elif answer_q1 == "To provide backup power during outages":
    st.error("Not quite. Substations help manage the grid but do not provide backup power.")

# Question 2
st.write("**Q2: What role do transformers play in the electrical grid?**")
answer_q2 = st.radio(
    "",
    ["They help to prevent electrical faults from spreading",
     "They store electrical energy for later use",
     "They step up or step down voltage for safe transmission and distribution",
     "They distribute electricity directly to consumers"]
)
if answer_q2 == "They help to prevent electrical faults from spreading":
    st.error("Not quite. Transformers are used to adjust voltage levels, not prevent faults.")
elif answer_q2 == "They store electrical energy for later use":
    st.error("Not quite. Transformers don't store energy—they change voltage levels.")
elif answer_q2 == "They step up or step down voltage for safe transmission and distribution":
    st.success("Correct! Transformers adjust voltage to ensure safe transmission and distribution.")
elif answer_q2 == "They distribute electricity directly to consumers":
    st.error("Not quite. Transformers are part of the distribution system but don't directly deliver to consumers.")

# Question 3
st.write("**Q3: What is the purpose of switchgear and circuit breakers in substations?**")
answer_q3 = st.radio(
    "",
    ["To increase the voltage of electricity",
     "To isolate faults and prevent outages from spreading",
     "To generate electricity",
     "To convert electricity into usable power for businesses"]
)
if answer_q3 == "To increase the voltage of electricity":
    st.error("Not quite. Switchgear and circuit breakers protect the grid but do not increase voltage.")
elif answer_q3 == "To isolate faults and prevent outages from spreading":
    st.success("Correct! They help protect the grid by isolating faults and preventing the spread of outages.")
elif answer_q3 == "To generate electricity":
    st.error("Not quite. Switchgear and circuit breakers protect the grid but don't generate electricity.")
elif answer_q3 == "To convert electricity into usable power for businesses":
    st.error("Not quite. Their job is to protect the grid, not convert electricity for use.")

# Question 4
st.write("**Q4: What is the primary function of feeders in the electrical grid?**")
answer_q4 = st.radio(
    "",
    ["To increase the voltage for long-distance transmission",
     "To carry electricity from substations to transformers or consumers",
     "To distribute electricity to businesses",
     "To store electrical energy for later use"]
)
if answer_q4 == "To increase the voltage for long-distance transmission":
    st.error("Not quite. Feeders carry electricity to lower-voltage areas, not for transmission.")
elif answer_q4 == "To carry electricity from substations to transformers or consumers":
    st.success("Correct! Feeders transport electricity to lower-voltage areas of the grid.")
elif answer_q4 == "To distribute electricity to businesses":
    st.error("Not quite. Feeders are part of the distribution system but not specifically for businesses.")
elif answer_q4 == "To store electrical energy for later use":
    st.error("Not quite. Feeders carry electricity, they do not store it.")

# Question 5
st.write("**Q5: What type of voltage do distribution lines generally carry for homes and businesses?**")
answer_q5 = st.radio(
    "",
    ["High voltage", "Low voltage", "Medium voltage", "Extra-high voltage"]
)
if answer_q5 == "High voltage":
    st.error("Not quite. High voltage is typically used for long-distance transmission, not distribution.")
elif answer_q5 == "Low voltage":
    st.success("Correct! Distribution lines for homes and businesses usually carry low voltage.")
elif answer_q5 == "Medium voltage":
    st.error("Not quite. Distribution lines typically use low voltage for residential areas.")
elif answer_q5 == "Extra-high voltage":
    st.error("Not quite. Extra-high voltage is not used for distribution to homes or businesses.")



st.subheader("What is redundancy?")
st.write(
    """
   Redundancy refers to the practice of incorporating backup systems, equipment or infrastructure to ensure there is a continuous and reliable supply of electricity. This means that in the case of one distribution network failing, there are still ways to supply people with energy. This is essential for minimising outages, maintaining grid stability and ensuring customers have a constant power supply. 
    """
)


st.subheader("Types of distribution network configurations")

st.write(
    """
    - Radial (single direction. Cost effective but vulnerable to outages) 
    - Looped (multiple paths that connect and supply consumers. It creates redundancy but if one fails there is another that can deliver power. Reliable but expensive) 
    - Mesh ( complex and resilient with multiple interconnections between different parts of the system. Reliable in densely populated areas. 
   
    """
)

# Question 1 - Multiple Choice
st.write("**Q1: Which of the following is a characteristic of a radial distribution network configuration?**")
answer_q1 = st.radio(
    "",
    ["Cost-effective but vulnerable to outages", 
     "Creates redundancy and is highly reliable", 
     "Expensive but has multiple paths", 
     "Highly resilient with multiple interconnections"]
)
if answer_q1 == "Cost-effective but vulnerable to outages":
    st.success("Correct! Radial networks are cost-effective but vulnerable to outages.")
else:
    st.error("Not quite. Radial networks are cost-effective but vulnerable to outages.")

# Question 2 - Multiple Choice with Explanation
st.write("**Q2: What is a mesh distribution network configuration?**")
answer_q2 = st.radio(
    "",
    ["Simple with single connection paths", 
     "Resilient with multiple interconnections, reliable in densely populated areas", 
     "Low-cost but prone to failures", 
     "Relies on a single power path"]
)
if answer_q2 == "Resilient with multiple interconnections, reliable in densely populated areas":
    st.success("Correct! Mesh networks are complex and highly resilient, especially in densely populated areas.")
else:
    st.error("Not quite. Mesh networks are highly resilient, but they involve complex interconnections.")

# Question 3 - True or False
st.write("**Q3: A looped distribution network creates redundancy and can deliver power if one path fails.**")
answer_q3 = st.radio(
    "",
    ["True", "False"]
)
if answer_q3 == "True":
    st.success("Correct! Looped networks have multiple paths, providing redundancy and reliability.")
else:
    st.error("Not quite. Looped networks are designed to be reliable and provide redundancy.")


st.subheader("What is metering?")

st.write(
    """
    Metering refers to the process of measuring and recording the consumption of electricity, gas, water, or other utilities by customers or in industrial settings. There are 3 different types of meters predominantly used by Jemena:

    - Smart meters: These are electronic meters that record energy consumption in 30-minute intervals. Smart meters communicate information to Jemena who then pass it to the electricity retailer for billing. Jemena has installed smart meters in more than 99 percent of homes and businesses.
    - Digital meters: Primarily used to measure gas volumes 
    - Current transformer meters: used to convert high current/voltage to lover values for the meter to be able to read what is passing through the cables. These are used for an electrical capacity above 76Amps per phase up until high voltage supplies. 
   
    """
)

col111  , col222= st.columns([9, 11])

with col111:
    st.image(
            r"C:\Users\kzammit\OneDrive - onlineeportal\Documents\GitHub\Internship-2025\jemena-smart-meter.png", caption= "Jemena smart meter", use_container_width=True)
            # r"C:\Users\bpoort\OneDrive - onlineeportal\Desktop\web_app\images\Jemena_BrandMark_RGB_000.png"


# Question 4 - Multiple Choice with Custom Feedback
with col222:
    st.write("**Q4: Which of these meters is used to convert high current/voltage to lower values for easy measurement?**")
    answer_q4 = st.radio(
        "",
        ["Smart meters", 
        "Digital meters", 
        "Current transformer meters", 
        "Analog meters"]
    )
    if answer_q4 == "Current transformer meters":
        st.success("Correct! Current transformer meters are used to step down high current/voltage for accurate readings.")
    else:
        st.error("Not quite. Current transformer meters are used for measuring high electrical capacity.")


# Question5 - Short Answer
st.write("**Q5: What is the primary purpose of metering?**")
answer_q5 = st.text_input(
    "Type your answer here"
)
if answer_q5.strip().lower() == "measuring and recording the consumption of electricity":
    st.success("Correct! Metering involves measuring and recording energy consumption.")
else:
    st.error("Not quite. Metering is the process of measuring and recording energy consumption.")

# Question 6 - Multiple Choice with Multiple Correct Answers
st.write("**Q6: Which of the following meters are used by Jemena? (Select all that apply)**")
answer_q6 = st.multiselect(
    "",
    ["Smart meters", "Digital meters", "Current transformer meters", "Analog meters"]
)
if "Smart meters" in answer_q6 and "Digital meters" in answer_q6 and "Current transformer meters" in answer_q6:
    st.success("Correct! Jemena uses smart, digital, and current transformer meters.")
else:
    st.error("Not quite. The correct answers are Smart meters, Digital meters, and Current transformer meters.")

# Two columns to compare Transmission and Distribution side-by-side
col11,col22= st.columns(2)

with col11:
    st.subheader("Primary Distribution")
    st.markdown("""
    The main function of primary distribution is to transport electricity form the substation to the local distribution transformers. These distribution lines conduct higher voltages. This system covers larger distances.
    """)

with col22:
    st.subheader("Secondary distribution")
    st.markdown("""
    The main function of secondary distribution is to distribute energy at lower voltages from the local transformers to homes and other end users.
    """)

# Question 7 - Multiple Choice with Correct/Incorrect Feedback
st.write("**Q7: What is the primary function of secondary distribution?**")
answer_q7 = st.radio(
    "",
    ["Transporting electricity from substations to local transformers", 
     "Delivering energy at lower voltages to end users", 
     "Carrying high voltage across large distances", 
     "Converting electricity for industrial use"]
)
if answer_q7 == "Delivering energy at lower voltages to end users":
    st.success("Correct! Secondary distribution delivers energy at lower voltages to homes and businesses.")
else:
    st.error("Not quite. Secondary distribution is responsible for delivering energy at lower voltages.")


# Question 8 - Dropdown for Single Answer
st.write("**Q8: Which distribution system covers larger distances and conducts higher voltages?**")
answer_q8 = st.selectbox(
    "",
    ["Primary distribution", "Secondary distribution"]
)
if answer_q8 == "Primary distribution":
    st.success("Correct! Primary distribution covers larger distances and conducts higher voltages.")
else:
    st.error("Not quite. Secondary distribution operates at lower voltages and is closer to end users.")

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
