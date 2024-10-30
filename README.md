# Shard Gossip Protocol Implementation

A distributed shard ownership management system using gossip protocol.

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
python -m unittest discover tests
```

## Usage

```python
from shard_gossip.node import Node
from shard_gossip.gossip import ShardOwnershipManager

# Create nodes
node1 = Node("node-1")
node2 = Node("node-2")

# Add peers
node1.add_peer("node-2")
node2.add_peer("node-1")

# Create managers
manager1 = ShardOwnershipManager(node1)
manager2 = ShardOwnershipManager(node2)

# Start gossip
manager1.start_gossip_round()
```
