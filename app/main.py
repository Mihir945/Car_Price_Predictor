from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title="Car Price Prediction API", version="1.0.0")
app.add_middleware(LoggingMiddleware)

#link endpoints
app.include_router(routes_auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(routes_predict.router, prefix="/api", tags=["Prediction"])

# monitoring using Prometheus
Instrumentator().instrument(app).expose(app)

# add exception handler
register_exception_handlers(app)