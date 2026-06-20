import streamlit as st
import requests

s_url="http://127.0.0.1:8000"

st.title("food stall")


opt=st.sidebar.selectbox("choose below",["Post","Get","Delete","Put"])

if opt=="Post":
    with st.form("choose"):
        food_name=st.text_input("name")
        price=st.number_input("price")
        url=st.text_input("image_url",placeholder="enter image url")

        btn=st.form_submit_button("Upload")

        if btn:
            payload={
            "name":food_name,
            "price":price,
            "image":url
            }
            res=requests.post(f"{s_url}/upload_food",json=payload)  #json //files //params
            st.success(res.json()["msg"])
            # st.write(res.status_code)
            # st.write(res.json()["msg"])

if opt=="Get":
    btn=st.button("submit")
    if btn:
        res=requests.get(f"{s_url}/get_details")

        st.dataframe(res.json())


if opt=="Delete":
    input=st.number_input("id")
    if st.button("Delete"):
        res=requests.delete(f"{s_url}/foods/{input}")
        st.success(res.json()["msg"])


if opt=="Put":
    input=int(st.number_input("id"))
    if input:

        res = requests.get(f"{s_url}/update/{input}")

        if res.status_code == 200:

            data = res.json()

            food_name = st.text_input(
                "Food Name",
                value=data["food_name"]
            )

            price = st.number_input(
                "Price",
                value=float(data["price"])
            )

            url = st.text_input(
                "Image URL",
                value=data["url"]
            )

        if st.button("update"):
            payload = {
                "name":food_name,
                "price":price,
                "image":url
            }

            res=requests.put(f"{s_url}/update/{input}",json=payload)
            st.success(res.json()["msg"])

