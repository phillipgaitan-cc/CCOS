CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    asana_task_id TEXT UNIQUE NOT NULL,

    task_name TEXT NOT NULL,

    local_project_path TEXT,

    onedrive_folder_path TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_projects_task_name
ON projects(task_name);

CREATE INDEX IF NOT EXISTS idx_projects_task_id
ON projects(asana_task_id);
CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    asset_id TEXT UNIQUE,

    filename TEXT NOT NULL,

    filepath TEXT NOT NULL,

    media_type TEXT,

    thumbnail_path TEXT,

    duration REAL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS project_assets (
    project_id INTEGER NOT NULL,

    asset_id INTEGER NOT NULL,

    relationship_type TEXT DEFAULT 'linked',

    PRIMARY KEY(project_id, asset_id),

    FOREIGN KEY(project_id)
        REFERENCES projects(id),

    FOREIGN KEY(asset_id)
        REFERENCES assets(id)
);