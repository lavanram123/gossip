class ShardGossipError(Exception):
    """Base exception for shard gossip errors"""
    pass

class TransferError(ShardGossipError):
    """Raised when shard transfer fails"""
    pass

class OwnershipError(ShardGossipError):
    """Raised when there's an ownership conflict"""
    pass

class InvalidStateError(ShardGossipError):
    """Raised when shard state is invalid"""
    pass
