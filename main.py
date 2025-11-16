from fastapi import FastAPI
from datetime import datetime
from typing import Dict

app = FastAPI(title="Server Date API", version="1.0.0")


@app.get("/date")
async def get_server_date() -> Dict[str, str]:
    """Возвращает текущую дату и время на сервере"""
    current_date = datetime.now()
    return {
        "date": current_date.strftime("%Y-%m-%d"),
        "time": current_date.strftime("%H:%M:%S"),
        "datetime": current_date.strftime("%Y-%m-%d %H:%M:%S"),
        "iso": current_date.isoformat()
    }

