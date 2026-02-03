import streamlit as st
st.title("Stray kids survey")
st.text("This survey will test your Stray Kids knowledge :)")
ans1=st.text_input("Q1: How is Stray Kids' sortened name?")
if st.button("Check q1"):
  if ans1==("skz") or ans1=="SKZ":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans2=st.text_input("Q2: Who is the leader?")
if st.button("Check q2"):
  if ans2=="Bangchan":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans3=st.text_input("Q3: Which member has three cats(Soonie, Doongie, Dory)?")
if st.button("Check q3"):
  if ans3=="Lee Know" or "Lee Minho" or "Lino":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans4=st.text_input("Q4: Who is the main rapper?")
if st.button("Check q4"):
  if ans4=="Han" or "Han Jisung" or "J.One":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans5=st.text_input("Q5: Who is the youngest?")
if st.button("Check q5"):
  if ans5=="I.N" or "IN" or "in" or "Jeongin":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
