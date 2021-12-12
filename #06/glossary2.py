programming_words = {
    'if' : 'indicates a condition to be fulfilled', 
    'del': 'permanent deletion',
    'get' : 'allows a non-error response when no key-value is available',
    'elif' : 'different tests until one passes and rest of block is ignored',
    'boolean' : 'True/False conditional tests',
    'in' : 'checks whether a value is in a list',
    'items' : 'returns list of key-value pairs',
    'keys' : 'assigns one key to a variable at a time',
    'sorted' : 'lists all keys and sort alphabetically before looping',
    'for' : 'creates a loop',
    'set' : 'each item returns as unique, no doubles, not a dictionary',
    }

print(programming_words)
print(f"\nif:\n    {programming_words['if']}.")
print(f"\ndel:\n    {programming_words['del']}.")
print(f"\nget:\n    {programming_words['get']}.")
print(f"\nelif:\n    {programming_words['elif']}.")
print(f"\nboolean:\n    {programming_words['boolean']}.")
print(f"\nin:\n    {programming_words['in']}.")

for words, meanings in programming_words.items():
    print(f"{words}:\n\t{meanings}")