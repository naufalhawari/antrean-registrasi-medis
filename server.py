from xmlrpc.server import SimpleXMLRPCServer
import time

class ClinicServer:
    def __init__(self):
        self.klinik_status = {
            "Klinik A": {"current_queue": 0, "estimated_wait_time": 0},
            "Klinik B": {"current_queue": 0, "estimated_wait_time": 0},
            "Klinik C": {"current_queue": 0, "estimated_wait_time": 0},
        }

    def register_patient(self, clinic_name, patient_info):
        

        # For simplicity, we'll just increment the queue count
        self.klinik_status[clinic_name]["current_queue"] += 1
        self.klinik_status[clinic_name]["estimated_wait_time"] += 10  # 10 Minutes per patient
        return f"Registration successful for {clinic_name}. Current Queue: {self.klinik_status[clinic_name]['current_queue']}"

    def get_queue_status(self, clinic_name):
        # Return the current queue status
        return {
            "current_queue": self.klinik_status[clinic_name]["current_queue"],
            "estimated_wait_time": self.klinik_status[clinic_name]["estimated_wait_time"],
        }

def run_server():
    server = SimpleXMLRPCServer(("0.0.0.0", 8000))  # Listen on all available interfaces
    clinic_server = ClinicServer()
    server.register_instance(clinic_server)
    print("Server listening on port 8000...")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
