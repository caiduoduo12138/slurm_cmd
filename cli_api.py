import uvicorn
import subprocess
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class JsonBody(BaseModel):
    cmd: str


@app.post("/cli")
def cli_api(json_body: JsonBody):
    command = json_body.cmd
    assert command.split(' ')[0] in ['vinfo', 'valloc', 'vacct', 'vbatch', 'vcancel',
                                     'vcontrol', 'vlogin', 'vlogout', 'vqueue', 'vrun'], "ERROR: invalid command input!"
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if len(tmp.stdout) > 0:
        out_string = tmp.stdout
    else:
        out_string = tmp.stderr

    return out_string


if __name__ == "__main__":
    uvicorn.run("cli_api:app", host="0.0.0.0", port=7777)
