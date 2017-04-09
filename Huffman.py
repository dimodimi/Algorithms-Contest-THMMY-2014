from heapq import heappush, heappop, heapify

#Returns a list of tuples ("character", frequency) with increasing frequency
def freq(s):
    freqs = dict()
    for i in range(len(s)):
        if s[i] in freqs:
            freqs[s[i]] += 1
        else:
            freqs[s[i]] = 1

    return freqs

def encode_cost(symbols_freq):
    #List of lists, form [total_frequency, total_bit_count]
    heap = [ [freq, 0] for symbol, freq in symbols_freq.items()]
    heapify(heap)
    while len(heap) > 1:
        left  = heappop(heap)
        right = heappop(heap)
        #The new node will have as frequency the sum of the frequencies of the two "children"
        # and the cost will be the costs of the two children nodes + their frequencies
        #because at each step the nodes go deeper one level (their bit represenation increases by 1 ) 
        new_node = [ left[0] + right[0],  left[1] + left[0] + right[1] + right[0] ]
        heappush(heap, new_node)

    final = heappop(heap)
    return final[1]

def huffman():
    message_len = int(raw_input())
    message     = raw_input()    
    symbols     = freq(message)
    total_cost  = encode_cost(symbols)

    return  int(float(8*message_len)/float(total_cost) * 100 )

print str(huffman()) + '%'