patients = [
    {"name": "John", "age": 45, "diagnosis": "flu"},
    {"name": "Mary", "age": 62, "diagnosis": "pneumonia"},
    {"name": "Sarah", "age": 28, "diagnosis": "diabetes"},
    {"name": "Michael", "age": 71, "diagnosis": "hypertension"},
    {"name": "Emma", "age": 33, "diagnosis": "asthma"}
]

total_age = 0;
num_of_patients = 0;
for p in patients:
    total_age += p["age"]
    num_of_patients = num_of_patients + 1
    if(p["age"] > 60):
        print(p['name'])

print("Average age of the patients is", total_age/num_of_patients)