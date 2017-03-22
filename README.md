# IDC Demo Lite

This is lite idc demo, full demo is [here](https://github.com/playniuniu/docker-demo-idc)

### Run

```bash
docker run -d --name demo-idc-lite -p 8000:8000 playniuniu/demo-idc-lite
```

### Manual install

This demo use python3 and flask, install from requirements.txt

```bash
python3 -m venv env/ 
./env/bin/pip install --upgrade pip 
./env/bin/pip install -r requirements.txt
./env/bin/gunicorn -d -b "0.0.0.0:8000" app:app
```

