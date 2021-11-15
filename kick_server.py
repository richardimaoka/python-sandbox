from kick_pb2 import KickReply
from kick_pb2_grpc import KickServerServicer, add_KickServerServicer_to_server
from concurrent import futures
import grpc
import logging


class KickServer(KickServerServicer):
    def Kick(self, request, context):
        return KickReply(registrationId="a")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_KickServerServicer_to_server(KickServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
