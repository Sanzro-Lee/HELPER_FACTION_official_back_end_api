import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from Staffs import create_staff, delete_staff, update_staff, find_staff, search_all_staff, create_staff_table, close_database


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


class Staff(BaseModel):
    id: str = None
    username: str = None
    password: str = None


class FindStaff(BaseModel):
    username: str = None
    password: str = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 数据库方法调用
# close_database()


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
