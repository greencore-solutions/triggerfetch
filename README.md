# triggerfetch

> Is your product in the answer when a shopper asks? For one barcode in one country: found (whether ChatGPT, Claude, Gemini and Grok name it, and where in the four it sits), likely why (the most probable reason from what the record shows: wrong name, missing barcode, not in the catalogue the AI reads, not verified, not orderable) and corrected (the brand's own words bound to its barcode, with a new receipt). One free check a day; then the brand's agent signs in.

Built and run by [wefetch](https://wefetch.ai/). This is the public connect kit, MIT. It holds no deploy code and no keys.

## Connect

- Endpoint: `https://triggerfetch.ai/mcp` (MCP, streamable HTTP)
- Agent card: `https://triggerfetch.ai/.well-known/agent-card.json` (copy in this repo, `agent-card.json`)
- For agents: https://triggerfetch.ai/llms.txt
- Site: https://triggerfetch.ai/
- Official MCP Registry: `ai.triggerfetch/triggerfetch` (`server.json` in this repo)

Any client that speaks streamable HTTP:

```json
{
  "url": "https://triggerfetch.ai/mcp",
  "transport": "streamable-http"
}
```

Claude Code:

```bash
claude mcp add --transport http triggerfetch https://triggerfetch.ai/mcp
```

List the tools with `python examples/generic_mcp_client.py`.

## Tools

| Tool | What it does |
|---|---|
| `check_product` | Is your product in the answer when a shopper asks? |
| `sign_in` | Sign in the brand's agent with its claim_seat identity: give the card address the brand claimed its seat with and one of its barcodes. |
| `sign_in_verify` | Finish sign-in: the token is read at the brand's domain and the barcode's seat on the hub must be the seat of that card. |
| `correct_product` | Corrected: the signed-in brand gives the words it wants its product found by (name, brand, size) for one barcode and one country. |
| `get_index` | The current edition of The AI Grocery Shopping Index: what the AIs answer when shoppers ask, by category and country, with each product by barcode, its answer share and shelf position, and orderable coverage per country. |

Artificial intelligence makes mistakes. Check what matters.
