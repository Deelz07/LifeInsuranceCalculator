import lifeinsurancetable as LI
import streamlit as st
# from txt_to_list import convert_to_table

table = LI.convert_to_table('lifetable.txt')
    
lifetable = LI.Lifetable(table,17)

st.title("Lifetable Calculator")

st.write("EPV of Assurance calculator")

start_age = st.slider("Starting Age", 17, 117)
end_age = st.slider("Contract End Age", 17, 117)


interest_rate = st.slider("Interest rate (%)",0,20)/100

assurance_epv = lifetable.disc_assurance_EV(interest_rate,start_age,end_age)

annuity_epv = lifetable.disc_annuity_EV(interest_rate,start_age,end_age)
sum_insured = st.number_input("Sum Insured", min_value=1000)
fairprice = assurance_epv*sum_insured/annuity_epv

# premium = calculate_premium(age, sum_insured)

if end_age > start_age:
    st.write("Expected value of contract is", assurance_epv)
    st.write("Expected value of annuity is:", annuity_epv )
    st.write("A fair annual premium under AM92 Basis is:", assurance_epv*sum_insured/(annuity_epv))
else:
    st.write("End age needs to be higher than start age")



# st.write 
# st.write("Premium:", premium)