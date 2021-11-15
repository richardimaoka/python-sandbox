import logging
import grpc
import kick_pb2
import kick_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = kick_pb2_grpc.KickServerStub(channel)
        response = stub.Kick(kick_pb2.KickRequest(kickerName="ab"))
    print("Kick client received: " + response.registrationId)


if __name__ == '__main__':
    logging.basicConfig()
    run()
