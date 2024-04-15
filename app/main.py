# main.py
import time
import requests
import grpc
from qrl.proto import qrl_pb2_grpc

def get_blockheight():
    """
    Retrieves the current block height from the QRL node.

    Returns:
        int: The current block height.
    """
    channel = grpc.insecure_channel('localhost:19009')
    stub = qrl_pb2_grpc.PublicAPIStub(channel)
    response = stub.GetStats(qrl_pb2.GetStatsReq())
    return response.block_height

def is_node_synced():
    """
    Checks if the QRL node is synced with the explorer.

    Returns:
        bool: True if the node is synced, False otherwise.
    """
    # first grab the latest known blockheight from the explorer
    explorerBlockheight = requests.get('https://explorer.theqrl.org/api/blockheight').json()['height']
    # using grpc grab the blockheight from the node
    nodeBlockheight = get_blockheight()
    # compare the two
    if explorerBlockheight == nodeBlockheight:
        return True

def fill_database():

    pass

def watch_chain():

    pass

while not is_node_synced():
    print("Syncing...")
    time.sleep(30)

print("Node is synced.")

#fill_database()

#while True:
#    watch_chain()
#    time.sleep(10)