import json

# Load the internal format data from the JSON file
with open('internal_format.json') as f:
    internal_data = json.load(f)

# Define a function to convert the internal format to the client format
def internal_to_client(data):
    client_data = {
        'ID': data['id'],
        'NAME': data['name'],
       
    }
    return client_data

# Convert the internal format to the client format
client_data = internal_to_client(internal_data)

# Save the client format data to a JSON file
with open('client_format.json', 'w') as f:
    json.dump(client_data, f, indent=4)

# Define a function to convert the client format to the internal format
def client_to_internal(data):
    internal_data = {
        'id': data['ID'],
        'name': data['NAME'],
        
    }
    return internal_data

# Load the client format data from the JSON file
with open('client_format.json') as f:
    client_data = json.load(f)

# Convert the client format to the internal format
internal_data = client_to_internal(client_data)

# Save the internal format data to a JSON file
with open('internal_format.json', 'w') as f:
    json.dump(internal_data, f, indent=4)

