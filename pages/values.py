import streamlit as st
from pathlib import Path

st.title("What Are Our Values?")

script_dir = Path(__file__).parent
project_root = script_dir.parent 
image_path = project_root / "assets" / "group_values.png"
image_path_str = image_path.as_posix() # Convert the path to a POSIX-style string (with forward slashes)

# Text content
st.markdown(
    """
    **Values are important**, because whilst it’s important **WHAT** we deliver, it’s equally important **HOW** we deliver our outcomes. 
    
    Our Values should underpin everything we do – guiding the way we behave, speak, and act."""
)


st.image(
    image_path_str, caption="Jemena's Group Values", use_container_width=True)

st.write("---")

# Values in more detail.

principles = [
    {
        "title": "Better Together",
        "description": "We value the diversity of our people, working together to achieve great outcomes.",
        "what_it_is": [
            "Explore and be open to different views.",
            "Make commercial decisions that deliver best outcomes for our Group.",
            "Respectfully engage each other to achieve more together.",
            "Be open and trust one another."
        ],
        "what_it_is_not": [
            "Dismiss alternative views.",
            "Delays due to process or self-interest.",
            "Fail to consult.",
            "Blame others."
        ]
    },
    {
        "title": "Be Accountable",
        "description": "We accept responsibility to deliver our commitments.",
        "what_it_is": [
            "Take ownership to deliver agreed outcomes.",
            "Do what we say we will do.",
            "Acknowledge and learn from mistakes.",
            "Act with speed and simplicity to increase our competitiveness."
        ],
        "what_it_is_not": [
            "Make excuses.",
            "Fail to learn from experience.",
            "Lack of openness and transparency.",
            "It’s someone else’s problem."
        ]
    },
    {
        "title": "Find a Better Way",
        "description": "We find improved and innovative ways to work.",
        "what_it_is": [
            "Strive to always be better.",
            "Be bold, courageous, and curious.",
            "Learn from others.",
            "Anticipate and respond to new challenges."
        ],
        "what_it_is_not": [
            "Accept the way it’s always been.",
            "Limit ourselves.",
            "Slow to act.",
            "Relitigate decisions."
        ]
    },
    {
        "title": "Think Like a Customer",
        "description": "Our actions consider our customers, community, and other stakeholders.",
        "what_it_is": [
            "Walk in our customer’s shoes.",
            "Seek to understand our customer.",
            "Pride ourselves on great service.",
            "Deliver solutions that meet customer needs."
        ],
        "what_it_is_not": [
            "Don’t listen to our customer.",
            "Make assumptions.",
            "Deliver unwanted services.",
            "Communicate in a way our customers don’t understand."
        ]
    },
    {
        "title": "We Care",
        "description": "We value safety and wellbeing for ourselves, our community, and environment.",
        "what_it_is": [
            "Courage to speak up and put people first.",
            "Lean in and take personal responsibility.",
            "Check in and listen to understand.",
            "Support each other by being fair and inclusive."
        ],
        "what_it_is_not": [
            "Be complacent.",
            "Ignore concerns.",
            "Make assumptions or think that we know best.",
            "Being unavailable."
        ]
    }
]

for principle in principles:
    icons = {
        "Better Together": "🤝",
        "Be Accountable": "✅",
        "Find a Better Way": "🔍",
        "Think Like a Customer": "🛍️",
        "We Care": "❤️"
    }
    st.header(f"{icons[principle['title']]} {principle['title']}")
    st.write(principle["description"])

    with st.expander("**What it is...**"):
        for item in principle["what_it_is"]:
            st.write(f"- {item}")

    with st.expander("**What it is not...**"):
        for item in principle["what_it_is_not"]:
            st.write(f"- {item}")

    st.markdown("---")
