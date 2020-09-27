import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# 引入 Staffs.py 里面增删改查员工的方法
from Staffs import create_staff, delete_staff, update_staff, find_staff, search_all_staff, create_staff_table, \
    close_database
# 引入 Orders.py 里面增删改查需求的方法
from Orders import create_order_table, create_order, search_all_order, find_order

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app=app)

items = {"foo": "The Foo Wrestlers"}

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# 创建员工类
class Staff(BaseModel):
    id: str = None
    username: str = None
    password: str = None


# 查找员工类
class FindStaff(BaseModel):
    username: str = None
    password: str = None


# 创建需求类
class Order(BaseModel):
    orderid: str = None
    createuser: str = None
    orderaddress: str = None
    orderphonenum: str = None
    createdate: str = None
    starttime: str = None
    endtime: str = None
    ordertype: int = None
    orderdesc: str = None
    orderprice: float = None
    orderrate: float = None
    orderpic: str = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 新增员工
@app.post("/createstaff/")
async def createstaff(staff: Staff):
    data = create_staff(staff.id, staff.username, staff.password)
    return data


# 删除员工
@app.post("/deletestaff/")
async def deletestaff(id):
    data = delete_staff(id)
    return data


# 更改员工
@app.post("/updatestaff/")
async def updatestaff(staff: Staff):
    data = update_staff(staff.id, staff.username, staff.password)
    return data


# 查找某个员工
@app.post("/findstaff/")
async def findstaff(staff: FindStaff):
    data = find_staff(staff.username, staff.password)
    jsonable_encoder({"status": "ok", "info": "%s登录成功" % staff.username, "session": staff.username})
    return data


# 查找所有员工
@app.get("/searchallstaff")
async def searchallstaff():
    data = search_all_staff()
    return data


# 创建 staff（员工）表
@app.get("/createstafftable")
async def createstafftable():
    data = create_staff_table()
    return data


# 关闭连接
@app.get("/closestaffdb")
async def closestaffdb():
    data = close_database()
    return data


# 新建需求
@app.post("/createorder")
async def createorder(order: Order):
    data = create_order(
        order.orderid,
        order.createuser,
        order.orderaddress,
        order.orderphonenum,
        order.createdate,
        order.starttime,
        order.endtime,
        order.ordertype,
        order.orderdesc,
        order.orderprice,
        order.orderrate,
        order.orderpic,
    )
    return data


# 查找特定需求
@app.post("/findorder")
async def findorder(orderid):
    data = find_order(orderid)
    return data


# 查找所有员工
@app.get("/searchallorder")
async def searchallorder():
    data = search_all_order()
    return data


# 新建需求表
@app.get("/createordertable")
async def createorderstatble():
    data = create_order_table()
    return data
