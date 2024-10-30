import time
import logging
from typing import Dict, Set
from .exceptions import InvalidStateError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ShardState:
    def __init__(self, shard_id: str, owner: str):
        self.shard_id = shard_id
        self.owner = owner
        self.version = 0
        self.state = "ACTIVE"
        self.last_modified = time.time()

    def to_dict(self) -> dict:
        return {
            "shard_id": self.shard_id,
            "owner": self.owner,
            "version": self.version,
            "state": self.state,
            "last_modified": self.last_modified
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'ShardState':
        state = cls(data["shard_id"], data["owner"])
        state.version = data["version"]
        state.state = data["state"]
        state.last_modified = data["last_modified"]
        return state

class Node:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.shard_map: Dict[str, ShardState] = {}
        self.peers: Set[str] = set()
        self.gossip_round = 0
        logger.info(f"Initialized node {node_id}")

    def add_shard(self, shard_id: str) -> ShardState:
        if shard_id in self.shard_map:
            raise InvalidStateError(f"Shard {shard_id} already exists")
        
        state = ShardState(shard_id, self.node_id)
        self.shard_map[shard_id] = state
        logger.info(f"Node {self.node_id} added shard {shard_id}")
        return state

    def add_peer(self, peer_id: str) -> None:
        if peer_id != self.node_id:
            self.peers.add(peer_id)
            logger.info(f"Node {self.node_id} added peer {peer_id}")

    def remove_peer(self, peer_id: str) -> None:
        self.peers.discard(peer_id)
        logger.info(f"Node {self.node_id} removed peer {peer_id}")

    def get_shard_state(self, shard_id: str) -> ShardState:
        return self.shard_map.get(shard_id)
