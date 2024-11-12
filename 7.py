# Initial packets in the bucket storage
storage = 0

# Total number of times bucket content is checked
no_of_queries = 4

# Total number of packets that can be accommodated in the bucket
bucket_size = 10

# Number of packets that enter the bucket at a time
input_pkt_size = 4

# Number of packets that exit the bucket at a time
output_pkt_size = 1

for i in range(no_of_queries):
    # Calculate space left in the bucket
    size_left = bucket_size - storage
    
    if input_pkt_size <= size_left:
        # Update storage by adding incoming packets
        storage += input_pkt_size
    else:
        # Packet loss occurs when incoming packets exceed available space
        print("Packet loss =", input_pkt_size)
    
    # Display current buffer status
    print(f"Buffer size= {storage} out of bucket size = {bucket_size}")
    
    # As packets are sent out into the network, reduce storage
    storage -= output_pkt_size
    
    # Ensure storage does not go below zero
    if storage < 0:
        storage = 0