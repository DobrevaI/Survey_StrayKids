import streamlit as st
st.title("Stray kids survey")
st.text("This survey will test your Stray Kids knowledge :)")
ans1=st.text_input("Question1: How is Stray Kids' sortened name?")
ans2=st.text_input("Question2: Who is the leader?")
if st.button("Check"):
  if ans1==("skz") or ans1=="SKZ":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
  if ans2=="Bangchan":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
