import xmlrpc.client

queue_ids = []

class ClinicClient:
    def __init__(self, server_address):
        self.server = xmlrpc.client.ServerProxy(server_address)

    def register_patient(self, clinic_id, patient_info):
        queue_id = self.server.register_patient(clinic_id, patient_info)
        if queue_id == "none":
            print(f"Pendaftaran gagal. Klinik sedang tutup")
            return None
        else:
            queue_ids.append(queue_id)
            print(f"Pendaftaran berhasil. Kode antrian: {queue_id}")
            return queue_id

    def get_queue_status(self, clinic_id):
        status = self.server.get_queue_status(clinic_id)
        print(f"{status}")
    
    def get_menu(self):
        print(self.server.get_menu())

if __name__ == "__main__":
    server_address = "http://127.0.0.1:8000"  
    client = ClinicClient(server_address)


    
    client.get_menu()
    
    pilihan_menu = int(input("Pilihan menu: "))
    while (pilihan_menu <= 3 and pilihan_menu >= 1) or pilihan_menu == 9:

        if pilihan_menu != 9:
            name = input("Nama Lengkap: ")
            dob = input("Tanggal Lahir (contoh: 30-01-2003): ")

            patient_info = {"name": name, "dob": dob}
            queue_id = client.register_patient(pilihan_menu, patient_info)
            if queue_id != None:
                client.get_queue_status(queue_id)
        elif pilihan_menu == 9:
            if len(queue_ids) > 0:

                for queue_id in queue_ids:
                    client.get_queue_status(queue_id)
            else:
                print("Anda belum melakukan registrasi")
        client.get_menu()
        pilihan_menu = int(input("Pilihan menu: "))
        
