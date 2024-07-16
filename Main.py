import streamlit as st

st.title('Hello Nice to meet you! :)')
st.title('Here is :red[B]:blue[S]:orange[S]:green[M] !!')
st.subheader(' ', divider='rainbow')

st.subheader(' ')
st.image('https://hijob.pen.go.kr/upload/map/39(1).jpg')
st.link_button("BSSM home-page", "https://school.busanedu.net/bssm-h/main.do")


st.subheader(' ')
st.subheader('What are you curious about?')
st.page_link("pages/1_bssm.py", label="go to page: bssm")
st.page_link("pages/2_introduction.py", label="go to page: introduction")
st.page_link("pages/3_Quiz.py", label="go to page: Quiz")
st.page_link("pages/4_result.py", label="go to page: result")