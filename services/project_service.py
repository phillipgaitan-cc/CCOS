from services.db import get_connection


def create_project(
    asana_task_id,
    task_name,
    local_project_path="",
    onedrive_folder_path=""
):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO projects (
            asana_task_id,
            task_name,
            local_project_path,
            onedrive_folder_path
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            asana_task_id,
            task_name,
            local_project_path,
            onedrive_folder_path
        ),
    )

    conn.commit()
    conn.close()


def get_projects():
    conn = get_connection()

    projects = conn.execute(
        """
        SELECT *
        FROM projects
        ORDER BY task_name
        """
    ).fetchall()

    conn.close()

    return projects


def get_project_by_id(project_id):
    conn = get_connection()

    project = conn.execute(
        """
        SELECT *
        FROM projects
        WHERE id = ?
        """,
        (project_id,)
    ).fetchone()

    conn.close()

    return project