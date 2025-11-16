from fastapi import FastAPI
from datetime import datetime
from typing import Dict

app = FastAPI(title="Server Date API", version="1.0.0")


@app.get("/date")
async def get_server_date() -> Dict[str, str]:
    """Возвращает текущую дату и время на сервере"""
    current_date = datetime.now()
    return {
        "date": current_date.strftime("%Y-%m-%d")
    }

@app.get("/time")
async def get_server_time() -> Dict[str, str]:
    """Возвращает текущее время на сервере"""
    current_time = datetime.now().strftime("%H:%M:%S")
    return {
        "time": current_time
    }

@app.get("/datetime")
async def get_server_datetime() -> Dict[str, str]:
    """Возвращает текущую дату и время на сервере"""
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "datetime": current_datetime
    }

@app.get("/iso")
async def get_server_iso() -> Dict[str, str]:
    """Возвращает текущую дату и время на сервере в формате ISO"""
    current_iso = datetime.now().isoformat()
    return {
        "iso": current_iso
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)