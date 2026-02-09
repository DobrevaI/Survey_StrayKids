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
  if ans2=="Bangchan" or ans2=="CB97":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans3=st.text_input("Q3: Which member has three cats(Soonie, Doongie, Dory)?")
if st.button("Check q3"):
  if ans3=="Lee Know" or ans3=="Lee Minho" or ans3=="Lino":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans4=st.text_input("Q4: Who is the main rapper?")
if st.button("Check q4"):
  if ans4=="Han" or ans4=="Han Jisung" or ans4=="J. One":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans5=st.text_input("Q5: Who is the youngest?")
if st.button("Check q5"):
  if ans5=="I.N" or ans5=="IN" or ans5=="in" or ans5=="Jeongin":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans6=st.text_input("Q6: Who is know as a puppy?")
if st.button("Check q6"):
  if ans6=="Seungmin":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans7=st.text_input("Q7: Who has had a buzz cut?")
if st.button("Check q7"):
  if ans7=="Hyunjin":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans8=st.text_input("Q8: Who is the sunshine of the group?")
if st.button("Check q8"):
  if ans8=="Felix" or ans5=="Yongbok":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
ans9=st.text_input("Q9: Who is the the 'protein king' of the group?")
if st.button("Check q9"):
  if ans9=="Changbin" or ans9=="SpearB":
    st.success("That is correct")
  else:
    st.error("Ohhhh that would be incorrect")
