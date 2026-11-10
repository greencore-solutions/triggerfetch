"""List the tools on this door over streamable HTTP. Python standard library only."""
import json
import urllib.request

URL = "https://triggerfetch.ai/mcp"
HEAD = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}


def rpc(body, session=None):
    headers = dict(HEAD)
    if session:
        headers["Mcp-Session-Id"] = session
    reply = urllib.request.urlopen(urllib.request.Request(URL, data=json.dumps(body).encode(), headers=headers), timeout=30)
    text = reply.read().decode("utf-8")
    payload = text.split("data: ")[-1] if "data: " in text else text
    return reply.headers.get("Mcp-Session-Id"), json.loads(payload)


session, first = rpc({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "connect-kit", "version": "1.0"}}})
print(first["result"]["serverInfo"])
_, tools = rpc({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}, session)
for tool in tools["result"]["tools"]:
    print(tool["name"])
