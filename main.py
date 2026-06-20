from fastapi import FastAPI
import mysql.connector

app=FastAPI()
conn_obj=mysql.connector.connect(
    host="localhost",
    password="S@nj@n@2005",
    database="food_stall",
    user="root"

)

cursor_obj=conn_obj.cursor(dictionary=True)


@app.get("/")
def home_fun():
    return {"msg":"server starting"}

@app.post("/upload_food")
def upload_food_data(payload:dict):
    query="""insert into foods_item(food_name, price, url)values(%s,%s,%s)"""
    Value=(
        payload["name"],
        payload["price"],
        payload["image"]
    )

    cursor_obj.execute(query,Value)
    conn_obj.commit()
    print(payload)
    return{
        "msg":"food_data is received"
    }


@app.get("/get_details")
def view_details():
    cursor_obj.execute("SELECT * FROM foods_item")
    foods=cursor_obj.fetchall()
    return foods

@app.delete("/foods/{input}")
def delete_fun(input:int):
    cursor_obj.execute("delete from foods_item where id=%s",(input,))
    conn_obj.commit()
    return {"msg":"food deleted successfully"}


@app.get("/update/{input}")
def get_food(input:int):

    query="select * from foods_item where id=%s"
    cursor_obj.execute(query,(input,))

    food=cursor_obj.fetchone()

    return food

@app.put("/update/{input}")
def update_fun(input:int,payload:dict):
    query="""update foods_item set food_name=%s,price=%s,url=%s where id=%s"""
    values=(
        payload["name"],
        payload["price"],
        payload["image"],
        input
    )
    cursor_obj.execute(query,values)
    conn_obj.commit()
    return{
        "msg":"updated successfully"
    }


