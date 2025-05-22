import streamlit as st

with st.echo():
    import pandas as pd
    import streamlit as st
    st.title("Getting Started Streamlit")
    st.write("testing streamlit")

    st.markdown("## Code")

    cols1, cols2, cols3, cols4 = st.columns(4)

    with cols1:
        code = """
        print("hello world")
        """
        code_button = st.button("show code")

        if code_button:
            st.code(code, language="python")

    with cols2:
        text_inp = st.text_input("Input your age")
        word_tokenize = "|".join(text_inp.split())
        st.markdown(f"{word_tokenize}")

    with cols1:
        text = st.text_input("Input your text")
        st.markdown(f"{text}")

    df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 5, 30, 40]})
    with cols2:
        st.dataframe(df)

    chart_button = st.button("show chart")
    if chart_button:
        st.line_chart(df, x="first column", y="second column")
