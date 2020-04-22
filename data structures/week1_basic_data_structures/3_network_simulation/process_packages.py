# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.times = deque()

    def process(self, request):
        while len(self.times) and self.times[0] <= request.arrived_at:
            self.times.popleft()

        if len(self.times) == self.size:
            return Response(True, -1)

        if len(self.times) >= 1:
            last = self.times[-1]
            self.times.append(request.time_to_process + last)
            return Response(False, last)

        self.times.append(request.arrived_at + request.time_to_process)
        return Response(False, request.arrived_at)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
