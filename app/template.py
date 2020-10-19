import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.router.Staffs import create_staff, delete_staff, update_staff, find_staff, search_all_staff, create_staff_table, close_database

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
    id: int
    username: str = None
    phonenum: int
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


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None


# class User(BaseModel):
#     username: str
#     full_name: str = None


# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name


# fake_items_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]


# @app.get("/items")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#         user_id: int, item_id: str, q: str = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item


# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, limit: Optional[int] = None):
#     item = {"item_id": item_id, "limit": limit}
#     return item


# @app.get("/model/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     if model_name.value == "lenent":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}


# @app.get("/results")
# async def read_results(q: str = Query(None, min_length=3, max_length=50), regex="^fixedquery$"):
#     results = {"items": [{"items_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/readitems/{item_id}")
# async def read_items(
#         q: str, item_id: int = Path(..., title="The ID of the item to get")
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# @app.post("/order/")
# async def create_item(item: Item):
#     return item


# @app.put("/items2/{item_id}")
# async def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", ge=0, le=100),
#         q: str = None,
#         item: Item = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


# @app.put("/items3/{item_id}")
# async def update_item(*, item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results


# @app.get("/items-header/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"Some-Errror": "There goes my error"}
#         )
#     return {"item": items[item_id]}


# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow ..."}
#     )


# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return JSONResponse({'mes': '触发了 RequestValidationError 错误，错误信息：%s 你妹的错了！' % (str(exc))})


# @app.get("/items5/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


# async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/items6/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     commons.update({'小钟': '同学'})


# @app.get("/users/")
# async def read_uers(commons: dict = Depends(common_parameters)):
#     return commons
