import streamlit as st

from services.project_service import (
    create_project,
    get_projects
)

st.title("Projects")

with st.form("new_project"):

    task_id = st.text_input(
        "Asana Task ID"
    )

    task_name = st.text_input(
        "Task Name"
    )

    submit = st.form_submit_button(
        "Create Project"
    )

    if submit:

        create_project(
            task_id,
            task_name
        )

        st.success(
            "Project created."
        )

st.divider()

projects = get_projects()

for project in projects:

    project_label = (
        f"📁 {project['task_name']} | "
        f"Task ID: {project['asana_task_id']}"
    )

    if st.button(
        project_label,
        key=f"project_{project['id']}",
        use_container_width=True
    ):

        st.session_state[
            "selected_project_id"
        ] = project["id"]

        st.switch_page(
            "pages/project_detail.py"
        )

    st.divider()