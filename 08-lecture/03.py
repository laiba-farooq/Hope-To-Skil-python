import time  # Import time module to measure execution time

# Decorator to log patient details before consultation
def log_decorator(func):
    def wrapper(patient_name):
        print(f"📋 Recording patient details: {patient_name}")
        return func(patient_name)  # Call the original function
    return wrapper

# Decorator to measure consultation time
def timer_decorator(func):
    def wrapper(patient_name):
        start = time.time()  # Record start time
        result = func(patient_name)  # Call the original function
        end = time.time()  # Record end time
        print(f"⏳ Consultation time: {end - start:.4f} seconds")
        return result
    return wrapper

# Applying multiple decorators to a doctor’s consultation
@log_decorator  # First, log patient details
@timer_decorator  # Then, measure consultation time
def doctor_consultation(patient_name):
    print(f"👨‍⚕️ Doctor is consulting {patient_name}...")
    time.sleep(1)  # Simulate consultation time
    print(f"📝 Prescription given to {patient_name}")

# Simulating a patient visiting the doctor
doctor_consultation("Alice")
