from fastapi import FastAPI
from db import db_connection
from viko_router import router

app = FastAPI(docs_url="/")
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    await db_connection.connect()


@app.on_event("shutdown")
async def shutdown_event():
    await db_connection.disconnect()
