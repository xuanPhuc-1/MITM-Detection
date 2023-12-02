import time
from scapy.all import IP, ICMP, sr1


def ping(host):
    # Gửi gói tin ICMP (ping) đến host
    packet = IP(dst=host) / ICMP()
    start_time = time.time()

    try:
        reply = sr1(packet, timeout=1, verbose=0)
        end_time = time.time()

        # Tính toán RTT
        rtt = (end_time - start_time) * 1000  # chuyển đổi sang milliseconds
        print(f"Round-Trip Time (RTT): {rtt:.2f} ms")

        # Lấy giá trị TTL từ gói tin reply
        if reply is not None:
            ttl = reply.ttl
            print(f"Time-to-Live (TTL): {ttl}")

            return rtt  # Trả về giá trị RTT
        else:
            print("Không nhận được phản hồi từ host.")
            return None
    except Exception as e:
        print(f"Lỗi: {e}")
        return None


# Thay đổi địa chỉ IP thành địa chỉ của host bạn muốn kiểm tra
target_host = "10.0.0.16"

while True:
    rtt_value = ping(target_host)
    if rtt_value is not None:
        # Sử dụng giá trị rtt_value theo nhu cầu của bạn
        pass

    # delay 1s
    time.sleep(1)
