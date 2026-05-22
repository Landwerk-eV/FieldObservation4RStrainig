from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from .config import DATA_DIR
from .geometry_ops import merge_polygon_features, split_polygon_feature
from .gpkg_service import GeoPackageService
from .schemas import MergeRequest, SaveFeaturesRequest, SplitRequest

app = FastAPI(title="Field Observation Web UI", version="0.1.0")
service = GeoPackageService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static_dir = Path(__file__).parent / "static"
templates_dir = Path(__file__).parent / "templates"
app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=str(templates_dir))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "data_dir": str(DATA_DIR),
        },
    )


@app.get("/api/health")
async def health() -> dict:
    return {"status": "ok", "data_dir": str(DATA_DIR)}


@app.get("/api/datasets")
async def list_datasets() -> dict:
    return {"datasets": service.list_datasets()}


@app.get("/api/datasets/{dataset_name}/meta")
async def dataset_meta(dataset_name: str) -> dict:
    try:
        return service.inspect(dataset_name)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/api/datasets/{dataset_name}/features")
async def get_features(dataset_name: str, layer: str | None = None) -> dict:
    try:
        return service.read_features(dataset_name, layer)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.put("/api/datasets/{dataset_name}/features")
async def put_features(dataset_name: str, body: SaveFeaturesRequest) -> dict:
    try:
        return service.save_features(dataset_name, body.feature_collection, body.layer)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/geometry/split")
async def split_geometry(body: SplitRequest) -> dict:
    try:
        return {"features": split_polygon_feature(body.feature, body.splitter)}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/geometry/merge")
async def merge_geometry(body: MergeRequest) -> dict:
    try:
        return {"feature": merge_polygon_features(body.features)}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
