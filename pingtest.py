import ping3
import time


def ping(host, count=4):
    """
    Ping the specified host and return TTL and RTT information.

    Parameters:
    - host (str): The target host to ping.
    - count (int): Number of ping requests to send.

    Returns:
    - List of dictionaries containing TTL and RTT information for each ping.
    """
    ping_results = []

    for i in range(count):
        # Perform a ping and get the result
        rtt = ping3.ping(host, unit="ms", size=64)

        # If the ping is successful, extract TTL and RTT
        if rtt is not None:
            result = ping3.verbose_ping(host, unit="ms", size=64)

            # Check if result is not None before accessing its properties
            if result is not None and result[1] is not None:
                ttl = result[1].ttl
                rtt = rtt * 1000  # Convert seconds to milliseconds
                ping_results.append({'ttl': ttl, 'rtt': rtt})

                print(f"Reply from {host}: TTL={ttl} RTT={rtt:.2f} ms")
            else:
                print(f"No reply from {host}")
        else:
            print(f"No reply from {host}")

        # Pause for a short time between pings
        time.sleep(1)

    return ping_results


if __name__ == "__main__":
    target_host = "8.8.8.8"
    ping_count = 4

    results = ping(target_host, ping_count)

    # Print the summary
    if results:
        avg_rtt = sum(result['rtt'] for result in results) / len(results)
        print(f"\nPing summary for {target_host}:")
        print(f"Avg RTT: {avg_rtt:.2f} ms")
    else:
        print(f"No successful pings to {target_host}")
