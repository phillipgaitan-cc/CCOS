import streamlit as st

from services.project_service import (
    get_project_by_id
)

st.title("Project Details")

if "selected_project_id" not in st.session_state:

    st.error(
        "No project selected."
    )

    st.stop()

project_id = st.session_state[
    "selected_project_id"
]

project = get_project_by_id(
    project_id
)

if not project:

    st.error(
        "Project not found."
    )

    st.stop()

st.subheader(
    project["task_name"]
)

st.write(
    f"**Task ID:** "
    f"{project['asana_task_id']}"
)

st.write(
    f"**Local Project Path:** "
    f"{project['local_project_path']}"
)

st.write(
    f"**OneDrive Folder:** "
    f"{project['onedrive_folder_path']}"
)

st.divider()

st.header("Assets")

st.info(
    "No assets linked yet."
)

if st.button("Back To Projects"):

    st.switch_page(
        "pages/projects.py"
    )
