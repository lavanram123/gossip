import unittest
from shard_gossip.node import Node, ShardState
from shard_gossip.exceptions import InvalidStateError

class TestNode(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.node = Node("node-1")

    def test_node_initialization(self):
        """Test node initialization with default values"""
        self.assertEqual(self.node.node_id, "node-1")
        self.assertEqual(len(self.node.shard_map), 0)
        self.assertEqual(len(self.node.peers), 0)

    def test_add_shard(self):
        """Test adding a new shard to the node"""
        state = self.node.add_shard("shard-1")
        self.assertEqual(state.shard_id, "shard-1")
        self.assertEqual(state.owner, "node-1")
        self.assertEqual(state.state, "ACTIVE")

    def test_add_duplicate_shard(self):
        """Test adding a duplicate shard raises exception"""
        self.node.add_shard("shard-1")
        with self.assertRaises(InvalidStateError):
            self.node.add_shard("shard-1")

    def test_add_remove_peer(self):
        """Test adding and removing peers"""
        self.node.add_peer("node-2")
        self.assertIn("node-2", self.node.peers)
        
        self.node.remove_peer("node-2")
        self.assertNotIn("node-2", self.node.peers)

if __name__ == '__main__':
    unittest.main()
