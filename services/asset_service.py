from services.db import get_connection


def create_asset(
    asset_id,
    filename,
    filepath,
    media_type="",
    thumbnail_path=""
):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO assets (
            asset_id,
            filename,
            filepath,
            media_type,
            thumbnail_path
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            asset_id,
            filename,
            filepath,
            media_type,
            thumbnail_path
        )
    )

    conn.commit()
    conn.close()


def get_assets():

    conn = get_connection()

    assets = conn.execute(
        """
        SELECT *
        FROM assets
        ORDER BY filename
        """
    ).fetchall()

    conn.close()

    return assets