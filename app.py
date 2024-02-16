"""Streamlit simple app, calculating interests for the next years."""

import plotly.express as px
import streamlit as st
import yaml


# CONFIG
# Load config file
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
# Setup
K = config["k"]
RATE = config["rate"]
ANN_SAVINGS = config["ann_savings"]
DURATION = config["duration_yrs"]

# SESSION STATE INITIALIZATION
# Capital
if "k_slider" not in st.session_state:
    st.session_state.k_slider = K["init"]
if "k_input" not in st.session_state:
    st.session_state.k_input = K["init"]
# Rate
if "rate_slider" not in st.session_state:
    st.session_state.rate_slider = RATE["init"]
if "rate_input" not in st.session_state:
    st.session_state.rate_input = RATE["init"]
# Annual savings
if "ann_sav_slider" not in st.session_state:
    st.session_state.ann_sav_slider = ANN_SAVINGS["init"]
if "ann_sav_input" not in st.session_state:
    st.session_state.ann_sav_input = ANN_SAVINGS["init"]


# CALLBACKS
def k_from_slider():
    st.session_state.k_input = st.session_state.k_slider


def k_from_input():
    st.session_state.k_slider = st.session_state.k_input


def rate_from_slider():
    st.session_state.rate_input = st.session_state.rate_slider


def rate_from_input():
    st.session_state.rate_slider = st.session_state.rate_input


def ann_sav_from_slider():
    st.session_state.ann_sav_input = st.session_state.ann_sav_slider


def ann_sav_from_input():
    st.session_state.ann_sav_slider = st.session_state.ann_sav_input


# GUI
st.set_page_config(
    page_title="Picsou",
    page_icon="https://static.wikia.nocookie.net/bdpedia/images/3/3a/Scrooge_mcduck_good_guys_collab_by_phantom_akiko-d5o6mzu.png/revision/latest?cb=20130728102826&path-prefix=fr",
    layout="wide",
)
st.write("# ⚙️ L'appli arrive ! 🦄")
st.write(
    f"Intérêts annuels pour les {DURATION} prochaines années (brut et net, PFL inclus) et magie des intérêts composés."
)

col1, col2, col3 = st.columns(3)

# Capital setup
with col1:
    st.write("## Capital de départ : {:_} €".format(st.session_state.k_slider).replace("_", " "))
    k_slider = st.slider(
        "",
        min_value=K["min"],
        max_value=K["max"],
        step=K["step"],
        key="k_slider",
        on_change=k_from_slider,
    )
    k_input = st.number_input(
        "",
        min_value=K["min"],
        max_value=K["max"],
        step=K["step"],
        key="k_input",
        on_change=k_from_input,
    )

# Annual rate setup
with col2:
    st.write(f"## Taux d'intérêt annuel : {st.session_state.rate_slider :.0%}")
    rate_slider = st.slider(
        "",
        min_value=RATE["min"],
        max_value=RATE["max"],
        step=RATE["step"],
        key="rate_slider",
        on_change=rate_from_slider,
    )
    rate_input = st.number_input(
        "",
        min_value=RATE["min"],
        max_value=RATE["max"],
        step=RATE["step"],
        key="rate_input",
        on_change=rate_from_input,
    )

# Annual savings setup
with col3:
    st.write(
        "## Épargne annuelle : {:_} €".format(st.session_state.ann_sav_slider).replace(
            "_", " "
        )
    )
    ann_sav_slider = st.slider(
        "",
        min_value=ANN_SAVINGS["min"],
        max_value=ANN_SAVINGS["max"],
        step=ANN_SAVINGS["step"],
        key="ann_sav_slider",
        on_change=ann_sav_from_slider,
    )
    ann_sav_input = st.number_input(
        "",
        min_value=ANN_SAVINGS["min"],
        max_value=ANN_SAVINGS["max"],
        step=ANN_SAVINGS["step"],
        key="ann_sav_input",
        on_change=ann_sav_from_input,
    )

# DEBUG
"st.session_state object 👇", st.session_state


# COMPUTATION
# ...


# df = px.data.iris()

# fig = px.scatter(
#     df,
#     x="sepal_width",
#     y="sepal_length",
#     color="sepal_length",
#     color_continuous_scale="reds",
# )

# tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
# with tab1:
#     st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# with tab2:
#     st.plotly_chart(fig, theme=None, use_container_width=True)
