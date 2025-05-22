import streamlit as st
import streamlit_shadcn_ui as ui

trigger_btn = ui.button(text="Trigger Button", key="trigger_btn")

ui.alert_dialog(show=trigger_btn, title="Alert Dialog", description="This is an alert dialog", confirm_label="OK", cancel_label="Cancel", key="alert_dialog1")

# st.title("Proficiency Voice Recognition")
#
# @st.dialog("Cast your vote")
# def vote(item):
#     st.write(f"Why is {item} your favorite?")
#     reason = st.text_input("Because...")
#     if st.button("Submit"):
#         st.session_state.vote = {"item": item, "reason": reason}
#         st.rerun()
#
# if "vote" not in st.session_state:
#     st.write("Vote for your favorite")
#     if st.button("A"):
#         vote("A")
#     if st.button("B"):
#         vote("B")
# else:
#     f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
#
#
