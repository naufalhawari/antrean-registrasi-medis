from xmlrpc.server import SimpleXMLRPCServer
import threading
import time

QUEUE_TIME = 10

class ClinicServer:
    def __init__(self):
        self.klinik_status = {
            1: {"name": "Klinik A", "current_queue": 0, "estimated_wait_time": 0, "open": True, "patients": []},
            2: {"name": "Klinik B", "current_queue": 0, "estimated_wait_time": 0, "open": False, "patients": []},
            3: {"name": "Klinik C", "current_queue": 0, "estimated_wait_time": 0, "open": True, "patients": []},
        }



    def register_patient(self, clinic_id, patient_info):


        
        # For simplicity, we'll just increment the queue count
        self.klinik_status[clinic_id]["current_queue"] += 1
        self.klinik_status[clinic_id]["estimated_wait_time"] += QUEUE_TIME
        return f"Pendaftaran berhasil. Nomor antrian: {self.klinik_status[clinic_id]['current_queue']}"

    def get_queue_status(self, clinic_id):
        # Return the current queue status
        return {
            "current_queue": self.klinik_status[clinic_id]["current_queue"],
            "estimated_wait_time": self.klinik_status[clinic_id]["estimated_wait_time"],
        }
    
    def get_menu(self):
        menu_text = "Selamat Datang di Antredis\n"
        # open_klinik_count = 0
        for id in self.klinik_status.keys():
            if (self.klinik_status[id]["open"]):
                # open_klinik_count += 1
                menu_text += f"{id}. {self.klinik_status[id]['name']}\n"
        
        return menu_text


def run_server():
    server = SimpleXMLRPCServer(("0.0.0.0", 8000))  # Listen on all available interfaces
    clinic_server = ClinicServer()
    server.register_instance(clinic_server)
    print("Server listening on port 8000...")

    # thread_dequeue = threading.Thread(dequeue, args=(clinic_server,))
    # thread_dequeue.start()
    server.serve_forever()
    # thread_dequeue.join()

if __name__ == "__main__":
    run_server()
