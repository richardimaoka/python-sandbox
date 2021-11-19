import logging
import time

import grpc

import route_guide_pb2
import route_guide_pb2_grpc





def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)


if __name__ == '__main__':
    logging.basicConfig()
    run()
