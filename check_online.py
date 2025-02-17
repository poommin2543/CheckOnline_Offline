from speedtest import Speedtest
from ping3 import ping
import time
from tabulate import tabulate

def test_speed():
    st = Speedtest()
    st.get_best_server()
    download_speed = st.download() / (1024 * 1024)  # convert to Mbps
    upload_speed = st.upload() / (1024 * 1024)  # convert to Mbps

    return download_speed, upload_speed

# def test_latency(host='8.8.8.8', count=5):
#     total_ping = 0
#     min_ping = float('inf')
#     max_ping = float('-inf')

#     for _ in range(count):
#         current_ping = ping(host)
#         total_ping += current_ping
#         min_ping = min(min_ping, current_ping)
#         max_ping = max(max_ping, current_ping)
#         time.sleep(1)  # 1 second interval between pings

#     avg_ping = total_ping / count
#     jitter = max_ping - min_ping

#     return avg_ping, jitter

def test_latency(host='8.8.8.8', count=5):
    total_ping = 0
    successful_pings = 0
    min_ping = float('inf')
    max_ping = float('-inf')

    for _ in range(count):
        current_ping = ping(host)
        if current_ping is not None:
            successful_pings += 1
            total_ping += current_ping
            min_ping = min(min_ping, current_ping)
            max_ping = max(max_ping, current_ping)
        time.sleep(1)  # 1 second interval between pings

    if successful_pings > 0:
        avg_ping = total_ping / successful_pings
        jitter = max_ping - min_ping
    else:
        avg_ping = None
        jitter = None

    return avg_ping, jitter

def test_packet_loss(host='8.8.8.8', count=10):
    sent_packets = count
    received_packets = 0

    for _ in range(count):
        if ping(host, timeout=2) is not None:
            received_packets += 1

    packet_loss = (sent_packets - received_packets) / sent_packets * 100

    return packet_loss

# if __name__ == "__main__":
#     results = []
#     download_sum, upload_sum, latency_sum, jitter_sum, packet_loss_sum = 0, 0, 0, 0, 0
    
#     for i in range(10):
#         download, upload = test_speed()
#         latency, jitter = test_latency()
#         packet_loss = test_packet_loss()
        
#         download_sum += download
#         upload_sum += upload
#         latency_sum += latency
#         jitter_sum += jitter
#         packet_loss_sum += packet_loss
        
#         results.append([i + 1, f"{download:.2f} Mbps", f"{upload:.2f} Mbps", f"{latency:.2f} ms", f"{jitter:.2f} ms", f"{packet_loss:.2f} %"])
#         print(i + 1, f"{download:.2f} Mbps", f"{upload:.2f} Mbps", f"{latency:.2f} ms", f"{jitter:.2f} ms", f"{packet_loss:.2f} %")

#     download_mean = download_sum / 10
#     upload_mean = upload_sum / 10
#     latency_mean = latency_sum / 10
#     jitter_mean = jitter_sum / 10
#     packet_loss_mean = packet_loss_sum / 10

#     results.append(["Mean", f"{download_mean:.2f} Mbps", f"{upload_mean:.2f} Mbps", f"{latency_mean:.2f} ms", f"{jitter_mean:.2f} ms", f"{packet_loss_mean:.2f} %"])
    
#     headers = ["Test No.", "Download", "Upload", "Latency", "Jitter", "Packet Loss"]
#     table = tabulate(results, headers=headers, tablefmt="grid")
#     print(table)
if __name__ == "__main__":
    results = []
    download_sum, upload_sum, latency_sum, jitter_sum, packet_loss_sum = 0, 0, 0, 0, 0
    successful_latency_tests = 0
    
    for i in range(10):
        download, upload = test_speed()
        latency, jitter = test_latency()
        packet_loss = test_packet_loss()
        
        download_sum += download
        upload_sum += upload
        if latency is not None and jitter is not None:
            latency_sum += latency
            jitter_sum += jitter
            successful_latency_tests += 1
        packet_loss_sum += packet_loss
        
        results.append([i + 1, f"{download:.2f} Mbps", f"{upload:.2f} Mbps", f"{latency:.2f} ms" if latency is not None else "N/A", f"{jitter:.2f} ms" if jitter is not None else "N/A", f"{packet_loss:.2f} %"])
        print(i + 1, f"{download:.2f} Mbps", f"{upload:.2f} Mbps", f"{latency:.2f} ms" if latency is not None else "N/A", f"{jitter:.2f} ms" if jitter is not None else "N/A", f"{packet_loss:.2f} %")

    download_mean = download_sum / 10
    upload_mean = upload_sum / 10
    latency_mean = latency_sum / successful_latency_tests if successful_latency_tests > 0 else None
    jitter_mean = jitter_sum / successful_latency_tests if successful_latency_tests > 0 else None
    packet_loss_mean = packet_loss_sum / 10

    results.append(["Mean", f"{download_mean:.2f} Mbps", f"{upload_mean:.2f} Mbps", f"{latency_mean:.2f} ms" if latency_mean is not None else "N/A", f"{jitter_mean:.2f} ms" if jitter_mean is not None else "N/A", f"{packet_loss_mean:.2f} %"])
    
    headers = ["Test No.", "Download", "Upload", "Latency", "Jitter", "Packet Loss"]
    table = tabulate(results, headers=headers, tablefmt="grid")
    print(table)
