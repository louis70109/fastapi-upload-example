# FastAPI Example

- GET  '/': Health check.
- GET  '/upload': Upload file page.
- POST '/upload': Upload multi-file API.
  - Test case in 'tests/'.

## Prerequisite

- Python 3.7+
- Docker

## Development

```shell
pip install -r requirements.txt 
pytest tests
python main.py
```

or 

```shell
docker-compose up
```

```shell
curl http://localhost:5000/
```