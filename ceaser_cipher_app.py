import streamlit as st

def ceasar(text, shift, direction):
    alphabet =[chr(i) for i in range(ord("a"), ord("z")+1)]
    if direction == "decode":
        shift *= -1
    output = ''
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos + shift) % len(alphabet)
            output += alphabet[new_pos]
        else:
            output += char
    return output

st.title("Ceasars Cipher")

direction = st.radio("Choose an Option: ", ["encode", "decode"])
text = st.text_input("Enter your message: ")
shift = st.slider("Shift number: ", 1, 25, 3)

if st.button("Submit"):
    result = ceasar(text.lower(), shift, direction)
    st.success(f"Result: {result}")