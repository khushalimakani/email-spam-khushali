import streamlit as st
import pickle

model=pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

st.title("Email spam Classification Application")

#run=    >streamlit run app.py

st.write("This is machine learning application to classify emails as spam or ham.")
user_input=st.text_area("Enter an email to claaify",height=150)
if st.button("Classify"):
    if user_input :
        data = [user_input]
        vect = cv.transform(data).toarray()
        pred = model.predict(vect)
        if pred[0]==0:
            st.success("This email is not spam")
        else:
            st.error("This is spam email")
    else:
        print("please type email")        