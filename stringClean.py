def answer(chunk, word):
    # Declare empty list for results
    outputs = []
    # Find indices in string where word occurs
    instance = []
    
    for i in range(len(chunk)):
        if chunk.startswith(word, i):
            instance.append(i)
            
    # Loop through those instance
    for i in instance:
        # Take out occurrence of word
        c = chunk[0:i] + chunk[i+len(word):len(chunk)]
        # One by one, take out remaining occurrences of word
        while c.find(word) != -1:
            c = c.replace(word, '', 1)
        # Append watered down string to result list
        outputs.append(c)
    # Sort the list by lexicographically earliest string
    outputs.sort(key=lambda item: (len(item), item))
    # Return 1st element in result list
    return outputs[0]
