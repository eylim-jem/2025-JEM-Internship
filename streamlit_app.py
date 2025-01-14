import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path

# --- Page Setup ---
 
# # --- OLD PAGES ---
# home_page = st.Page(
#     page = "pages/home.py",
#     title = "Home",
#     icon = ":material/house:",   
# )
# projects_page = st.Page(
#     page = "pages/projects.py",
#     title = "Projects", 
#     icon = ":material/rocket_launch:",
# )
# values_page = st.Page(
#     page = "pages/values.py",
#     title = "The Jemena Values",
#     icon = ":material/diversity_2:",
# )
# stakeholders_page = st.Page(
#     page = "pages/stakeholders.py",
#     title = "Our stakeholders",
#     icon = ":material/communication:",
# )
# zinfra_page = st.Page(
#     page = "pages/zinfra.py",
#     title = "Zinfra",
#     icon = ":material/engineering:",
# )

# Week 2

trans_dist_page = st.Page(
    page = "pages/trans_dist.py",
    title = "Transmission vs Distribution",
    icon = ":material/bolt:",   
)
distribution_concepts_page = st.Page(
    page = "pages/distribution_key_concepts.py",
    title = "Key Concepts of Distribution",
    icon = ":material/electrical_services:",   
)
distribution_role_page = st.Page(
    page = "pages/distribution_role.py",
    title = "Distribution in the Modern Grid",
    icon = ":material/wind_power:",   
)

# Week 3 pages

other_utilities_page= st.Page( 
    page = "pages/other_utilities.py",
    title = "Other utilities",
    icon = ":material/search:",   
)
business_model__page = st.Page( 
    page = "pages/business_model.py",
    title = "Business Model",
    icon = ":material/business:",   
)
organisation_structure_page= st.Page( 
    page = "pages/organisation_structure.py",
    title = "Organisation structure",
    icon = ":material/edit:",   
)



# --- Nav setup ---
pg = st.navigation(
    {
        # pages = [home_page, projects_page, values_page]
        # "Electricity": [home_page, projects_page, values_page],
        # "Assets and Operations": [stakeholders_page, zinfra_page],

        "Week 2 Deliverables": [trans_dist_page, distribution_concepts_page, distribution_role_page],
        "Week 3 Deliverables": [other_utilities_page, business_model__page, organisation_structure_page],
        "Week 4 Deliverables": [],
        "Week 5 Deliverables": [],
        "Week 6 Deliverables": [],
        "Week 7 Deliverables": [],

    }
)

# --- Run nav ---
pg.run()

# --- Logo (all pages) ---
script_dir = Path(__file__).parent
image_path = script_dir / "assets" / "Jemena_BrandMark_RGB_000.png"
image_path_str = image_path.as_posix() # Convert the path to a POSIX-style string (with forward slashes)
st.logo(image_path_str, link = "https://www.jemena.com.au/")

