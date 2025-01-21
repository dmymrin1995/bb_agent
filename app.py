from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/home")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/hellobot/")
async def read_item(name: str):
    return {"message": f"Hello, {name}"}
