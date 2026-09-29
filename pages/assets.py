import streamlit as st

from services.asset_service import (
    create_asset,
    get_assets
)

st.title("Assets")

with st.form("new_asset"):

    asset_id = st.text_input(
        "Asset ID"
    )

    filename = st.text_input(
        "Filename"
    )

    filepath = st.text_input(
        "File Path"
    )

    submit = st.form_submit_button(
        "Create Asset"
    )

    if submit:

        create_asset(
            asset_id,
            filename,
            filepath
        )

        st.success(
            "Asset created."
        )

st.divider()

assets = get_assets()

for asset in assets:

    st.write(
        f"{asset['filename']}"
    )

    st.caption(
        asset['filepath']
    )

    st.divider()