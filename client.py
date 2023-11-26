import xmlrpc.client

class ClinicClient:
    def __init__(self, server_address):
        self.server = xmlrpc.client.ServerProxy(server_address)

    def register_patient(self, clinic_id, patient_info):
        result = self.server.register_patient(clinic_id, patient_info)
        print(result)

    def get_queue_status(self, clinic_id):
        status = self.server.get_queue_status(clinic_id)
        print(f"Status antrian: {status}")

    def get_menu(self):
        print(self.server.get_menu())

if __name__ == "__main__":
    server_address = "http://192.168.100.9:8000"  # Replace <server-ip> with the actual IP address of the server device
    client = ClinicClient(server_address)


    
    client.get_menu()
    
    pilihan_menu = int(input("Pilihan menu: "))
    while pilihan_menu <= 3 and pilihan_menu >= 1:

        medic_record_number = int(input("Nomor rekam medis: "))
        name = input("Nama Lengkap: ")
        dob = input("Tanggal Lahir (contoh: 30-01-2003): ")

        patient_info = {"medic_record_number": medic_record_number, "name": name, "dob": dob}
        client.register_patient(pilihan_menu, patient_info)
        client.get_queue_status(pilihan_menu)

        pilihan_menu = int(input("Pilihan menu: "))

        client.get_menu()
