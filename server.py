from xmlrpc.server import SimpleXMLRPCServer
import threading
import time

QUEUE_TIME = 10

class ClinicServer:
    def __init__(self):
        self.klinik_status = {
            1: {"name": "Klinik A", "status": "Buka", "queue_wait_time": [], "queue_patients": []},
            2: {"name": "Klinik B", "status": "Tutup", "queue_wait_time": [], "queue_patients": []},
            3: {"name": "Klinik C", "status": "Buka", "queue_wait_time": [], "queue_patients": []},
        }

        self.thread_dequeue = threading.Thread(target = self.dequeue)

    
    def dequeue(self):
        while True:
            time.sleep(QUEUE_TIME)
            print("UPDATING QUEUES...")
            for clinic_id in self.klinik_status.keys():
                for i in range(len(self.klinik_status[clinic_id]["queue_wait_time"])):
                    self.klinik_status[clinic_id]["queue_wait_time"][i] = max([0, self.klinik_status[clinic_id]["queue_wait_time"][i] - QUEUE_TIME])
                print(f'{self.klinik_status[clinic_id]["name"]}: last queue waiting time = {max([0] + self.klinik_status[clinic_id]["queue_wait_time"])}')
            

            

    def register_patient(self, clinic_id, patient_info):
        if (self.klinik_status[clinic_id]["status"] == "Tutup"):
            return "none"
        
        
        self.klinik_status[clinic_id]["queue_patients"].append(patient_info)

        last_queue_wait_time = max(self.klinik_status[clinic_id]["queue_wait_time"] + [0])
        
        self.klinik_status[clinic_id]["queue_wait_time"].append(last_queue_wait_time + QUEUE_TIME)

        
        return f"{clinic_id}{len(self.klinik_status[clinic_id]['queue_patients']) - 1}"


    def get_queue_status(self, queue_id):
        clinic_id = int(queue_id[0])
        queue_wait_time_index = int(queue_id[1:])
        estimation_wait_time = self.klinik_status[clinic_id]["queue_wait_time"][queue_wait_time_index]
        return f"Estimasi waktu tunggu kode antrian {queue_id}: {estimation_wait_time}"
    
    def get_menu(self):
        menu_text = "Selamat Datang di Antredis\n"
        menu_text += "No.\tNama\t\tStatus\tEstimasi Waktu Tunggu\n"
        for id in self.klinik_status.keys():
            
            menu_text += f"{id}.\t{self.klinik_status[id]['name']}\t{self.klinik_status[id]['status']}\t{max([0] + self.klinik_status[id]['queue_wait_time'])}\n"
        
        menu_text += "9. Lihat semua status antrian\n"
        menu_text += "0. Keluar"
        return menu_text

def run_server():
    server = SimpleXMLRPCServer(("0.0.0.0", 8000))  # Listen on all available interfaces
    clinic_server = ClinicServer()
    server.register_instance(clinic_server)
    print("Server listening on port 8000...")

    clinic_server.thread_dequeue.start()
    server.serve_forever()
    clinic_server.thread_dequeue.join()

if __name__ == "__main__":
    run_server()
